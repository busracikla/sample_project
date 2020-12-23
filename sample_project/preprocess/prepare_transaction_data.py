# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/00_prepare_transaction_data.ipynb (unless otherwise specified).

__all__ = ['Create_Data']

# Cell
import os
import pandas as pd
from sample_project import config
from fastcore.utils import store_attr
import numpy as np

# Cell
class Create_Data:
    '''
    This class is built to create main dataset to be used in this project. Following steps below, the transaction dataset for clients in the scope is created:
    1. Merging three different datasets: transaction, customer info and disp info which shows customer and account matches
    2. Applying three different filters below to cover only customers in the scope:
        - Consider only transactions whose date in between <start date> and <end date>
        - Consider only customers who have loans with more than <loan_amnt_thrsh> euros
        - Consider only customers from districts which have more than <district_cnt_thrsh> customers
    '''
    def __init__(self,trnx_dataset=None, disp_dataset=None, client_dataset=None, loan_dataset=None, loan_amnt_thrsh=1000, district_cnt_thrsh = 100, start_date=900000, end_date=1000000):

        '''
        Args:
            trnx_dataset (Pandas DataFrame): The transaction dataset which has at least these fields: "account_id","date"
            disp_dataset (Pandas DataFrame): The disp dataset which has at least these fields: "client_id","account_id"
            client_dataset (Pandas DataFrame): The customer info dataset which has at least these fields: "client_id","district_id"
            loan_dataset (Pandas DataFrame): The loan dataset which has at least these fields: "client_id","amount"
            loan_amnt_thrsh (integer): Loan amount threshold to be use to apply filter 2
            district_cnt_thrsh (integer): District count threshold to be used to apply filter 3
            start_date (integer): Start date threshold for transaction dataset to apply filter 1
            end_date (integer): End date threshold for transaction dataset to apply filter 1

        Return:
            main_data (pandas DataFrame): the transaction dataset for clients in the scope
        '''

        store_attr()

        if trnx_dataset == None:
            self.trnx_dataset = pd.read_csv(config.DATA_DIR + config.CSV_TRANSACTION, index_col=[0])

        if disp_dataset == None:
            self.disp_dataset = pd.read_csv(config.DATA_DIR + config.CSV_DISP_INFO, index_col=[0])

        if client_dataset == None:
            self.client_dataset = pd.read_csv(config.DATA_DIR + config.CSV_CUST_INFO, index_col=[0])

        if loan_dataset == None:
            self.loan_dataset = pd.read_csv(config.DATA_DIR + config.CSV_LOAN, index_col=[0])


    def __call__(self):

        main_data = self._applying_date_filter(self._merge_main_datasets())
        main_data = self._applying_loan_amount_filter(main_data)
        main_data = self._applying_district_filter(main_data)

        return main_data

    def _merge_main_datasets(self):

        return  (self.trnx_dataset.drop(["k_symbol","bank","account"],axis=1)
                 .merge(self.disp_dataset[["client_id","account_id"]], on="account_id",how="left")
                 .merge(self.client_dataset[["client_id","district_id"]],on="client_id",how="left")
                )

    def _applying_date_filter(self,df):

        return df[(df["date"] >= self.start_date)&(df["date"] <= self.end_date)]

    def _applying_loan_amount_filter(self,df):

        df = df.merge(
                        (self.loan_dataset
                             .merge(self.disp_dataset[["client_id","account_id"]],on="account_id",how="left")
                             .groupby("client_id",as_index=False).amount.sum().rename(columns={'amount':'Total_Loan_Amount'})
                         ), on ="client_id", how="left"
                      )
        df["Total_Loan_Amount"] = df["Total_Loan_Amount"].fillna(0)

        return df[df["Total_Loan_Amount"] > self.loan_amnt_thrsh]

    def _applying_district_filter(self,df):

        district_count = self.client_dataset.groupby("district_id",as_index=False).client_id.count().rename(columns={'client_id':'Num_Cust_in_District'})
        district_list = district_count[district_count["Num_Cust_in_District"]>self.district_cnt_thrsh]["district_id"].tolist()

        return df[df["district_id"].isin(district_list)]