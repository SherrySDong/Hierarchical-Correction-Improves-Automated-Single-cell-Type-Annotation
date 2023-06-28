
import keras
import tensorflow as tf
import numpy as np
from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, BatchNormalization, Dense, Flatten
from tensorflow.keras.optimizers import Adam
from keras.initializers import glorot_uniform
from keras.losses import binary_crossentropy
from keras import backend as K
from keras import losses


def self_crossentropy(y_true, y_pred):
    y_true = K.flatten(y_true)
    y_pred = tf.clip_by_value(K.flatten(y_pred), 1e-7, (1.0 - 1e-7))
    out = -(y_true * K.log(y_pred) + (1.0 - y_true) * K.log(1.0 - y_pred))
    return K.mean(out)

def mean_squared_error(y_true, y_pred):
    return K.mean(K.square(y_pred - y_true), axis=-1)

def clipped_mse(y_true, y_pred):
    return K.mean(K.square(K.clip(y_pred, 0., 1.0) - K.clip(y_true, 0., 1.0)), axis=-1)


def full1d(size,type_len):
    inputs = Input((size))  # 1024
    layer=Dense(256,activation='relu')(inputs)
    layer=Dense(128,activation='relu')(layer)
    layer=Dense(64,activation='relu')(layer)
    outputs = Dense(type_len, activation="sigmoid")(layer)
    
    model = Model(inputs=[inputs], outputs=[outputs])
    model.compile(optimizer=Adam(lr=3e-5, beta_1=0.9, beta_2=0.999, decay=0.0), loss=self_crossentropy, metrics=["accuracy"])
    return model


