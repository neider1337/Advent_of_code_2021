import pandas as pd
import csv
import requests
#df = pd.read_fwf('input.txt')
#df.to_csv('log2.csv',index=False)

with open('log2.csv') as csvfile:
    data = list(csv.reader(csvfile))


count = 0


for i in range(0, len(data)-1):
    if data[i]<data[i+1]:
        count +=1
    elif i == len(data) and data[i-1]<data[i]:
        count +=1


