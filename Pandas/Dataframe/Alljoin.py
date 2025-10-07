import pandas as pd

matric={
    'Id':[1,2,3,4,5,6,7,8,9,10],
    'Name':['ayush','sneha','nitika','sandhaya','madhu','simran','rajni','puja','nitu','ashish'],
    'Sub':['math','sst','hindi','java','python','c++','html','Php','nodejs','ruby'],
}
intermidiate={
    'Id':[0,1,2,3,4,5,6,7,8,9],
    'Name':['john','bob','david','nolan','rutherford','einstin','newton','oppenhimer','beerbiceps','virat'],
    'Marks':[85,90,87,54,98,54,53,95,66,82]
}
df_matric = pd.DataFrame(matric)

df_inter = pd.DataFrame(intermidiate)

# inner join
mf_merge=pd.merge(df_matric,df_inter,on='Id',how='inner')
print(mf_merge)
# left join
mf_merge=pd.merge(df_matric,df_inter,on='Id',how='left')
print(mf_merge)
# rigtht join
mf_merge=pd.merge(df_matric,df_inter,on='Id',how='right')
print(mf_merge)
# outer join
mf_merge=pd.merge(df_matric,df_inter,on='Id',how='outer')
print(mf_merge)

