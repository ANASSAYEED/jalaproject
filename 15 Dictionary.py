#Creating dictionary
Dict = dict([(1,'AASIM'), (2,'UMAR'), (3,'ADNAN'), (4,'ADNAN'), (5,'SAAD')])
print("Dictionary with each item as a pair:",Dict) #printing dictionary

#adding element in dictionary
Dict[6] = 'AAKASH'
print("\n Dictionary with new item added:",Dict)

#updating values in dictionary
Dict[3] = 'SALMAN'
print("\n Dictionary with updated values:",Dict)

print("\n Accessing one value in Dictionary:",Dict[1])

#deleting value from drictionary
del Dict[6]
print("\n Delete a value from a Dictionary:",Dict)

#creating a nested dictionary
Dict1 = {1: 'AASIM', 2: 'UMAR',
        3:{'Age' : 18, 'Branch' : 'CSE', 'Year' : 'Third Year'}}
print("\n Nested loop Dictionary:",Dict1)

print("\n Accessing an element of a Nested Dictionary:",Dict1[2])
