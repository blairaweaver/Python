import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectFromModel
# used initially only for seeing blank values
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# I have tried several different things, but I seem to be stuck at sub 0.8. I hope that you take into consideration
# everything that I tried
# I had some weird thing where it would drop down to about 25%, which I did email you about, but
# you made no comment about
# I believe it might be an issue with my data/preprocessing or due to the fact that I am
# running python 3.8 on my system

def load_data(filename):
    # Load the data into a pandas dataframe
    return pd.read_csv(filename)

def define_features(dataframe, start, end, yfeature):
    # Splits the encoded data into the X and y
    # This only works for features that are adjacent
    features = dataframe.loc[:, start:end]
    X = features.values
    y = dataframe[yfeature].values
    return X, y

def split_data(X, y, test_size):
    # Splits the test data into train and test based on user define test size
    return train_test_split(X, y, test_size=test_size)

clf = SGDClassifier(loss='log', penalty='l2')

data = load_data('file.txt')
data_dummies = pd.get_dummies(data.drop("fnlwgt", axis=1))

# Using all the features in training and using get dummies
# From multiple runs, will vary widely in the accuracy
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
# data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
data_X_train, data_x_test, data_Y_train, data_y_test = split_data(X, y, 0.2)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
print("Baseline with all Features")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")


# Using only type of employment and education
X, y = define_features(data_dummies, 'type_employer_Federal-gov', 'education_Some-college', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = split_data(X, y, 0.2)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
print("Using Employment and Education")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# Using Occupation
X, y = define_features(data_dummies, 'occupation_Adm-clerical', 'occupation_Transport-moving', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = split_data(X, y, 0.2)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
print("Using Occupation")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# Using education and occupation
features = data_dummies[list(data_dummies.loc[:, 'education_10th':'education_Some-college'] + data_dummies.loc[:, 'occupation_Adm-clerical':'occupation_Transport-moving'])]
X = features.values
y = data_dummies['income_>50K'].values
data_X_train, data_x_test, data_Y_train, data_y_test = split_data(X, y, 0.2)
clf.fit(data_X_train, data_Y_train)
print("Using Education and Occupation")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# Using a recusive feature selection
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
select = RFE(RandomForestClassifier(n_estimators=40, random_state=42), n_features_to_select=60)
select.fit(data_X_train, data_Y_train)
X_train_rfe = select.transform(data_X_train)
x_test_rfe = select.transform(data_x_test)
clf.fit(X_train_rfe, data_Y_train)
y_pred = clf.predict(x_test_rfe)
print("Using RFE to pick features")
print("Training score: {:.3f}".format(clf.score(X_train_rfe, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(x_test_rfe, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# # Test using Model
select = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold="median")
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
select.fit(data_X_train, data_Y_train)
X_train_model = select.transform(data_X_train)
x_test_model= select.transform(data_x_test)
clf.fit(X_train_model, data_Y_train)
y_pred = clf.predict(x_test_model)
print("Using Model Selection to pick Features")
print("Training score: {:.3f}".format(clf.score(X_train_model, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(x_test_model, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# Practicing with Cross validation
print("Cross Validation score and then Prediction from Cross Validation")
print(cross_val_score(clf, data_X_train, data_Y_train, cv=3, scoring="accuracy"))
y_train_pred_cross = cross_val_predict(clf, data_X_train, data_Y_train, cv=3)
print(confusion_matrix(y_true=data_Y_train, y_pred=y_train_pred_cross))
print("----------------------------------------------")

# Tested other learning rate styles, but optimal seems the way to go

# Using the Inverse scaling learning rate
for i in [10, 1, 0.1, 0.01, 0.001, 0.0001]:
    X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
    data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
    clf = SGDClassifier(loss='log', penalty='l2', random_state=42, learning_rate='invscaling', eta0=i)
    clf.fit(data_X_train, data_Y_train)
    y_pred = clf.predict(data_x_test)
    n_corret = sum(y_pred == data_y_test)
    print("Accuracy of the model using invscaling and eta0 of {:0.4f} is".format(i))
    print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
    print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
    print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
    print("----------------------------------------------")

# Using the adaptive learning rate
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf = SGDClassifier(loss='log', penalty='l2', random_state=42, learning_rate='adaptive', eta0=0.01)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
print("Accuracy of the model using adaptive")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# Using the constant learning rate
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf = SGDClassifier(loss='log', penalty='l2', random_state=42, learning_rate='constant', eta0=0.01)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)
print("Accuracy of the model using constant")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
print("----------------------------------------------")

# Modify alpha, which is used in the learning rate calculation for optimal
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
accuracy =[]
rate = [1,0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001, 0.000005, 0.000001]
for i in rate:
    clf = SGDClassifier(loss='log', penalty='l2', learning_rate='optimal', random_state=42, alpha=i)
    clf.fit(data_X_train, data_Y_train)
    y_pred = clf.predict(data_x_test)
    accuracy.append(clf.score(data_X_train, data_Y_train))
    print("Accuracy of the model using optimal and alpha of {:0.6f} is".format(i))
    print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
    print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
    print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
    print("----------------------------------------------")

plt.scatter(rate, accuracy)
plt.xlabel("Alpha")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Alpha using the optimal learning rate")
plt.show()

plt.close()

accuracy =[]
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
regu = ['l2', 'l1', 'elasticnet']
for i in regu:
    clf = SGDClassifier(loss='log', penalty=i, learning_rate='optimal', random_state=42)
    clf.fit(data_X_train, data_Y_train)
    y_pred = clf.predict(data_x_test)
    accuracy.append(clf.score(data_X_train, data_Y_train))
    print("Accuracy of the model using optimal and", i)
    print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
    print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
    print(confusion_matrix(y_true=data_y_test, y_pred=y_pred))
    print("----------------------------------------------")

plt.scatter(regu, accuracy)
plt.xlabel("Regularization")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Regularization using the optimal learning rate")
plt.show()

plt.close()

# # X_columns = ['age','type_employer','fnlwgt','education',
# 'education_num','marital','occupation',
# 'relationship','race','sex','capital_gain','capital_loss','hr_per_week', 'country']
ct = ColumnTransformer(
    [("scaling", StandardScaler(), ['age', 'education_num','capital_gain','capital_loss','hr_per_week']),
     ("onehot", OneHotEncoder(sparse=False),
     ['type_employer', 'education',  'marital','occupation','relationship','race','sex',
      'country'])])



# using l2 with 0.005 alpha to create a decision boundary and using the RFE for features
clf = SGDClassifier(loss='log', penalty='l1', learning_rate='optimal', random_state=42, alpha=0.000005)
X, y = define_features(data_dummies, 'age', 'country_Yugoslavia', 'income_>50K')
data_X_train, data_x_test, data_Y_train, data_y_test = train_test_split(X, y, test_size=0.20)
clf.fit(data_X_train, data_Y_train)
y_pred = clf.predict(data_x_test)

print("Accuracy of the best parameters")
print("Training score: {:.3f}".format(clf.score(data_X_train, data_Y_train)))
print("Test score: {:.3f}".format(clf.score(data_x_test, data_y_test)))
print("----------------------------------------------")

data_features = data.drop(labels=["income", "fnlwgt"], axis=1)
X_train, X_Test, Y_train, Y_Test = train_test_split(data_features, data.income, test_size=0.2, random_state=42)
ct.fit(X_train)
X_train_tran = ct.transform(X_train)

X_Test_trans = ct.transform(X_Test)

clf.fit(X_train_tran, Y_train)
print("Accuracy of the best parameters with OneHot")
print("Training score: {:.3f}".format(clf.score(X_train_tran, Y_train)))
print("Test score: {:.3f}".format(clf.score(X_Test_trans, Y_Test)))



print("----------------------------------------------")
clf = SGDClassifier(loss='log', penalty='l1', learning_rate='adaptive', random_state=42, alpha=0.000001, eta0=0.01)
clf.fit(X_train_tran, Y_train)
print("Accuracy of Adaptive and OneHot")
print("Training score: {:.3f}".format(clf.score(X_train_tran, Y_train)))
print("Test score: {:.3f}".format(clf.score(X_Test_trans, Y_Test)))