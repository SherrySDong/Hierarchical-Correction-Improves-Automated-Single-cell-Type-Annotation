import numpy as np
import random 
import sys
import keras
import os
import glob
import pandas as pd
import full


## map all cells to binarized cell type

## record which typ it is...
gs={} # gold standard to train
all_files = glob.glob('train_gs/*')

type_len = len(np.genfromtxt(all_files[0])[0,1:])
print(type_len)


import pickle
with open('../processeddata_sep/human_retina_2.pkl.17700', 'rb') as f:
    x = pickle.load(f)
    size = len(x.columns)

train_set=[]
validation_set=[]
for the_example in all_files:
    aaa = the_example.split('/')

    rrr=random.random()
    if (rrr<0.8):
        train_set.append(aaa[-1])
    else:
        validation_set.append(aaa[-1])

batch_size=1

### feed data into the model
def generate_data(train_set, batch_size, if_train):
    i = 0
    while True:
        image_batch = []
        label_batch = []
        for b in range(batch_size):
            if i == len(train_set):
                i = 0
                random.shuffle(train_set) ## shuffle after epoch
            with open('../processeddata_sep/' + train_set[i], 'rb') as fhand:
                osb = pickle.load(fhand)
                image = osb.to_numpy()
            #    image=image.reshape((image.shape[0],image.shape[1],1))

            image_batch=image
            try:
                label=np.genfromtxt('train_gs/' + train_set[i])[:,1:]
                label_batch=label
            except:
                label=np.genfromtxt('train_gs/' + train_set[i])[1:]
                label_batch=label
                label_batch=np.asarray(label_batch).reshape((1,len(label)))
            
                
            i += 1
        yield (image_batch, label_batch)



model = full.full1d(size,type_len) ## output length should be dynamically determined. 
name_model='weights.h5' ### save the parameters
callbacks = [
    keras.callbacks.ModelCheckpoint(os.path.join('./', name_model),
    verbose=0, save_weights_only=False,save_best_only=True,monitor='val_loss')
    ]

model.fit_generator(
    generate_data(train_set, batch_size,True),
    steps_per_epoch=int(len(train_set) // batch_size), epochs=20,
    validation_data=generate_data(validation_set,batch_size,False),
    validation_steps=int(len(validation_set) // batch_size),callbacks=callbacks)


