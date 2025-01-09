import datetime

curr = datetime.datetime.now().time()
print(curr)
if 4 <= curr.hour < 12 : print("Good Morning")
elif 12 <= curr.hour < 17 : print("Good After Noon")
elif 17 <= curr.hour < 21 : print("Good Evening")
else : print("Good Night")