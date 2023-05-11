#Dictionary into  List  conversion
dict = {"Nikhil" : ("Age- 26", "IIT", "Software Engineer" ), "Akshat" : ("Age-25", "JIIT", "Civil Engineer")}
 
# printing original dictionary
print("The original dictionary : " + str(dict))
 

# Dictionary to list conversion
res = [(key, i, j, k) for key, (i, j, k) in dict.items()]
 
# print result
print("The list after conversion : " + str(res)) 
# ============================================================================================


#List into Tuple coversion
#here i made a function to covert list into tuple
def convert(list):
    return tuple(list)
list =[44,58,78,99,55,88]
print(convert(list))
# ================================================================================================

#methods of lists
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

#this will tell the type of items
print(type(l))
#this will add an item at the end because list iis always ordered
l.append(5)
print(l)
#this will remove the item
l.remove(11)
print(l)
#this will arrange the list in ascending or descending order
l.sort(reverse=True)
print(l)
#this will remove the item by taking the index position as an argument
l.pop(1)
print(l)
#this will insert an item in list by taking two arguments(index and item witch you want to insert)
l.insert (1,49)
print(l)
#this will return the shallow copy of the list
l.copy()
print (l)
#this will clear all items of the list
# l.clear()
# print(l)
#this will reverse all the elements of list
l.reverse()
print(l)
#Add each element of iterable in the end of the list
l.extend([4,1,8])
print(l)
# =================================================================================================================



#Multi dimensional list
list = [[1,2,3],
         [3,4,5],
         [1,8,9]]
list[2].reverse()
print(list)
list[0].sort(reverse=True)
print(list)
list[1].extend([7])
print(list)
list[0].remove(3)
print(list)