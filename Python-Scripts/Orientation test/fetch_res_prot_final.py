import re
from argparse import ArgumentParser, FileType
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


parser = ArgumentParser(epilog='''This program will fetch state information from cpout and
                                outputs kde plot for each pH.''')

parser.add_argument('-n','--resnum', dest='resnum', type=int, help='''Residue number(index in cpout) to fetch protonation state''')

parser.add_argument('-ch', '--chunk', dest='chunk', type=int, nargs='+', help=''' Input all the cpout chunks for one simulation at one pH''')

parser.add_argument('-pH','--pH', dest='pH', type=float, nargs='+', help='''Input all the pH values to get plots''')
# parser.add_argument('-f', '--files', dest='files', nargs='+', type=FileType('r'), help=" Two column file format")

opt = parser.parse_args()

# This will make regex
regex_str = 'Time:[\s\S]+?Residue\s+'+ str(opt.resnum) + '\sState:\s+(\d)'
re_pattern_prot_stat = re.compile(bytes(regex_str, encoding='utf-8'))
dtype_prot_stat = [('prot_state', np.int32)]




def fetch_prot_state(pH_value):

# This part will put all the file names into list based on chunk and pH values
    file_list = []
    df_prot_state = pd.DataFrame()
    for chunk in opt.chunk:
        file_str = '1C2T_reordered_' + ("{0:.2f}".format(chunk)) + '.pH_' + str("{0:.2f}".format(pH_value))
        file_list.append(file_str)

# Protonation state has been fetched from cpout files and last value has been truncated.
    for files in file_list:
        prot_state = np.fromregex(files, re_pattern_prot_stat, dtype=dtype_prot_stat)
        df1 = pd.DataFrame(prot_state[:-1])
        df_prot_state = pd.concat([df_prot_state, df1], ignore_index=True)
    return (df_prot_state)

# df_prot_state = fetch_prot_state(4.00)

# Reading two column distance files formatted by tab or more than one space.
def read_distance_file(pH_value):
    file_dist_measure = 'd1_108@NE2_115@O_' + str("{0:.2f}".format(pH_value)) + '.dat'
    df_dist = pd.read_csv(file_dist_measure, sep='\s+', names=["Value"], skiprows=1, usecols=[1,])
    return (df_dist)

# Concatenate distance and protonation state in one dataframe
# and creating dictionary of dataframes
dict_df = {}
for pH in opt.pH:

    # Formatted pH value
    pH_f = np.float("{0:.2f}".format(pH))

    df_prot_state = fetch_prot_state(pH_f)
    df_dist = read_distance_file(pH_f)
    # print(df_dist)

    df_prot_state_dist = pd.concat([df_prot_state, df_dist], ignore_index=True, axis=1)

    dict_df[pH_f] = df_prot_state_dist


# Plotting kde using matplotlib and scipy
def kde_estimate(x, xmin, xmax, y, ymin, ymax):
    # Peform the kernel density estimate
    xx, yy = np.mgrid[xmin:xmax:200j, ymin:ymax:200j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)

    return(xx, yy, f)


fig = plt.figure(figsize=(14, 8.0))

# Increasing the font of all the texts in plot
import matplotlib
matplotlib.rcParams.update({'font.size': 22})

# Creating subplots and axes dynamically
axes = [plt.subplot(1,len(opt.pH),i+1) for i in range(len(opt.pH))]

# Labelling xaxes and title
for ax,pH in zip(axes, opt.pH):
    ax.set_title("pH-"+ str("{0:.2f}".format(pH)))
    ax.set_xlabel('$d H108@N\epsilon2-Y115@O$')
    ax.set_yticks(range(3))
    ax.set_xticks(range(6))

plt.subplots_adjust(wspace=0, hspace=0)

# Deleting labels for other sharedy axes
plt.setp([a.get_yticklabels() for a in axes[1:]], visible=False)

# Setting the number of yticklabels on first strip of plot
string = (np.array(['$HIP-N\delta1$ $N\epsilon2$', '$HID-N\delta1$ ', '$HIE-N\epsilon2$']))
# setting how many yticks a plot can have for first f
axes[0].set_yticks(range(3))
# Passing the string as label
axes[0].set_yticklabels(string, rotation=45)

# plotting for each pH
for i, pH in enumerate(opt.pH):

    # Formatted pH value
    pH_f = np.float("{0:.2f}".format(pH))

    # pH - 4.00
    x = dict_df[pH_f][1]
    y = dict_df[pH_f][0]

    xmin, xmax = 1.5, 7.0
    ymin, ymax = -0.5, 2.5

    xx, yy, f = kde_estimate(x, xmin, xmax, y, ymin, ymax)

    axes[i].set_xlim(xmin, xmax)
    axes[i].set_ylim(ymin, ymax)
    # Contourf plot
    cfset = axes[i].contourf(xx, yy, f, cmap='BuGn')
    # legend = ax.legend(loc='upper center', shadow=True)
    # Contour plot
    #cset = axes[i].contour(xx, yy, f, colors='k')
    # Label plot
    #axes[i].clabel(cset, inline=1, fontsize=10)

# plt.savefig("ter_H108-prot_d108NE2-115O.png", dpi=600)
plt.show()

