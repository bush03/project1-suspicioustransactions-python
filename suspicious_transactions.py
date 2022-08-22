import pandas as pd 
import os

def get_suspicious_transactions(file):
    df = pd.read_csv(file) 
    index_with_nan = [index for index, row in df.iterrows() if row.isnull().any()]
    improper_transactions=[]  
    missing_transactions_index=df[df['Transaction ID'].isnull()].index.tolist()
    for i in range(len(index_with_nan)):
        if index_with_nan[i] not in missing_transactions_index:
            improper_transactions.append(df['Transaction ID'].iloc[index_with_nan[i]])
    print("improper transactions includes transaction ids:",improper_transactions,'\n')
    print("index number of suspicious transactions with missing transaction ids:",missing_transactions_index,'\n')
    print("index number of all suspicious transactions:",index_with_nan,'\n')
    for i in range(len(index_with_nan)):
        nan_values = df.iloc[index_with_nan[i]].isna()
        label=nan_values[nan_values == True].index[0]
        print(label,'is missing from the index',index_with_nan[i])
        
path = os. getcwd()
get_suspicious_transactions('transactions.csv')   
