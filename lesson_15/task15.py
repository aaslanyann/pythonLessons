# Exercise 1
# --------------


# list_text = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
# palindrom_text = list(filter(lambda elem: elem == elem[::-1], list_text))
# print(palindrom_text)

# --------------



# Exercise 2
# --------------

# def custom_map(func, it):
#     result = (func(elem) for elem in it)
#     return result
#
# custom_map(lambda e: e * 2, [1,2,3,4,5])
#


# --------------


# Exercise 3
# --------------
# numbers = [5,7,9,12,4567,45,21,45,7896,1234,9984,412,354,74]
# 3.1

from functools import reduce

# def find_max_num(list):
#     max = list[0]
#     for elem in list:
#         if max < elem:
#             max = elem
#     return max
# print(find_max_num(numbers))

# 3.2
# result = reduce(lambda e,z : z if e < z else e, numbers)
# print(result)

# --------------



# Research
# ----------------
"""
reduce functiony yndunuma argument function vory yndunima erku argument arajin argument
da en argumentna vorin vor naxnakan value enq tvel isk erkrordy hajordakanutyan hajord elementy.
ev reduce erkrord argumentov yndunuma mer listy.
Reduce ogragorceluc araj petq e import anel functools-ic
"""

# ----------------



