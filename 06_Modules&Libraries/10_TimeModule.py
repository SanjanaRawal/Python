import time
s1 = time.process_time()
s2 = time.perf_counter()
print(time.time()) #tells how much time is spend since 1st january 1970 #changes each time when ran
print()
print(time.localtime())
print()
print(time.strftime("%Y/%m/%d %H:%M:%S" , time.localtime()))
print()
time.sleep(5) #Wait for 5 seconds
print("After 5 seconds : " , time.time())
print()
st = "2006/02/12 02:34:51"
print(st , type(st))
dt = time.strptime(st , "%Y/%m/%d %H:%M:%S") #str to struct_time conversion
print(dt , type(dt))
print()
e2 = time.perf_counter()
e1 = time.process_time()
print(f"Time elapse : {e2-s2} seconds")
print(f"CPU time : {e1-s1} seconds")