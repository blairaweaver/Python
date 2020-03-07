from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

cat_encoder = OneHotEncoder();

data = load_data('adult.data.txt')

print(data.head())