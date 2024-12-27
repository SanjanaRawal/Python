flowers = ["Lily" , "Marigold" , "Rose" , "Sunflower" , "Jasmine" , "Tulip" , "Lotus"]
print(flowers)

#Delete value at 4th index
flowers.pop(4)
print(flowers)

#Add Lavender at 5th index
flowers.insert(5 , "Lavender")
print(flowers)

#Swap 1st and last index
flowers[0] , flowers[len(flowers)-1] = flowers[len(flowers)-1] , flowers[0]
print(flowers)

#Print all individual elements of the list
for flower in flowers :
    print(flower)

#Continue current list with elements of list : [Orchid , Daisy , Daffodil]
lst = ["Orchid" , "Daisy" , "Daffodil"]
#flowers.append(lst) will give a list inside list
flowers = flowers+lst
print(flowers)