#empty list
my_list=[]

#Add elements to my_list
numbers =[10,20,30,40]
print("Before append:",numbers)

#use append method
my_list.extend(numbers)
print("After extend:", my_list)

#insert element at index 1
my_list.insert(1,15)
print("After insert:", my_list)

#extend my_list with my_numbers
print("List1:",my_list)
my_numbers=[50,60,70]
print("List2:",my_numbers)

#join two lists
my_list.extend( my_numbers)
print("List after extend:",my_list)

#Remove the last element
del my_list[-1]
print("After removing last element:", my_list)

#sort my_list
my_list.sort()
print("Sorted list:",my_list)

#find and print the index of the value 30
index_of_30=my_list.index(30)
print("Index of 30:",index_of_30)



my_list







