# Exercise 1
# ---------------
# users = []
# my_info = "Aghvan,Aslanyan,19,Apex,Metropolis,Top-Gun Maverick,Guf,Pringles"
#
# with open("db.txt", "r") as txt:
#     user_data = txt.readlines()
#     user_data.append(my_info)
#
# # 1.1
# for ind, elem in enumerate(user_data,0):
#     if ind != 0:
#         users.append(dict(zip(user_data[0].strip().split(","), user_data[ind].strip().split(","))))
#
# # 1.2
# def foo(user_list, **kwargs):
#     for elem in kwargs:
#         for ind, val in enumerate(kwargs[elem], 0):
#             users[ind][elem] = val
#
#
# foo(users, favourite_car=["Range Rover","BMW","Aston Martin"], boy=['1.75','1.76','1.78'])
#
# # 1.3
#
# lines = []
# lines.append(",".join(list(users[0].keys())).strip())
#
# for elem in users:
#     lines.append(",".join(list(elem.values())).strip())
#
#
# with open("db.txt", "w") as txt:
#     for line in lines:
#         txt.write(line + "\n")

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

























