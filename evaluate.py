import numpy as np
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
    print(each_prediction)
    try:
        pred = np.concatenate((pred, np.genfromtxt(each_prediction)), axis=0)
    except:
        pred= np.concatenate((pred, np.genfromtxt(each_prediction).reshape(1,len(np.genfromtxt(each_prediction)))), axis=0)

all_gs = glob.glob('train_gs/*')
each_gs=all_gs.pop(0)
train_gs =(np.genfromtxt(each_gs ))[:,1:]
for each_gs in all_gs:
    try:
        train_gs = np.concatenate((train_gs, np.genfromtxt(each_gs)[:,1:]), axis=0)
    except:
        train_gs = np.concatenate((train_gs, np.genfromtxt(each_gs)[1:].reshape(1,len(np.genfromtxt(each_gs)[1:]))), axis=0)


column = 0
AUC = open('performance', 'w')
TYPE = open('type.list', 'r')
for line in TYPE:
    line=line.strip()
    AUC.write(line)
    y_true = gs[:,column]
    y_predict = pred[:,column]
    y_train=train_gs[:,column]
   # try:
    if (np.sum(y_true)==0):
        auc='na'
    elif (np.sum(y_train)==0):
        auc='na'
    else:
        auc = roc_auc_score(y_true, y_predict)
  #  except:
    #    auc = 'na'
    AUC.write('\t')
    AUC.write(str(auc))
    AUC.write('\n')
    column = column + 1
