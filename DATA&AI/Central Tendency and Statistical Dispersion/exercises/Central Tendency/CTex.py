import pandas as pd
import math
broadband = pd.read_csv("broadband.csv", delimiter=',',decimal=',')
# q1b
broadband['round sync speed'] = round(broadband['avr sync speed'])
print(broadband['round sync speed'])
print('MODE: ',broadband['round sync speed'].mode())
print('MEAN: ',broadband['round sync speed'].mean())
print('MEDIAN: ',broadband['round sync speed'].median())
def get_outliers(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    I = Q3 - Q1
    low = Q1 - 1.5 * I
    high = Q3 + 1.5 * I
    return[data[~data.between(low,high)]]

def get_extreme_outliers(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    I = Q3 - Q1
    low = Q1 - 3 * I
    high = Q3 + 3 * I
    return[data[~data.between(low,high)]]
#print(broadband[broadband['round sync speed']!=get_outliers(broadband['round sync speed'])])
print(broadband.loc(broadband['round sync speed']!=get_outliers(broadband['round sync speed'])))
