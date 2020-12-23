
# I'm used to create a file which holds names of tables only and to call these names in the notebooks while reading data so that only changing this module will be quite efficient in case of any change of data to be used. Since I create this sample project in my local computer, I don't have access to Hive and I can't use tables from Hive in this sample project. Because of that hive table names are commented out.


# RAW DATA FROM HIVE
#TABLE_CUSTOMER = "domino.customer_list"
#TABLE_TRANSACTIONS = "domino.customer_transactios"

# INTERMEDIATE DATA FROM HIVE
#TABLE_CUSTOMER_GRID = "domino.customer_merged_w_grid"
#TABLE_CUSTOMER_TRNX = "domino.customer_merged_trnx"

# INTERMEDIATE DATA FROM CSV
CSV_TRANSACTION = "transaction.csv"
CSV_CUST_INFO = "client.csv"
CSV_DISP_INFO = "disp.csv"
CSV_ACCOUNT_INFO = "account.csv"
CSV_LOAN = "loan.csv"

# FINAL MODEL DATA FROM HIVE
#TABLE_CHURN_MODEL = "domino.churn_model_data"

# PATH PREFIX FOR FOLDER WHICH HOLDS CSV FILES
DATA_DIR = "../data/"


