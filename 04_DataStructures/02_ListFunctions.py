from os import remove

lst = [123 , "abc" , 34.5 , True , 876 , "xyz" , False , 0 , True]
#To get size of list
print("List size = " , len(lst))
#To count occurrence of an element
print("Occurrence of True : " , lst.count(True))
#Add something to list
lst.append([1,2,3])
print("New list : \n" , lst)
#Add at specific location
lst.insert(2 , (99,55))
print("New list : \n" , lst)
#To remove from list
lst.remove(True)
print("New list : \n" , lst)
#To remove from certain location
lst.pop(2)
print("New list : \n" , lst)
#To create copy of list
lst2 = lst.copy()
print("Other list : " , lst2)
#To access elements
print("Index of abc is " , lst.index("abc") )
#To extend one list to other
lst3 = [3 , 4 , 5]
lst.extend(lst3)
print("Extended list : " , lst)
#To reverse list
print("Reversed list : " , lst.reverse())
#To sort list
a = [5,8,7 , 0 , -8]
print("Unsorted list : " , a)
a.sort()
print("Sorted list : " ,a)
a.sort(reverse=True)
print("Descending order : " , a)
