import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('Questionnaire 21-22.csv',delimiter=';',decimal='.')
print(data)
data.info()
# q1a
blood=data[data['Blood Type']=='Unknown']
print(len(blood)/len(data))
# q1b
license=data[data['Driver License']=='Yes']
print(100*(len(license)/len(data)))
# q2a
print(sum(data[data['Writing Hand']=='Left']['Mobile Devices'])/len(data[data['Writing Hand']=='Left']))
# q2b
print(sum(data[data['Writing Hand']=='Right']['Mobile Devices'])/len(data[data['Writing Hand']=='Right']))
# q3a
data['Shoe Size']=pd.to_numeric(data['Shoe Size'])
data['Size']=data['Length']/data['Shoe Size']
print(data['Size'])
# q3b
print(f"max : {data['Size'].max()}")
print(f"min : {data['Size'].min()}")
print(f"mean: {data['Size'].mean()}")
# q4
print(f" sum of siblings: {sum(data['Siblings'])}")
# q5
data.plot.scatter(x="Travel Distance",y="Travel Time",title="Distance to KDG")
plt.show()