import pandas as pd

laptops = pd.read_csv('laptops.csv', delimiter=';', decimal=',')
cpuGen = ['Sandy Bridge','Ivy Bridge','Haswell','Broadwell','Skylake','Kabylake']
laptops['cpuGeneration']=laptops['cpuGeneration'].astype(pd.CategoricalDtype(categories=cpuGen,ordered=True))
print(laptops)