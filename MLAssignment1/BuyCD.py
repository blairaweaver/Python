# This is to import everything that is needed
from sklearn import tree
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import graphviz


def load_data(filename):
    return pd.read_csv(filename)


ordinal_encoder = OrdinalEncoder()

# Loads training data and prints head
train = load_data('train.csv')
train.head()

# Loads test data and prints head
test = load_data('test.csv')
test.head()

# Encodes the catagorical data for sklearn
# Type
train.Type = ordinal_encoder.fit_transform(train.Type.values.reshape(-1, 1))
test.Type = ordinal_encoder.fit_transform(test.Type.values.reshape(-1, 1))
# Price
train.Price = ordinal_encoder.fit_transform(train.Price.values.reshape(-1, 1))
test.Price = ordinal_encoder.fit_transform(test.Price.values.reshape(-1, 1))
# Category
train.Category = ordinal_encoder.fit_transform(train.Category.values.reshape(-1, 1))
test.Category = ordinal_encoder.fit_transform(test.Category.values.reshape(-1, 1))

# get Decision tree with train data
feature_cols = ['Type', 'Price']
X = train.loc[:, feature_cols]
y = train.Category
tree_clf = DecisionTreeClassifier()
tree_clf.fit(X, y)

# Print tree in notebook
dot_data = tree.export_graphviz(
    tree_clf,
    out_file=None,
    feature_names=feature_cols,
    rounded=True,
    filled=True)
graph = graphviz.Source(dot_data)

# makes the pdf of the tree
graph.render('test', view=True)

# Use tree to predict test
X = test.loc[:, feature_cols]
output = tree_clf.predict(X)
output

# expected values
answer = test.Category.values
answer

# calculates the number of correctly evaluated entries from the test
right = 0
for i, x in enumerate(output):
    if x == answer[i]:
        right += 1

print("{} out of {} correctly evaluated".format(right, len(output)))
