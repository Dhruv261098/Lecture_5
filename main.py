# List

my_list = ["Windows", "Linux", "MAC OS", "Unix"]
print(type(my_list))

# [NUMBER_OF_ELEMENTS] [INDEX_NUMBER]
# Index in python starts from 0
# That means the index of the first elememt is 0

print('First Element', my_list[0])
print('Lats Element', my_list[-1])

print('Length', len(my_list))

# Using Range

# [START_POINT: END POINT]

print(my_list[0:2])
# 0
# 0 + 1
# 1 + 1 = 2 (Don't peint 2)


# No o/p
print(my_list[1:1])
# 1 = 1

print(my_list [-1:-2])
print(my_list[-1:-2])

# To add step size (By default it is set to 1)
# [START_POINT: END POINT: STEP_SIZE]
print(my_list)
print(my_list[0:3:2])
# o -> Windows
# 0 + 2 -> Mac OS
# 2 + 2 -> is out of range


# to replace element

my_list[0] = "Windows 10"
print(my_list)

# to print element of list of list

my_list = ["Windows", "Linux", "MAC OS", "Unix", [0,1,2]]
print(my_list[-1][2])

# Append -> allow us to add single element to a list
my_list.append("Dhruv")
print(my_list)

# insert -> allow us to insert a single element in list at secific position

my_list.insert(0, "Desai")
print(my_list)

# index(element) -> To get index of the perticular elemet
print(my_list.index("Dhruv"))

# count(element) -> To count the occurance of element
my_list = ["Windows", "Linux", "MAC OS", "Unix", [0,1,2],"Windows"]
print(my_list.count("Windows"))

# remove(element) -> To remove element
my_list.remove("Linux")
print(my_list)