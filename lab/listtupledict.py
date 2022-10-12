'''
#LIST OPERATION 

#creating a list
l=list()
#adding element
l.append(1)
l.append(2)
l.append(3)
#GETTING MAX ELEMENT
print(F'MAXIMUM ELEMENT IS : {max(l)}')
#GETTING MIN ELEMENT
print(f'MINIMUM IS : {min(l)}')
#DELETING A ELEMENT
print(f'before deleting : {l}')
del l[1]
print(f'after deleting : {l}')




#TUPLE OPERATION

#creating a tuple
t=(1,2,3)
#we cant add element to tuple directly convert to list then add
t=list(t)
t.append(4)
t=tuple(t)
#print the max
print(F'MAXIMUM ELEMENT IS : {max(t)}')
#GETTING MIN ELEMENT
print(f'MINIMUM IS : {min(t)}')
#we can't delete element directly from tuple
print(f'before deleting : {t}')
t=list(t)   
del t[2]
t=tuple(t)
print(f'after deleting : {t}')

'''

#CREATING DICTIONARY
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
#ADDING ELEMENT
thisdict["color"] = "red"
#GETTING THE MAX ELEMENT
print(F'MAXIMUM KEY IS : {max(thisdict)}')
#GETTING MIN ELEMENT
print(f'MINIMUM KEY IS : {min(thisdict)}')
#DELETING A ELEMENT
print(f'before deleting : {l}')
del thisdict["color"]
print(f'after deleting : {l}')