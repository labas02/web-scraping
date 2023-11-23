import pandas as pd 
import numpy as np 
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences",]]

predict = "G3"

X = np.array(data.drop([predict], axis=1))
Y = np.array(data[predict])

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(X_train,Y_train)
acc = linear.score(X_test,Y_test)
print(acc)

print("co: ", linear.coef_)
print("intercept: ", linear.intercept_)

predictions = linear.predict(X_test)

for X in range(len(predictions)):
   print(predictions[X], X_test[X],Y_test[X])