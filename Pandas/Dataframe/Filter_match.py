import pandas as pd
import numpy as np
from xlwings.pro.reports.filters import columns

ipl=pd.read_csv('matches.csv')
print(ipl.columns)
print(ipl.head(5))
newdf=ipl['season']=='Pune'
print(newdf)
ty=ipl[newdf]
print(ty[['winner','result']])

