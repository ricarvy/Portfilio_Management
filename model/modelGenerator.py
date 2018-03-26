# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 20:36
# @Author  : Li Jiawei
# @FileName: modelGenerator.py
# @Software: PyCharm

import tensorflow as tf

from keras.layers import Dense, Activation, Conv2D
from keras.models import Sequential
from keras.regularizers import l1,l2

class Model:
    def __init__(self,config):
        self.__config = config
        self.__layers = config['layers']
        self.__input = config['input']

    def generateModel(self):
        model=Sequential()
        network=None
        nerwork_list=[]
        regularizer=None
        for layer_number, layer in enumerate(self.__layers):
            if layer['type'] == 'ConvLayer':
                if layer['regularizer']=="L2":
                    regularizer=l2(0.01)
                else:
                    regularizer=l1
                    print('stride:',layer['strides'])
                network=Conv2D(input_shape=(),
                               filters=int(layer['filter_number']),
                               kernel_size=self.allint(layer["filter_shape"]),
                               strides=self.allint(layer['strides']),
                               padding=layer['padding'],
                               activation=layer['activation_function'],
                               kernel_regularizer=regularizer)
            elif layer['type'] == 'EIIE_Dense':
                if layer['regularizer']=="L2":
                    regularizer=l2(0.01)
                else:
                    regularizer=l1
                width=self.__input['window_size']
                network=Conv2D(filters=int(layer['filter_number']),
                               kernel_size=[1,width],
                               strides=[1,1],
                               activation=layer['activation_function'],
                               kernel_regularizer=regularizer)
            elif layer['type'] == 'EIIE_Output_WithW':
                if layer['regularizer']=="L2":
                    regularizer=l2(0.01)
                else:
                    regularizer=l1
                width = self.__input['window_size']
                height = self.__input['coin_number']
                features = self.__input['feature_number']
            else:
                raise ValueError('The layer {} is not supproted'.format(layer['type']))
            nerwork_list.append(network)

        for net_number, network in enumerate(nerwork_list):
            model.add(network)
        return model



    def allint(self,l):
        return [int(i) for i in l]