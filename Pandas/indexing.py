#indexing
import numpy as np
import pandas as pd
data={
    "name": ["Rajesh Kumar", "Sunita Devi", "Himanshu Kumar", "Ankita Kumari"],
    "age": [50, 45, 20, 16],
    "place": ["Patna", "Patna","Mathura", "Patna"],
    "work": ["Teacher", "Homemaker", "Student", "School Student"]
}
num=np.arange(0,20).reshape(4,5)
df=pd.DataFrame(data)
print(df)

#by column name  only single column in series frame
print(df['name'])

# by multiple rows and column name  only access by double [[]] in Dataframe
print(df[["name","age","place"]])

# indexing iloc[] by position eg.(0,0),(1,1),(2,2)... with row and column
print(df.iloc[1:2,0:3])

# indexing  loc[] by selecting rows and column eg "name","age
df_num=pd.DataFrame(num)
print(df_num)
print(df_num.loc[[1,2]])

# Basic Operation
NUm=[[1,np.nan,2],[3,5,np.nan]]
pf=pd.DataFrame(NUm,index=["A","B"],columns=["X","Y","Z"])
print(pf)
print(pf.isnull().sum()) # show  total number is Nan
print(pf.isnull()) # show the Nan ia true And values Is false

print(pf['X'].unique())  # show unique value in row or column

print(pf>2)