import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import time
 


store_data = pd.read_csv('groceries - groceries.csv', header=None)

 

store_data.head()

 

store_data

 

store_data.shape
records = []
for i in range(0,500):
    records.append([str(store_data.values[i,j]) for j in range(0, 32)])
    
start_time = time.time()
association_rules = apriori(records, min_support = 0.001, min_confidence = 0.3, min_lift = 3, min_length = 2)
association_results = list(association_rules)
print(len(association_results))
for i in association_results:
    print('\n')
    print(i)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
stop_time = time.time()
print(f"Training time: {stop_time - start_time}s")