import numpy as np 
import pandas as pd
dict={
    'first score':[100,45,70,np.nan],
    'second score':[np.nan,90,45,35],
    'third score':[60,50,np.nan,80]
}
data=pd.DataFrame(dict)
print(data)
print(data.isnull().tail(1))
print(data.notnull())
print(data.fillna(50))
print(data.ffill())
print(data.bfill())
print(data.dropna(axis=1))
print(data[0:2])