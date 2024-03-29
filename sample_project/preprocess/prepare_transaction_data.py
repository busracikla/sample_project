# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/00_prepare_transaction_data.ipynb (unless otherwise specified).

__all__ = ['Transactional_Data']

# Cell
import os
import pandas as pd
from sample_project import config
from sample_project.helper import write_to_csv, read_from_csv
from fastcore.utils import store_attr
import numpy as np

# Cell
class Transactional_Data:
    '''
    This class is built to create main dataset to be used in this project. Following steps below, the transaction dataset for
    clients in the scope is created:
    1. Merging three different datasets: "transaction","customer info" and "disp info" which shows customer and account matches
    2. Applying three different filters below to cover only customers in the scope:
        - Consider only transactions whose date in between <start date> and <end date>
        - Consider only customers who have loans with more than <loan_amnt_thrsh> euros
        - Consider only customers from districts where there are more than <district_cnt_thrsh> customers

    Args:
            trnx_dataset (Pandas DataFrame): The csv file path which has transaction dataset with at least these fields: "account_id","date"
            disp_dataset (Pandas DataFrame): The csv file path which disp dataset with at least these fields: "client_id","account_id"
            client_dataset (Pandas DataFrame): The csv file path which customer info dataset with at least these fields: "client_id","district_id"
            loan_dataset (Pandas DataFrame): The csv file path which loan dataset with at least these fields: "client_id","amount"
            loan_amnt_thrsh (integer): Loan amount threshold to be use to apply filter 2
            district_cnt_thrsh (integer): District count threshold to be used to apply filter 3
            start_date (integer): Start date threshold for transaction dataset to apply filter 1
            end_date (integer): End date threshold for transaction dataset to apply filter 1
            to_csv (boolean): If the returned dataframe is desired to be written into csv file

    Return:
            main_data (pandas DataFrame): the transaction dataset for clients in the scope
    '''

    def __init__(self,trnx_dataset=config.CSV_TRANSACTION,
                 disp_dataset= config.CSV_DISP_INFO,
                 client_dataset=config.CSV_CUST_INFO,
                 loan_dataset=config.CSV_LOAN,
                 loan_amnt_thrsh=1000,
                 district_cnt_thrsh = 110,
                 start_date=900000,
                 end_date=970000):

        store_attr()


    def create_data(self, apply_filters = True, to_csv=True):

        df_trnx = read_from_csv(self.trnx_dataset)
        self.df_disp = read_from_csv(self.disp_dataset)
        self.df_client = read_from_csv(self.client_dataset)
        self.df_loan = read_from_csv(self.loan_dataset)

        merged_data = (df_trnx.drop(["k_symbol","bank","account"],axis=1)
                              .merge(self.df_disp[["client_id","account_id"]], on="account_id",how="left")
                              .merge(self.df_client[["client_id","district_id"]],on="client_id",how="left")
                             )

        if apply_filters:
            merged_data = self.applying_date_filter(merged_data)
            merged_data = self.applying_loan_amount_filter(merged_data)
            merged_data = self.applying_district_filter(merged_data)

        if to_csv:
            write_to_csv(df= merged_data, path = config.CSV_CUSTOMIZED_TRNX )

        return merged_data

    def applying_date_filter(self,df):

        return df[(df["date"] >= self.start_date)&(df["date"] <= self.end_date)]

    def applying_loan_amount_filter(self,df):

        df = df.merge(
                        (self.df_loan
                             .merge(self.df_disp[["client_id","account_id"]],on="account_id",how="left")
                             .groupby("client_id",as_index=False).amount.sum().rename(columns={'amount':'Total_Loan_Amount'})
                         ), on ="client_id", how="left"
                      )
        df["Total_Loan_Amount"] = df["Total_Loan_Amount"].fillna(0)

        return df[df["Total_Loan_Amount"] > self.loan_amnt_thrsh]

    def applying_district_filter(self,df):

        district_count = self.df_client.groupby("district_id",as_index=False).client_id.count().rename(columns={'client_id':'Num_Cust_in_District'})
        district_list = district_count[district_count["Num_Cust_in_District"]>self.district_cnt_thrsh]["district_id"].tolist()

        return df[df["district_id"].isin(district_list)]
