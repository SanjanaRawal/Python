import pandas as pd
import numpy as np

#Creating series
s = pd.Series([123,"B",("C","M"),34.78,"E",[True , False , True]] , index=["a","b","c","d","e","f"])
print(s)

data = {"Months" : ["January" , "February" , "March" , "April"] }
a = pd.DataFrame(data)
print(a)
def extract(val) :
    return val[0:3]
a["Short"] = a["Months"].map(extract)
print(a)


#Creating dataframe
df = pd.DataFrame( { "Name" : ["Rohan" , "Rahul" , "Rohit"] ,
                     "LastName" : ["Sharma" , "Verma" , "Joshi"] ,
                     "Age" : [39 , 25 , 41] ,
                     "Salary" : [25000 , 19000 , np.nan]})
print(df)
print(df.isnull())
print(df["Salary"].mean())
df["Salary"] = df["Salary"].replace(np.nan , df["Salary"].mean())
print(df)
print(df["Salary"].mean()) #mean doesn't change
#Column  Transformation
df.loc[(df["Age"]>30) , "Experience"] = "Is Experienced"
df.loc[(df["Age"]<=30) , "Experience"] = "Is New to work"
print(df)
df["Id"] = df["Name"].str.lower() + "123" + df["LastName"].str.upper()
print(df)
df["Bonus"] = (df["Salary"]/100)*15
print(df)


#Creating dataframe from data stored in an excel file
df2 = pd.read_excel("06_exceldata.xlsx" , sheet_name="Sheet1")
print(df2)
print(df2.duplicated())
print(df2["StudentID"].duplicated())
print(df2["StudentID"].duplicated().sum())
print(df2.drop_duplicates()) #nothing changed , as over which column is not defined
print(df2.drop_duplicates("StudentID"))
print(df2.isnull())
print(df2.isnull().sum())
print(df2.dropna()) #deletes all null values
print(df2.replace(np.nan , "some value" )) #all nan values replaced
print(df2.bfill())
print(df2.ffill())
df2["Age"] = df2["Age"].replace(np.nan , 11)
df2["Class"] = df2["Class"].replace(np.nan , 5)
print(df2)
print(df2.isnull().sum())



#Importing csv data and creating a dataframe
df3 = pd.read_csv("06_csvdata.csv" , header=0)
print(df3)
print(df3.head(7)) #by default  5
print(df3.tail(7)) #by default 5
print()
print(df3.info())
print(df3.describe())
print(df3.isnull())
print(df3.isnull().sum())
print(df3)
print(df3.groupby("AIRLINE NAME").agg({"WAY OF PAYMENT" : "count"}))
print(df3.groupby(["AIRLINE NAME","WAY OF PAYMENT"]).agg({"WAY OF PAYMENT" : "count"}))
print(df3)
print(df3.groupby("WAY OF PAYMENT").agg({"FLIGHT BOOKING COST" : "mean"}))
print(df3.groupby(["WAY OF PAYMENT","AIRLINE NAME"]).agg({"FLIGHT BOOKING COST" : "mean"}))
print(df3.groupby(["AIRLINE NAME","WAY OF PAYMENT"]).agg({"FLIGHT BOOKING COST" : ["count","mean"]}))

data1 = {"EmpID" : ["E08" , "E02" , "E03" , "E04" , "E05" , "E06"] ,
         "Name" : ["Nick" , "Ronny" , "Noa" , "Enna" , "Christian" , "Andrew"] ,
         "Age" : [34 , 28 , 45 , 21 , 39 , 40] }
data2 = {"EmpID" : ["E01" , "E02" , "E09" , "E04" , "E05" , "E07"] ,
         "Salary" : [30000 , 25000 , 40000 , 35000 , 44000 , 29000 ]}
a1 = pd.DataFrame(data1)
a2 = pd.DataFrame(data2)
print(a1)
print(a2)
print(pd.merge(a1,a2,on="EmpID")) #gives all common ids merged
print(pd.merge(a1,a2,on="EmpID",how="left")) #merged all common ids + shows all ids of first mentioned df
print(pd.merge(a1,a2,on="EmpID",how="right")) #merged all common ids + shows all ids of second mentioned df
print(pd.concat([a1,a2])) #a1 continued with a2 , with all columns in a1 and a2 , elements repeat , hence used for different data sets containing same columns

b1 = pd.DataFrame({"Fruit" : ["apple" , "strawberry" , "mango" , "litchi" , "cherry"] ,
                   "Price" : [150 , 70 , 120 , 100 , 160] ,
                   "Quantity" : [4 , 7 , 5 , 2 , 10]})
print(b1)
b2 = b1.copy()
print(b2)
b2.loc[[0,1,4],"Price"]=[120,90,140]
b2.loc[[0,1,4],"Quantity"]=[8,4,15]
print(b2)
print(b1.compare(b2))
print(b1.compare(b2 , align_axis=0))
print(b1.compare(b2, keep_shape=True))
print(b1.compare(b2, keep_shape=False))

c1 = pd.DataFrame({"keys" : ["k1","k2","k1","k2"] ,
                   "name" : ["kanha","murli","shyam","krishna"] ,
                   "house" : ["blue","yellow","red","yellow"] ,
                   "grade" : [4,6,2,10]})
print(c1)
print(c1.pivot(index="keys" , columns="name" , values=["house","grade"]))

c2 = pd.DataFrame({"name" : ["kanha","murli","shyam","krishna"] ,
                   "house" : ["blue","yellow","red","yellow"] ,
                   "grade" : [4,6,2,10]})
print(pd.melt(c2 , id_vars=["name"] , value_vars=["house"]))
print(pd.melt(c2 , id_vars=["name"] , value_vars=["house"] , var_name="House" , value_name="HouseColor"))
print(pd.melt(c2 , id_vars=["name"] , value_vars=["house","grade"]))