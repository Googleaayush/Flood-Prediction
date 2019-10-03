# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:07:38 2019

@author: Ayush Jain
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pickle

dataset=pd.read_csv("final.csv")
X=dataset.iloc[:,[0,1,3,4,5,6,8,9]].values
Y=dataset.iloc[:,10].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelen1=LabelEncoder()
labelen2=LabelEncoder()
labelen3=LabelEncoder()

X[:,1]=labelen1.fit_transform(X[:,1])
X[:,2]=labelen2.fit_transform(X[:,2])
X[:,3]=labelen3.fit_transform(X[:,3])
#X[:,4]=labelencoder_X.fit_transform(X[:,4])

"""
onehotencoder=OneHotEncoder(categorical_features=[1,2,3])
X=onehotencoder.fit_transform(X).toarray()
"""


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,Y, test_size=0.2,random_state=0)


from sklearn.ensemble import RandomForestClassifier
classifier= RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
classifier.fit(X_train, y_train)

#saving the model for future use
#filename = 'randomforestmodel.sav'
#pickle.dump(classifier, open(filename, 'wb'))


y_pred=classifier.predict(X_test)

print(classifier.score(X_test,y_test))



from sklearn import metrics
print("Accuracy for Random Forest : ",metrics.accuracy_score(y_test,y_pred)*100)

print(metrics.confusion_matrix(y_test,y_pred))
print(metrics.classification_report(y_test,y_pred))



l1=[23.5,'Jan','ANATAPUR','ANDHRA PRADESH',7,2,16,0.5]
l1[1]=labelen1.transform(l1[1])
l1[2]=labelen2.transform(l1[2])
l1[3]=labelen3.transform(l1[3])
l1=np.array(l1)
l1=np.reshape(l1,(1,l1.shape[0]))
output1=classifier.predict(l1)
print(output1[0])  
