# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/02_extract_features.ipynb (unless otherwise specified).

__all__ = ['extract_features']

# Cell
import os
import pandas as pd
from sample_project import config
from sample_project.helper import write_to_csv, read_from_csv
from fastcore.utils import store_attr
import numpy as np

# Cell
def extract_features(df, to_csv=True, with_label=True):
    '''
    This function is built to extract two types of features which are:
    1. Total transaction amount within each date bin
    2. Total transaction count within each date bin

    Args:
        df (Pandas DataFrame): The transaction dataset which has at least these fields: "account_id","date","client_id"
        to_csv (boolean): If the returned dataframe is desired to be written into csv file
        with_label (boolean): If label is also asked to be in the data

    Return:
        feats (pandas DataFrame): the customer list together with extracted features
    '''

    df["date_bin"] = pd.cut(df.date, 10, labels=np.arange(0,10))

    feats = df.groupby(["client_id","date_bin"]).agg({'amount':['sum','count']})
    feats.columns = ["sum","count"]
    feats.reset_index(inplace=True)

    feats = feats.pivot( index="client_id",columns='date_bin', values=["sum","count"])
    feats = feats.fillna(0).reset_index()
    feats.columns=["client_id"]+["{}_bin_{}".format(j,i) for i in np.arange(0,10) for j in ["sum","count"]]

    if with_label: feats = feats.merge(df[["client_id","churn_or_not"]].drop_duplicates(),on="client_id",how="left")
    if to_csv: write_to_csv(feats, config.CSV_CUST_FEATS)

    return feats