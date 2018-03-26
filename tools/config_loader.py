# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 20:28
# @Author  : Li Jiawei
# @FileName: config_loader.py
# @Software: PyCharm

import os
import json

rootPath=os.path.dirname(os.path.abspath(__file__)).replace('\\tools','\\net_config.json')
class ConfigLoader:
    def __init__(self):
        self.__config_path=rootPath

    def load_config(self):
        with open(self.__config_path) as config_file:
            config=json.load(config_file)
        self.fill_default(config)
        return config

    def fill_default(self,config):
        self.set_missing(config, "random_seed", 0)
        self.set_missing(config, "agent_type", "NNAgent")
        self.fill_layers_default(config["layers"])
        self.fill_input_default(config["input"])
        self.fill_train_config(config["training"])

    def fill_train_config(self,train_config):
        self.set_missing(train_config, "fast_train", True)
        self.set_missing(train_config, "decay_rate", 1.0)
        self.set_missing(train_config, "decay_steps", 50000)

    def fill_input_default(self,input_config):
        self.set_missing(input_config, "save_memory_mode", False)
        self.set_missing(input_config, "portion_reversed", False)
        self.set_missing(input_config, "market", "poloniex")
        self.set_missing(input_config, "norm_method", "absolute")
        self.set_missing(input_config, "is_permed", False)
        self.set_missing(input_config, "fake_ratio", 1)

    def fill_layers_default(self,layers):
        for layer in layers:
            if layer["type"] == "ConvLayer":
                self.set_missing(layer, "padding", "valid")
                self.set_missing(layer, "strides", [1, 1])
                self.set_missing(layer, "activation_function", "relu")
                self.set_missing(layer, "regularizer", None)
                self.set_missing(layer, "weight_decay", 0.0)
            elif layer["type"] == "EIIE_Dense":
                self.set_missing(layer, "activation_function", "relu")
                self.set_missing(layer, "regularizer", None)
                self.set_missing(layer, "weight_decay", 0.0)
            elif layer["type"] == "DenseLayer":
                self.set_missing(layer, "activation_function", "relu")
                self.set_missing(layer, "regularizer", None)
                self.set_missing(layer, "weight_decay", 0.0)
            elif layer["type"] == "EIIE_LSTM" or layer["type"] == "EIIE_RNN":
                self.set_missing(layer, "dropouts", None)
            elif layer["type"] == "EIIE_Output" or \
                            layer["type"] == "Output_WithW" or \
                            layer["type"] == "EIIE_Output_WithW":
                self.set_missing(layer, "regularizer", None)
                self.set_missing(layer, "weight_decay", 0.0)
            elif layer["type"] == "DropOut":
                pass
            else:
                raise ValueError("layer name {} not supported".format(layer["type"]))

    def set_missing(self,config, name, value):
        if name not in config:
            config[name] = value
