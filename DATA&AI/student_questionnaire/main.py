import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy import stats
data = pd.read_csv('Questionnaire 21-22.csv', delimiter=';', decimal='.')
print(data)
data.info()
# q1a
blood = data[data['Blood Type'] == 'Unknown']
print(len(blood) / len(data))
# q1b
license = data[data['Driver License'] == 'Yes']
print(100 * (len(license) / len(data)))
# q2a
print(sum(data[data['Writing Hand'] == 'Left']['Mobile Devices']) / len(data[data['Writing Hand'] == 'Left']))
# q2b
print(sum(data[data['Writing Hand'] == 'Right']['Mobile Devices']) / len(data[data['Writing Hand'] == 'Right']))
# q3a
data['Shoe Size'] = pd.to_numeric(data['Shoe Size'])
data['Size'] = data['Length'] / data['Shoe Size']
print(data['Size'])
# q3b
print(f"max : {data['Size'].max()}")
print(f"min : {data['Size'].min()}")
print(f"mean: {data['Size'].mean()}")
# q4
print(f" sum of siblings: {sum(data['Siblings'])}")
# q5
data.plot.scatter(x="Travel Distance", y="Travel Time", title="Distance to KDG")
plt.show()

# MEANS AND DEVIATIONS
# q1a
print("shoe size avg: ", data['Shoe Size'].mode())

# q1b
data['Shoe Size'].dropna().mean()
# q2
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
print(get_outliers(data['Shoe Size']))
print(get_extreme_outliers(data['Shoe Size']))

#q3
print((44-data['Shoe Size'].mean())/data['Shoe Size'].std())
print((175-data['Length'].mean())/data['Length'].std())

