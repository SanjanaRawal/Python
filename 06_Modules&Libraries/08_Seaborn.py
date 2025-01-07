import random

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("06_csvdata.csv")
data = sb.load_dataset("tips")
data1 = sb.load_dataset("titanic")

# k1 = "X"
# k2 = "Y"
# l1 = [1,2,3,4,5]
# l2 = [65,45,85,55,75]
# data = {k1 : l1 , k2 : l2}
# df = pd.DataFrame(data)
# print(df)
# sb.lineplot(data=data , x="X" , y="Y")
# plt.show()

# print(df)
# sb.lineplot(data=df , x="AIRLINE NAME" , y="FLIGHT BOOKING COST" , hue="WAY OF PAYMENT" , style="WAY OF PAYMENT" , palette=sb.color_palette("pastel6"))
# plt.show()



# print(data)
# # sb.barplot(data=data , x="day" , y="tip")
# sb.barplot(data=data , x="day" , y="tip" , estimator="median" , hue="smoker" , palette="pink" , order=["Sun","Sat","Fri","Thur"] , errorbar=("ci",0))
# plt.show()



# print(data)
# sb.histplot(data=data , x="day" , hue="sex" , kde=True , bins=5)
# plt.show()

# print(data1)
# sb.histplot(data=data1 , x="age" , hue="alive" , kde=True , palette="cool" , discrete=True )
# plt.show()



# print(data.columns)
# sb.scatterplot(data=data , x="total_bill" , y="tip" , hue="day" , size="size" , marker="o")
# plt.show()

# print(df)
# sb.scatterplot(data=df , x="WAY OF PAYMENT" , y="FLIGHT BOOKING COST" , hue="SOURCE OF CITY")
# plt.show()


# print(data.columns)
# grp = data.groupby("day").agg({"tip" : "mean"})
# sb.heatmap(grp)
# plt.show()

# print(df.columns)
# grp = df.groupby("DESTINATION OF FLIGHT").agg({"FLIGHT BOOKING COST" : "sum"})
# sb.heatmap(grp)
# plt.show()



# print(data)
# sb.countplot(data=data , x="day")
# plt.show()

# print(df)
# sb.countplot(data=df , x="SOURCE OF CITY" , color="hotpink" , hue="WAY OF PAYMENT")
# plt.show()



# sb.violinplot(data=data , x="total_bill")
# plt.show()

# sb.violinplot(data=df , x="FLIGHT BOOKING COST")
# plt.show()



# # sb.pairplot(data)
# sb.pairplot(data , hue="day" , diag_kind="kde") #for 3 columns having numerical data
# plt.show()

# print(data1.columns)
# sb.pairplot(data1 , hue="sex") #had 8 columns with numeric data hence 8x8 plots made
# plt.show()



# sb.stripplot(data=data , x="day" , y="total_bill" , hue="sex" , dodge=True , jitter=0.3)
# plt.show()



# # sb.boxplot(data=data , x="tip")
# sb.boxplot(data=data , x="sex" , y="tip" , orient="vertical")
# plt.show() #gives outliers



# sb.catplot(data=data , x="day" , y="tip" , hue="sex" , kind="violin")
# plt.show()



# d = sb.load_dataset("exercise")
# sb.set_style(style="whitegrid")
# sb.set_style(style="ticks")
# sb.barplot(data=d , x="time" , y="pulse")
# plt.show()


# sb.palplot(sb.color_palette())
# plt.show()

# sb.palplot(sb.color_palette("pink"))
# plt.show()

# sb.palplot(sb.color_palette("hot"))
# plt.show()

# sb.palplot(sb.color_palette("cool"))
# plt.show()

# sb.palplot(sb.color_palette("spring" , 4))
# plt.show()

# sb.palplot(sb.color_palette("viridis"))
# plt.show()



# print(data)
# a = sb.FacetGrid(data=data , col="time" , height=3 , hue="sex")
# a.map(sb.barplot , "day" , "tip")
# plt.show()



# sb.relplot(data=data , x="tip" , y="total_bill" , hue="smoker" , kind="scatter" , col="day")
# plt.show()



# sb.swarmplot(data=data , x="day" , y="total_bill" , hue="smoker" , dodge=True) #data doesn't overlap by default
# plt.show()



print(data)
# sb.kdeplot(data=data , x="total_bill")
sb.kdeplot(data=data , x="total_bill" , hue="day" , multiple="stack")
plt.show()
