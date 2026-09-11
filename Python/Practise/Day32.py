import pandas as pd
s=pd.Series([90,89,78,45],index=["raj","allen","smith","kevin"])
print(s)
print(s['allen'])
#2d-DataFrame
data={
    "name":['raju','harish','ramya'],
    "age":[23,21,25],
    "marks":[89,56,78]
}
df=pd.DataFrame(data)
print(df)
print(df['name'])
print(df[['name','marks']])
print(df.loc[0])    #to access particular row we use loc
print(df.iloc[0,0])   #position-based & column 
print(df.head(1))  #gives top elements
#ADD NEW COLUMN
df['grade']=['A','B','A++']
print(df)
#ADD NEW ROW
new_row={'name':'David','age':18,'marks':89,'grade':'A'}
df.loc[3]=new_row
print(df.describe())
print(df[df['marks']>85])