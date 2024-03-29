
# I'm used to create a file which holds names of tables only and to call these names in the notebooks while reading data 
# so that only changing this module will be quite efficient in case of any change of data sets to be used. 
# Since I create this sample project in my local computer, I don't have access to Hive and I can't use tables from Hive in this sample project. 
#Because of that hive table names are commented out.


# PATH PREFIX FOR FOLDER WHICH HOLDS CSV FILES
DATA_DIR = "../data/"

# RAW DATA FROM HIVE
#TABLE_CUSTOMER = "domino.customer_list"
#TABLE_TRANSACTIONS = "domino.customer_transactios"

# RAW DATA FROM CSV
CSV_TRANSACTION = DATA_DIR + "transaction.csv"
CSV_CUST_INFO = DATA_DIR + "client.csv"
CSV_DISP_INFO = DATA_DIR + "disp.csv"
CSV_ACCOUNT_INFO = DATA_DIR + "account.csv"
CSV_LOAN = DATA_DIR + "loan.csv"


# INTERMEDIATE DATA FROM HIVE
#TABLE_CUSTOMER_GRID = "domino.customer_merged_w_grid"
#TABLE_CUSTOMER_TRNX = "domino.customer_merged_trnx"

# INTERMEDIATE DATA FROM CSV
CSV_CUSTOMIZED_TRNX = DATA_DIR + "customized_trnx_data.csv"
CSV_LABELLED_TRNX = DATA_DIR + "labelled_trnx_data.csv"
CSV_CUST_FEATS = DATA_DIR + "customer_list_w_feats.csv"


# FINAL MODEL DATA FROM HIVE
#TABLE_CHURN_MODEL = "domino.churn_model_data"

# FINAL MODEL DATA FROM CSV
CSV_CHURN_MODEL = DATA_DIR + "customer_list_w_feats.csv"





