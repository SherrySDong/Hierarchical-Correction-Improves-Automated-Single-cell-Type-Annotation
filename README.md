# Code for "Single-cell Type Annotation with Deep Learning in 265 normal cell types for humans"

We developed a deep learning-based single-cell type prediction tool that assigns the cell type to 265 different cell types for humans, based on data from approximately five million cells. This repository is the source training code of the project. It is implemented in Python 3.6 and Tensorflow 2.0.


<img width="473" alt="截屏2023-12-30 上午11 22 36" src="https://github.com/SherrySDong/Hierarchical-Correction-Improves-Automated-Single-cell-Type-Annotation/assets/115379295/2a3c3eec-3b8f-4d4f-85a1-032296a4a71d">

The code can be devided into three parts: Pre-processing; training; and evaluation

## Preprocessing:
### extract_chunked.py
Splits data into chunks of cells. The size of the chunk can be modified by changing the  chunk parameter. During this process, each h5d file is split into multiple files so that the deep learning framework only need to take in one chunk at a time to fit in the memory of the CPU. 

### extractall.py
Extract expression data without spliting into chunks. We prepared this file for testing of small dataset that can directly fit into the CPU. 


## Training
### separate.py
Create cross-validation dataset

### full.py
The full.py code is the network structure. 

The network contains 3 hidden layers. The first hidden layer had 256 neurons, the second hidden layer had 128 neurons and the third hidden layer had 64 neurons (Figure 1B). This architecture is designed to gradually reduce the dimension of the gene expression data. The input layer contains 19403 genes and the output includes 265 distinct values allowing predicting representing different cell types simultaneously in a single model.


### train_deep.py
Trains the model on the training split, saves the model.

### predict_deeplearning.py
Predicts each cell type in the test set.


## Evaluation
### evaluate.py
The model is evaluated using AUC for each cell type.

### evaluate_f1.py
The model is evaluated using F1 score, the harmonic mean of precision and recall. 

## Adapt to new dataset. 
### extract.py
Read in an example dataset in h5ad format and output the corresponding GEX_observation.txt and GEX_feature.txt files
Then modify the predict_deeplearning.py to take in the data the user is interested in.
