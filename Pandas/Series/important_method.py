import random
import Work_wth_CSV
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
df=pd.Series(data)

#between : it used to filter series to fall specific range
print(df.between(2,4))

#clip : it used to limit the value a series to specified range
print(df.clip(5,10))

#  drop_duplicated : remove duplicated values
temp=pd.Series([1,2,1,2,3,4,3,4,5,4])
print(temp.duplicated())

# isnull : To check Missing Values Or NaN To  (True : Represent Missing values) And So on
temp1=pd.Series([1,np.nan,4,5,6,54,32,np.nan,54,np.nan])
print(temp1.isnull())

# dropna() : remove missing values and return new series
print(temp1.dropna())

# fillna() : Fill missing values in series
print(temp1.fillna(temp1.mean()))

# isin : to filter a series  only element
print(df.isin([21,25]))

# copy : Craete a copy of original data
new=df.head().copy()
print(new)

# Plot : Create Visual data
# Plot
show_plot=pd.read_csv("C:\\Users\\91886\\Desktop\\Aiml\\Pandas\\Series\\bollywood_dataset.csv")
print(show_plot)
print(show_plot["BoxOffice(Cr)"].value_counts().head(4).plot(kind='bar'))