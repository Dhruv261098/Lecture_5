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

