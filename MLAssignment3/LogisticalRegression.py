import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix

def load_data(filename):
    # Load the data into a pandas dataframe
    return pd.read_csv(filename)

def pandas_encode_data(dataframe):
    ## Get rid of????
    # uses the pandas one-hot encoding (pg 216 of Introduction to Machine Learning with Python
    return pd.get_dummies(dataframe)

def define_features(dataframe, start, end, yfeature):
    # Splits the encoded data into the X and y
    # This only works for features that are adjacent
    features = dataframe.loc[:, start:end]
    X = features.values
    y = dataframe[yfeature].values
    return X, y

def split_data(X, y, test_size):
    # Splits the test data into train and test based on user define test size
    return train_test_split(X, y, test_size=test_size, random_state=42)

clf = SGDClassifier(loss='log', penalty='l2', random_state=0)

data = load_data('adult.data.txt')
data_dummies = pd.get_dummies(data)

# Using all the features in training
# From multiple runs, will vary widely in the accuracy
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
n_corret = sum(y_pred == data_y_test)
print("Accuracy of the model using all columns", n_corret/len(data_y_test))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))

# Using only type of employment and education
X, y = define_features(data_dummies, 'type_employer_Federal-gov', 'education_Some-college', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
n_corret = sum(y_pred == data_y_test)
print("Accuracy of the model using employment and education", n_corret/len(data_y_test))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))

# Using Occupation
X, y = define_features(data_dummies, 'occupation_Adm-clerical', 'occupation_Transport-moving', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
n_corret = sum(y_pred == data_y_test)
print("Accuracy of the model using occupation", n_corret/len(data_y_test))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))

# Using education and occupation
features = data_dummies[list(data_dummies.loc[:, 'education_10th':'education_Some-college'] + data_dummies.loc[:, 'occupation_Adm-clerical':'occupation_Transport-moving'])]
X = features.values
y = data_dummies['income_>50K'].values
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
n_corret = sum(y_pred == data_y_test)
print("Accuracy of the model using occupation and education", n_corret/len(data_y_test))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))


# print(list(data_dummies.columns))
# print(data_dummies.info())
# features = data_dummies.loc[:, 'age': 'country_Yugoslavia']
# X = features.values
# y = data_dummies['income_>50K'].values
# data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
# print("X.shape: {} y.shape: {}".format(X.shape, y.shape))
# clf = SGDClassifier(penalty='l2')
# clf.fit(data_X_train, data_Y_train)
# y_pred = clf.predict(data_x_test)
# n_corret = sum(y_pred == data_y_test)
# print(n_corret)
# print(n_corret/len(data_y_test))