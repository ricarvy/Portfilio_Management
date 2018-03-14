# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 19:33
# @Author  : Li Jiawei
# @FileName: main.py
# @Software: PyCharm

from __future__ import division
from argparse import ArgumentParser
from ORM.coin import Coin

def parser_builder():
    parser=ArgumentParser()
    parser.add_argument("--test",
                        dest="mode",
                        default="test1")
    parser.add_argument("--process",
                        dest="mode")
    return parser

def main():
    parser=parser_builder()
    option=parser.parse_args()
    if option.mode == 'dataPreprocessing':
        dataPreprocessing()

def test():
    pass

'''
Download the data matrix from external resourses

The method 
'''

'''
Prepare the basic data frame from database(like data.db)

The database is prepared in the folder 'Portfolio_Management/database'
if the folder is empty, pls run the code : 
main.py --process=databaseloader
firstly

Using this method we can get trainable dataframe

'''
def dataPreprocessing(database,):
    print('dataPreprocessing')




if __name__ == "__main__":
    main()
    ### test()