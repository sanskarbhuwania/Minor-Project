# -*- coding: utf-8 -*-
"""DS_minor_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RvmUhg7DWI6XtnIxPzl_sRf710zEHqeC
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from skimage.transform import resize
from skimage.io import imread
target=[]
images=[]
flat_data=[]

dir='/content/drive/MyDrive/data'
categories=['airplane','drones','helicopter']
for i in categories:
  pos=categories.index(i)
  path=os.path.join(dir,i)
  for img in os.listdir(path):
    img_array=imread(os.path.join(path,img)) 
    img_resize=resize(img_array,(150,150,3)) # Nomalization happenes automatically
    flat_data.append(img_resize.flatten())
    images.append(img_resize)
    target.append(pos)
flat_data=np.array(flat_data)
target=np.array(target)
images=np.array(images)
df=pd.DataFrame(flat_data)
df['Target']=target

x=df.iloc[:,1:-1].values
y=df.iloc[:,67500:67501].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0,stratify=y)
y=y.flatten() 
y_train=y_train.flatten() 
y_test=y_test.flatten()

from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.svm import SVC
svc=SVC()
parameters={'kernel':['rbf','linear'],
            'C': [1,10,100]
}
cv=GridSearchCV(svc,parameters,cv=5)
cv.fit(x_train,y_train)
cv.best_params_

model=SVC(C=10, kernel='rbf')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)
print(y_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
accuracy_score(y_pred,y_test)

confusion_matrix(y_pred,y_test)

classification_report(y_pred,y_test)