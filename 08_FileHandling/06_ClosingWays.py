#Three ways to close a file

#normal way
f = open("01", mode="r")
print("01 file opened")
#operations
#file isn't closed in case of exception
f.close()

#exception handling
try:
    f = open("Hellooo", mode="r")
    print("Hellooo file opened")
    # operations
except FileNotFoundError :
    print("The file does not exist.")
finally:
    if 'f' in locals():
        f.close()

#with statement
with open("02_text", mode="r") as f :
    #operations
    print("02_text file opened")