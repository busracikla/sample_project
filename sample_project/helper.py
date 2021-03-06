import pandas as pd
import os 
import numpy as np

#import pyspark
#import pyspark.sql.functions as F
#from pyspark.sql import SparkSession, DataFrame

from sample_project import config


def get_spark_session(mode="yarn", executor_memory=8, driver_memory=32, max_result_size=8):
    '''
        Common script to create spark session in the notebook 
        
        Args:
            mode (string): Possible values are "yarn", "local[8]"
            executor_memory (integer) 
            driver_memory (integer)
            max_result_size (integer)
            
        Return:
            SparkSession
    '''
    
    return SparkSession.builder\
            .master(mode)\
            .enableHiveSupport()\
            .config("spark.app.name","churn")\
            .config("spark.driver.memory",f"{driver_memory}G")\
            .config("spark.executor.memory",f"{executor_memory}G")\
            .config("spark.driver.maxResultSize",f"{max_result_size}G")\
            .getOrCreate()


def write_to_hive(sdf, save_as):
    '''
        Common script to write data into hive
        
        Args:
           sdf (spark dataframe): Desired data to be written into Hive
           save_as (string): Name of the table to be written in Hive
            
    '''
    sdf.write.saveAsTable(save_as, format="parquet", mode="overwrite")
    


def write_to_csv(df, path):
    '''
        Common script to write data into csv
        
        Args:
           df (pandas dataframe): Desired data to be written into csv
           path (string): Name of the csv file to be written together with directory path in the beginning (Ex: ../data/csv_name.csv)
            
    '''
    return df.to_csv(path)


def read_from_csv(path):
    '''
        Common script to read data from csv
        
        Args:
           path (string): Name of the csv file to be read together with directory path in the beginning (Ex: ../data/csv_name.csv)
            
    '''
    return pd.read_csv(path, index_col=[0])



    