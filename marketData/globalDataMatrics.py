# -*- coding: utf-8 -*-
# __time__ = '2018/3/27 21:15'
# __author__ = 'ClayZhang'

import os
import sqlite3
import logging

'''
This is a definition of rootPath

The operation convert the absPath from current file path to the path of data.db
The rootPath will show the abs path of data.db
'''
rootPath=os.path.dirname(os.path.abspath(__file__)).replace('\\marketData','\\database\\Data.db')

'''
This is a definition of csv storage folder path

If you want to save the specific data panel to .csv file
plz store in the csvPath
'''
cvsPath=os.path.dirname(os.path.abspath(__file__)).replace('\\marketData','\\temp_csv\\')

'''
This is a class to handle the .db file
'''
class GlobalDataMatrics:
    '''

    '''
    def __init__(self, config, start, end):
        ### dtype:dict
        ### a dict that present the net_config.json information
        self.__config = config

        ### dtype:str
        ### start date/time of the global data matrics
        ### format like: 'yyyy/mm/dd'
        self.__start = start

        ### dtype:str
        ### end date/time of the glocal data matrics
        ### format like: 'yyyy/mm/dd'
        self.__end = end

        ### dtype:Cursor (Database operation cursor)
        ### the cursor that handle the data in database
        self.__cursor=self.initialize_db()

    '''
    Database initialization
    Param:
        database_path:
            dtype:str
            script: .db file's abs path
    Return:
        cursor:
            dtype: sqlite3.Cursor
            script: database operation cursor
    '''
    def initialize_db(self, database_path=rootPath):
        cursor=None
        ### fill the blank
        return cursor

    '''
    get the global data matrics with index [start, end]
    Param:
        start: 
            dtype: str
            script:
        end :
            dtype: str
            script:
    Return:
        panel
            dtype:pandas.DataFrame
            script: 
    '''
    def get_global_panel(self,
                         start,
                         end):
        cursor=self.__cursor
        panel=None
        ### fill the blank
        return panel

    '''
    Save the data panel into .csv file in the file '/temp_csv/'
    Param:
        start: 
            dtype: str
            script:
        end :
            dtype: str
            script:
        filename:
            dtype: str
            script: plz follow the format like 'DP_start_end.csv'
        path:
            dtype: str
            script: the restore path , default '/temp_csv'
    '''
    def save_as_csv(self,
                    start,
                    end,
                    filename,
                    path=cvsPath):
        ### fill the blank
        logging.warn('Your data panel from %s to %s has been store as %s '.format(start,end,cvsPath+filename))
        pass
