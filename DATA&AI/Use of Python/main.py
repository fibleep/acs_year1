import math

import numpy as np
import pandas as pd
from IPython.display import display

data = [[1, 15, 54, 36.5], [2, 18, 68, 37.1], [3, 11, 41, 36.4], [4, 17, 59, 37.2], [5, 20, 65, 36.9]]
dfA = pd.DataFrame(data, columns=['id', 'age', 'weight', 'temp'])
print(dfA)
# q2a
q2a = dfA.iloc[:, 1]
print(f"column {dfA.columns[1]} is of type {type(q2a)}")
# q2b
print("3rd row: ")
print(dfA.iloc[2])
# q2c
print(f"max age {max(dfA.loc[:, 'age'])} and min age {min(dfA.loc[:, 'age'])}")
# q2d
print(sum(dfA.loc[:, 'weight'] / len(dfA.loc[:, 'weight'])))
# q2e
print("weights divided")
for weight in dfA.loc[:, 'weight']:
    print(weight / 1000)
# q2f
print("temp to fahrenheit")
for temp in dfA.iloc[:, -1]:
    print((temp * 9 / 5) + 32)
# q3a

# dfA.to_csv('use_of_python.csv')

# q3b
newData = dfA
newData.at[0, 'age'] = 50
newData.to_csv('use_of_python.csv')

# q3b
testData = pd.read_csv('use_of_python.csv')
print(testData)
# q4a
print("delete id")
testData.drop(testData.columns[0], axis=1, inplace=True)  # delete unnamed
testData.drop(testData.columns[0], axis=1, inplace=True)  # delete id
print(testData)
# q4b
print("add new column")
newData = [160, 175, 162, 169, 179]
testData['lengths'] = newData
print(testData)
# q4c & q4d
BMI = []
for weight, length in zip(testData.loc[:, 'weight'], testData.loc[:, 'lengths']):
    BMI.append(weight / math.pow((length / 100), 2))
testData['BMI'] = BMI
# q4e
for index in testData.index[testData.loc[:, 'weight'] > 60].tolist():
    testData.at[index, 'weight'] = 0
print(testData)

# q4f
for index in testData.index[testData.loc[:, 'age'] >= 18].tolist():
    testData.at[index, 'age'] = 19
print(testData)
# q4g
print("temp for ppl over 16")
print((testData.loc[testData['age'] >= 16]).loc[:, 'temp'])

# q5a
sportData = pd.read_csv('sportData.csv', sep=';')
print(f"Length of sportData is {len(sportData)}")
# q5b
print(sportData['Sport'].unique())
# q5c
sportData = pd.read_csv('sportData.csv', sep=';', na_values='none')
print(sportData['Sport'].unique())
# q5d
print(sportData.iloc[0::].isna().any())
# q5e
print(sportData[sportData['Sport'].isna()])
# q5f
sportDataPerfected = sportData
sportDataPerfected.dropna(subset=['Sport', 'Hours per week'], inplace=True)
display(sportDataPerfected)
# q5g
print(f"max age is {max(sportDataPerfected['Age'])}")
# q5h
print(f"sum of all values > 1 is {sum(sportDataPerfected['Times per week'] > 1)}")

# q6a
lista = [10, 20, 30, 30, 30]


def replace(myList, to_look_for, replacement):

    """
    Replace values of a list
    :param myList: this is a list
    :param to_look_for: this is a number we want to replace
    :param replacement: this is a number we want to change to_look_for to

    :returns: a list with all to_look_for positions changed to replacement
    """

    myList = [(replacement if index == to_look_for else index) for index in myList]
    print(myList)


replace(lista, 30, 42)
lista_np = np.array(lista)
lista_pd = pd.Series(lista)
replace(lista_np, 30, 42)
replace(lista_pd, 30, 42)
