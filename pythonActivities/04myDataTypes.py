#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview

#str: text/characcter
x = "Hello World, it is I, Danielle"		

#int: integers
x = 20		

#float: convert to integer
x = 20.5		

#complex
x = 1j		

#bool: True or False Expression 
x = True	

#python arrays
#list: is a collection which is ordered and changeable. Allows duplicate members
x = ["apple", "banana", "cherry"]	

#tuple: is a collection which is ordered and unchangeable. Allows duplicate members	
x = ("apple", "banana", "cherry")	

#dictionary: is a collection which is unordered, changeable and indexed. No duplicate members
x = {"name" : "John", "age" : 36}		

#set: is a collection which is unordered and unindexed. No duplicate members
x = {"apple", "banana", "cherry"}		
##	

#type() is the function that returns the type of an object passed to argument. You can use this to find out the type of an object.
x = 5
print(type(x)) 