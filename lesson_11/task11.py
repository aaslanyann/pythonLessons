# Exercise 1
# ---------------
# users_list = []
# list_key = []
# data_list = []
# ind = 0
#
# # 1.1
# with open("db.txt", "r") as text:
#     data_list = text.readlines()
#     list_key = data_list[0].strip().split(',')
#     print(list_key)
#     data_list.pop(0)
#
# for elem in data_list:
#     result = {}
#     for value in elem.split(","):
#         result[list_key[ind]] = value
#         ind += 1
#     users_list.append(result)
#     ind = 0
#
# # 1.2
#
# def foo(users_list, **kwargs) :
#     result = {}
#     for elem in kwargs.keys():
#         result[elem] = kwargs[elem]
#     users_list.append(result)
#     return users_list
#
#
# users_list = foo(users_list, first_name="Aghvan", last_name="Aslanyan", age=19,
#           profession="supermen",
#           country="Metropolis",
#           favorite_film="Top-Gun Maverick",
#           favorite_singer="Guf",favorite_chips="Doritos")
#
# # 1.3
#
# list_for_db = []
#
# for elem in users_list:
#     list_for_db.append(f"""\n
# first_name={elem[list_key[0]]}, last_name={elem[list_key[1]]},
# age={elem[list_key[2]]}, profession={elem[list_key[3]]}
# country={elem[list_key[4]]}, favorite_film={elem[list_key[5]]},
# favorite_singer={elem[list_key[6]]} ,  favorite_chips={elem[list_key[7]]}""")
#
# with open("db.txt", "a") as text:
#     text.writelines(list_for_db)
#

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