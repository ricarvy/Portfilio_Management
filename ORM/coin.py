# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 19:55
# @Author  : Li Jiawei
# @FileName: coin.py
# @Software: PyCharm

import tensorflow as tf

from ORM.coin_basic import Coin_Basic

class Coin(Coin_Basic):

    def test(self):
        print(self.name)
