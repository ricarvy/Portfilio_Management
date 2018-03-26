# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 19:33
# @Author  : Li Jiawei
# @FileName: main.py
# @Software: PyCharm

from __future__ import division
from argparse import ArgumentParser

from model.modelGenerator import Model
from tools.config_loader import ConfigLoader

def parser_builder():
    parser=ArgumentParser()
    parser.add_argument("--mode",
                        dest="mode")
    parser.add_argument("--process",
                        dest="process")
    return parser

def main():
    parser=parser_builder()
    option=parser.parse_args()
    configLoader=ConfigLoader()
    config=configLoader.load_config()
    if option.process == 'generate_model':
        modelGeneration(config)

def modelGeneration(config):
    print('model is generating...')
    model=Model(config)
    model=model.generateModel()

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