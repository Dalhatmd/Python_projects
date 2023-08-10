my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
print("The list with unique elements only:")
temp_list = my_list[:]
for i in my_list:
    if i in temp_list:
        del my_list[i]
print(my_list)