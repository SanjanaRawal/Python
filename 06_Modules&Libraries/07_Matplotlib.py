from cProfile import label

import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
from matplotlib.patches import bbox_artist

data = pd.read_csv("06_csvdata.csv")
df = pd.DataFrame(data)

# x = ["Part1" ,"Part2" ,"Part3" ,"Part4" ,"Part5"]
# y = [52 , 96 , 24 , 35 , 73]
# color = ["black" , "red" , "green" , "cyan" , "magenta" , "lavender"]
# plt.bar(x,y , color = random.choice(color) , edgecolor = "black")
# plt.xlabel("Parts" , fontsize = 15)
# plt.ylabel("Frequency" , fontsize = 15)
# plt.title("Frequencies of different parts" , fontsize = 20)
# plt.show()



# print(df)
# grp = df.groupby("WAY OF PAYMENT")["FLIGHT BOOKING COST"].sum()
# print(grp)
# # plt.bar(df["WAY OF PAYMENT"] , df["FLIGHT BOOKING COST"])
# plt.bar(grp.index , grp.values) #More accurate
# plt.show()


# x = ["Part1" ,"Part2" ,"Part3" ,"Part4" ,"Part5"]
# y1 = [52 , 96 , 24 , 35 , 73]
# y2 = [76 , 23 , 45 , 35 , 42]
# plt.plot(x,y1 , marker = "o" , ls = ":" , color="r" , label = "freq1")
# plt.plot(x,y2 , marker = "x" , ls = "--" , color="g" , label = "freq2")
# plt.legend()
# plt.show()



# print(df)
# grp = df.groupby("AIRLINE NAME")["FLIGHT BOOKING COST"].sum()
# print(grp)
# plt.plot(grp.index , grp.values)
# plt.show()


# x = np.random.randint(1,10,50)
# y = np.random.randint(10,100,50)
# plt.scatter(x,y,marker="*",c=np.random.randint(10,100,50),cmap="hot",s=np.random.randint(10,100,50))
# plt.colorbar()
# plt.show()



# print(df.columns)
# plt.scatter(df["WAY OF PAYMENT"] , df["FLIGHT BOOKING COST"] , color="g")
# plt.show()


# com = ["Sony" , "Sansui" , "Penasonic" , "Samsung" , "LG" , "Xiomi"]
# sales = [120 , 90 , 50 , 200 , 150 , 100 ]
# clr = ["green" , "silver" , "purple" , "pink" , "blue" , "red"]
# plt.pie(sales)
# plt.pie(sales , labels = com , colors=clr , explode = [0,0,0.1,0,0,0.1] , shadow=True , autopct="%.1f" , startangle=45)
# plt.show()


# print(df)
# print(df.columns)
# types = df.groupby("WAY OF PAYMENT")["FLIGHT BOOKING COST"].sum()
# print(types)
# plt.pie(types , labels = types.index , autopct="%.0f")
# plt.show()


# l = [15,12,30,16,51,21,16,61,10,45,69,32,27]
# plt.box(l)
# plt.boxplot(l)
# plt.show()


# l = [1,24,4,6,8,3,12,14,20]
# l1 = [2,3,4,7,6,3,2,3,7]
# val = [l,l1]
# plt.boxplot(val)
# plt.show()


# print(df.columns)
# plt.boxplot(df["FLIGHT BOOKING COST"])
# plt.show()


# x = [ 30,40,68,27,47,57,88,59,47,44,57,44,44,33,66,23,66,5,2,5,50,17,78,44,77,34 ]
# plt.hist(x , bins=len(x) , edgecolor="black" , color="grey")
# plt.show()


# d = [30,40,78,88,45,72,85,20,0,50,70,20,30,40,80,30,20]
# plt.violinplot(d)
# plt.violinplot(d , showmedians=True)
# plt.show()


# print(df)
# plt.violinplot(df["FLIGHT BOOKING COST"])
# plt.show()



# x = [40,10,30,50,80,10,45,90,10,30,20,50,30,20]
# # plt.stem(x)
# plt.stem(x , linefmt="--" , markerfmt="D" , bottom=1 , orientation="horizontal")
# plt.show()


# print(df.columns)
# top = df.head(20)
# plt.stem(top["FLIGHT BOOKING COST"])
# plt.plot(top["FLIGHT BOOKING COST"])
# plt.show()



# x = [1,2,3,4,5,6,7]
# y1 = [15,10,34,23,40,20,45]
# y2 = [8,25,10,30,67,81,27]
# y3 = [22,62,30,10,39,21,50]
# # plt.stackplot(x,y1,y2)
# plt.stackplot(x,y1,y2,y3 , baseline="sym" , labels=["Y1","Y2","Y3"] , colors = ["black","gray","silver"])
# plt.legend()
# plt.show()


# x = ["d1","d2","d3","d4","d5","d6","d7"]
# y = [25,50,45,20,10,30,55]
# # plt.step(x,y)
# plt.step(x,y , where="post" , marker="o")
# plt.show()


# print(df)
# grp = df.groupby("SOURCE OF CITY")["FLIGHT BOOKING COST"].agg("sum")
# print(grp)
# plt.step(grp.index , grp.values , where="mid" , color="red" , marker="x")
# plt.show()


# x=[10,20,30,40,50]
# y1=[45,60,15,30,75]
# y2=[105,90,30,60,75]
# plt.figure(figsize=[4,4])
# plt.plot(x,y1 , label="day one")
# plt.plot(x,y2 , label ="day two")
# plt.legend(loc=3 , ncols=2 , bbox_to_anchor=[0.4,0.75])
# plt.show()


# x1 = [10,20,30,40,50]
# y1 = [67,23,45,12,90]
# plt.title("First")
# plt.plot(x1,y1)
# plt.subplot(1,2,1) #rows,columns,chart num
# plt.show()
# x2 = [50,60,70,80,90]
# y2 = [98,71,32,65,43]
# plt.title("Second")
# plt.plot(x2,y2)
# plt.subplot(1,2,2)
# plt.suptitle("Data")
# plt.show()


x =[1,2,3,4,5]
y=[10,34,20,40,25]
plt.plot(x,y)
plt.savefig("07_savegraph.png" , facecolor="yellow" , bbox_inches="tight" , pad_inches=1)
plt.show()





