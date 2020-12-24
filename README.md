# Sample Project

As a part of my job application, I created this project so that I can demonstrate a sample from my coding. I have found some external datasets which can be used to check if my code works or not. The goal of my sample project is writing code which can be usable in detecting prospective churners with the churn definition which is "customers don't have any active account anymore are considered as churners".  <br>

## Installing 

nbdev package is used here to build a library from the notebooks which are located in the "notebooks" folder.Coherent classes and functions get packaged together which can be later called from main notebook (pipeline). This reduces the need for rerunning evert time when preparing the data and/or running the model. <br>

In order to contribute or use this project make sure to clone this repository and pip install it: <br>

    pip install -e .


## Executing

Make sure you have installed the package (pip command above). To run the full-end-to-end pipeline which includes all the pipeline steps derived from separate notebooks (see section Structure down below) you need to execute "index.ipynb" notebook. The steps include: <br>

    1. getting the data and labels 
    2. splitting data into train & test
    3. training & testing the model
    
    
## Structure

The structure of the "notebooks" directory: <br>

    * exploration folder: It contains some notebooks which are not included into pipeline but are used in exploration/analysis part.
    * 00_prepare_transaction_data.ipynb
    * 01_label_data.ipynb
    * 02_extract_features.ipynb
    * 03_train_test_split.ipynb
    * 04_classification_model.ipynb
    * index.ipynb
   
