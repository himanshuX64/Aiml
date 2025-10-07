import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#  using list
student_data=[
    [100,99,33],
    [90,56,36],
    [80,25,60]
]
st=pd.DataFrame(student_data,columns=['id','marks','age'])
print(st)

# using dictionary
std_data={
    "Place":["Mathura","Patna","Siwan"],
    "Package":[10,3,7],
    "Name":["Himu","Lalit","Veer"]
}
Dict_data=pd.DataFrame(std_data)
print(Dict_data)
# ipl data
ipl=pd.read_csv("C:\\Users\\91886\\Desktop\\Aiml\\Pandas\\Dataframe\\matches.csv")
print(ipl.info())
print(ipl.shape)
print(ipl.dtypes)
print(ipl.columns)
print(ipl.isnull().sum())
print(ipl.duplicated().sum())
print("_"*50)
# Movies data
movies_data=pd.read_csv("C:\\Users\\91886\\Desktop\\Aiml\\Pandas\\Dataframe\\movies.csv")
print(movies_data.head(10))
print(movies_data.shape)
print(movies_data.dtypes)
print(movies_data.columns)
print(movies_data.isnull().sum())
print("_"*50)
print(movies_data.duplicated().sum())

# rename column
print(Dict_data.rename(columns={'Package':'lpa'}))
# inplace : parmanent change
print(Dict_data.rename(columns={'Package':'lpa'},inplace=True))

# selecting column
print(movies_data['genres'])
# selecting multiple columns
print(movies_data[['release_date','runtime']])
print("_"*50)
# iloc to check index based
print(movies_data.iloc[1])
print("_"*50)
print(movies_data.iloc[:5])
print("_"*50)
# fancy fiter
print(movies_data.iloc[[1,5,10]])

# loc : row wise access
print("_"*50)
# from student data
print(st.loc[1])
# multiple rows
print(st.loc[[0,1]])

# SELECTING ROWS AND COLUMN IN INDEX (0,5)
print("_"*50)
print(movies_data.iloc[0:3,0:3])



