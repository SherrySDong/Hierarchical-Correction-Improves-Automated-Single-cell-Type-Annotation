import numpy as np
import sklearn
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix
import glob
from sklearn.metrics import roc_auc_score
all_gs = glob.glob('test_gs/*')
each_gs=all_gs.pop(0)
gs =(np.genfromtxt(each_gs ))[:,1:]
each_prediction = each_gs
each_prediction=each_prediction.replace('test_gs', 'prediction')
pred = np.genfromtxt(each_prediction)
for each_gs in all_gs:
    try:
        gs = np.concatenate((gs, np.genfromtxt(each_gs )[:,1:]), axis=0)
    except:
        gs= np.concatenate((gs, np.genfromtxt(each_gs)[1:].reshape(1,len(np.genfromtxt(each_gs)[1:]))), axis=0)
    each_prediction = each_gs
    each_prediction=each_prediction.replace('test_gs', 'prediction')
    #print(each_prediction)
    try:
        pred = np.concatenate((pred, np.genfromtxt(each_prediction)), axis=0)
    except:
        pred= np.concatenate((pred, np.genfromtxt(each_prediction).reshape(1,len(np.genfromtxt(each_prediction)))), axis=0)
    #break

all_gs = glob.glob('train_gs/*')
each_gs=all_gs.pop(0)
train_gs =(np.genfromtxt(each_gs ))[:,1:]
for each_gs in all_gs:
    try:
        train_gs = np.concatenate((train_gs, np.genfromtxt(each_gs)[:,1:]), axis=0)
    except:
        train_gs = np.concatenate((train_gs, np.genfromtxt(each_gs)[1:].reshape(1,len(np.genfromtxt(each_gs)[1:]))), axis=0)
    #break

def findF1(y_true, y_score):
    precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y_true, y_score)
    try:
        f1_scores = 2*recall*precision/(recall+precision)
        return(np.max(f1_scores))
    except:
