import pandas as pd
import numpy as np

# The code uses the pd.read_csv() function to read a CSV file located at C:\\Users\\91886\\Desktop\\Aiml\\Pandas\\bollywood_dataset.csv.
data=pd.read_csv("C:\\Users\\91886\\Desktop\\Aiml\\Pandas\\Series\\bollywood_dataset.csv")
print(data.info())

# head and tail to show the data some upper part and lower part
print(data.head()) # upper
print("_"*50)
print(data.tail()) #lower

print("_"*50)
#Retrieves a random sample from the data Series
print(data.sample())

print("_"*50)

# Counts the number of occurrences of each lead actor in the  data.values_count
print(data.value_counts())

print("_"*50)
#Sort the BoxOfficer(Cr) Column in ascending order
print(data["BoxOffice(Cr)"].sort_values())

print("_"*50)
#Sort the BoxOfficer(Cr) Column in descending order
print(data["BoxOffice(Cr)"].sort_values(ascending=False))

print("_"*50)
#Sort thr Movie  Row in Ascending order
print(data["Movie"].sort_index())

#Sort thr Movie  Row in descending order
print(data["Movie"].sort_index(ascending=False))

#                      SERIES WITH MATH METHOD
print("_"*50)
#  Counts the number of non-null elements in thw Column
print(data["BoxOffice(Cr)"].count())

# mean(): Calculates the mean (average) value of the BoxOffice Series
print("_"*50)
print(data["BoxOffice(Cr)"].mean())

# median(): Calculates the median (middle) value of the BoxOffice Series
print("_"*50)
print(data["BoxOffice(Cr)"].median())

# mode(): Calculates the mode (most frequent value) of the BoxOffice Series
print("_"*50)
print(data["BoxOffice(Cr)"].mode())

# Sum() : Sum of total Boxoffice in series
print("_"*50)
print(data["BoxOffice(Cr)"].sum())