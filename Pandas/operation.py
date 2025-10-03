#Basic operation
import numpy as np
import pandas as pd

num=np.arange(0,50).reshape(5,10)
print(num)
df=pd.DataFrame(num,index=['A','B','C','D','E'],columns=['P','Q','R','S','T','U','V','W','X','Y'])

# Transpose chane row to column
print(df.transpose())

# sort by index
print(df.sort_index(axis=0,ascending=False))
