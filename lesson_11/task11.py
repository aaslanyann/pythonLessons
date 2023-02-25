# Exercise 1
# ---------------

# users = []
# dict_key = []
# user_data = []
# my_info = "Aghvan,Aslanyan,19,Apex,Metropolis,Top-Gun Maverick,Guf,Pringles"
#
# with open("db.txt", "r") as txt:
#     user_data = txt.readlines()
#     dict_key = user_data[0].strip().split(",")
#     user_data.pop(0)
#
# user_data.append(my_info)
#
# # 1.1
# for elem in user_data:
#     users.append(dict(zip(dict_key, elem.split(","))))
#
#
# # 1.2
#
# def foo(user_list, **kwargs):
#     key = list(kwargs.keys())[0]
#     dict_key.append(key)
#     for ind, elem in enumerate(kwargs[key],0):
#         user_list[ind][key] = elem
#     return user_list
#
# users = foo(users, favorite_car=["BMW", "Range Rover", "Volga"])
#
# # 1.3
# lines = []
# lines.append(",".join(dict_key))
#
# for elem in users:
#     lines.append(",".join(elem.values()).strip())
#
# with open("db.txt", "w") as txt:
#     for line in lines:
#         txt.write(line.strip() + '\n')


# ---------------

# Exercise 2
# ---------------
# numbers = [[[[[10]]]]]
# def foo(l):
#     if type(l[0]) == int:
#         return l[0]
#     return foo(l[0])
#
# print(foo(numbers))


# ---------------




# Exercise 3
# ---------------

# numbers  = [1, 2, [3, 4], [5, 6, [10, 19]]]
#
# def foo(nums):
#     result = 0
#
#     for elem in nums:
#         if type(elem) == list:
#             result += foo(elem)
#         else:
#             result += elem
#
#     return result
#
# print(foo(numbers))

# ---------------



# Reserach
# ---------------

"""
lambda functiony anonim functioner en. hatuk def barov haytararum em sovorakan function.
Function kara stana lyuboy chapi argumentner
Orinak*
"""

double = lambda x: x*2
# print(double(5))




# ---------------