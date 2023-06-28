#!/usr/bin/env python3
import os
import sys
import logging
import numpy as np
import time
import scipy.io
import glob
import pickle
from keras.utils.np_utils import to_categorical
from keras import backend as K
import tensorflow as tf
import keras
# import cv2
import full 

# set the value of data format convention
K.set_image_data_format('channels_last')  # TF dimension ordering in this code

## record feature matrix feature map
the_model='weights.h5' # get all models in the directory
os.system("mkdir prediction") 
all_test = glob.glob('test_gs/*')
FILE=open(all_test[0], 'r')
line=FILE.readline()
line=line.strip()
table=line.split('\t')
gs_len=len(table)-1


with open('../processeddata_sep/human_retina_2.pkl.17700', 'rb') as f:
    x = pickle.load(f)
    size = len(x.columns)

model = full.full1d(size,gs_len)
model.load_weights(the_model) ## load weight
for each_test in all_test:
    FILE=open(each_test,'r')
    ttt=each_test.split('/')
    with open('../processeddata_sep/' + ttt[-1], 'rb') as fhand:
        osb = pickle.load(fhand)
        image = osb.to_numpy()
        #    image=image.reshape((image.shape[0],image.shape[1],1))

    image_batch=image
    output = model.predict(image_batch)
    np.savetxt('prediction/' + ttt[-1], output, delimiter='\t')
