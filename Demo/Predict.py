import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import cv2
import mahotas
import h5py
from skimage import feature
import imutils
import numpy as np 
import pandas as pd 
import os
from sklearn.model_selection import train_test_split
import mahotas
import datetime
import tarfile
import urllib.request
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

#-----------------------------------    

def fd_hu_moments(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature


# feature-descriptor-2: Haralick Texture
def fd_haralick(image):
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the haralick texture feature vector
    haralick = mahotas.features.haralick(gray).mean(axis=0)
    # return the result
    return haralick


# feature-descriptor-3: Color Histogram
def fd_histogram(image, mask=None):
    # convert the image to HSV color-space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # compute the color histogram
    hist  = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    # normalize the histogram
    cv2.normalize(hist, hist)
    # return the histogram
    return hist.flatten()

bins   = 8
def Prediction():
  
  label = ['Apple','Avocado','Banana','Coconut' ,'Custard','Dragon Fruit','Guava','Mango','Orange','Plum','Start Fruit','Watermelon']
  #img_path = input("Nhập đường dẫn file của ảnh: ")
  img_path = 'static/image/new_image'
  #img_path = 'Apple005.jpg'
  model = pickle.load(open("Model/Model_3d.pkl",'rb'))
  model_predict = model['RF']
  # Rút trích đặc trưng với 
  
  img = cv2.imread(img_path)
  cv2.imshow('Image',img)
  image = cv2.resize(img, (64,64))
  ####################################
  # Global Feature extraction
  ####################################
  fv_hu_moments = fd_hu_moments(image)
  fv_haralick   = fd_haralick(image)
  fv_histogram  = fd_histogram(image)

  ###################################
  # Concatenate global features
  ###################################
  global_feature = np.hstack([fv_histogram, fv_haralick, fv_hu_moments])

  #print(global_feature)
  # predict label of test image
  prediction = model_predict.predict([global_feature] )[0]
  #print(prediction)
  # show predicted label on image
  return prediction
#Prediction()

