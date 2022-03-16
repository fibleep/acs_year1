import pandas as pd
import math
#SLIDES
laptops = pd.read_csv('laptops.csv', delimiter=';', decimal=',')
cpuGen = ['Sandy Bridge','Ivy Bridge','Haswell','Broadwell','Skylake','Kabylake']
laptops['cpuGeneration']=laptops['cpuGeneration'].astype(pd.CategoricalDtype(categories=cpuGen,ordered=True))
print(laptops)
print("------------------------")
print(laptops.cpuGeneration.mode())
print("------------------------")
print(laptops.RAM.median())
print("------------------------")
#print(laptops.cpuGeneration.median())
print("------------------------")
def median_categorical(data):
    d = data.dropna()
    n = len(d)
    middle=round(n/2)
    return d.sort_values().reset_index(drop=True)[middle]
print(median_categorical(laptops.cpuGeneration))
print("------------------------")
print(laptops.diskspace.mean())
print("------------------------")
