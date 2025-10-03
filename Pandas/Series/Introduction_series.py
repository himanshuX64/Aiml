import pandas as pd
marks=[65,45,98,63]
sub=['hindi','sanskrit','urdu','math']
result=pd.Series(marks,index=sub)
print(result)

# Size attribute and output return number of element
print(result.size)

# dtype attribute and return data type of element
print(result.dtype)

# is_unique  to check all element are unique then duplicate show then output false
print(result.is_unique)
num=pd.Series(data=[1,1,2,5,6,7],index=['A','B','C','D','E','F'])
print(num.is_unique)

# Index attributes return the index labels
print(result.index)

# Values attributes return the actual data element in series
print(result.values)
