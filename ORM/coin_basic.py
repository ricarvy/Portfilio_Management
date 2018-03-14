# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 19:57
# @Author  : Li Jiawei
# @FileName: coin_basic.py
# @Software: PyCharm

class Coin_Basic():
    def __init__(self, name, high, low, open, volume, quoteVolume, weightedAverage):
        self.name = name
        self.high = high
        self.low = low
        self.open = open
        self.volume = volume
        self.quoteVolume = quoteVolume
        self.weightedAverage = weightedAverage
