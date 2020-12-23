# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/03_train_test_split.ipynb (unless otherwise specified).

__all__ = ['Stratified_Split', 'check_class_balance']

# Cell
import os
import pandas as pd
from sample_project import config
from sample_project.helper import write_to_csv, read_from_csv
from fastcore.utils import store_attr
import numpy as np
from sklearn.model_selection import train_test_split
from IPython.display import display


# Cell
class Stratified_Split:
    '''
    This class is built to split model data into train and test set

    Args:
            model_data (Pandas DataFrame): The csv file name which has model dataset with "client_id", features and label which is "churn_or_not"
            test_size (float): Percentage of data to be used as test set
            seed (integer): number for randomization of initial point
            do_downsample (boolean): If it's wanted to do downsampling

        Return:
            train (pandas DataFrame): the train set which includes both features and label
            test (pandas DataFrame): the test set which includes both features and label

    '''
    def __init__(self, model_data = None, test_size=0.1, seed=42, do_downsample=False):

        store_attr()

        if model_data == None: model_data = config.CSV_CHURN_MODEL
        self.model_data = read_from_csv(model_data)


    def __call__(self):

        train, test = train_test_split(self.model_data, stratify = self.model_data["churn_or_not"], test_size=self.test_size, random_state=self.seed)

        if self.do_downsample:
            train = self._downsample(train)

        return train, test

    def _downsample(self,df):
        return pd.concat(model_data[model_data["churn_or_not"]==1],
                         model_data[model_data["churn_or_not"]==0].sample(len(model_data[model_data["churn_or_not"]==1])))


# Cell
def check_class_balance(df):
    grouped = df.groupby("churn_or_not").size().rename("count").to_frame()
    grouped["percentage"] = grouped["count"] / len(df)
    return grouped