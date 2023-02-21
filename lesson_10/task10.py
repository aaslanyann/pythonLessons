# Exercise 1
# ---------------

# my_name = 'name'
#
# def f1():
#     global my_name
#     my_name = "Vzgo"
#
# f1()
# print(f"My Real Name {my_name}")

# ---------------



# Exercise 2
# ---------------

# users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza", "Janna", "Armen", "Lilit"]
# long_word = 'dzaynaskavarakavacharanoc'
# last_names = ("Watson", "Richards", "Richardson", "Saunders", "Watson", "Young", "Saunders")
#
# def identical_elements(sequence_object):
#     if type(sequence_object) == "int":
#         print('please send sequence object')
#         return
#
#     result = set()
#     length = len(sequence_object)
#     ind = 0
#     x = ind + 1
#
#     while ind < length - 1:
#         if sequence_object[ind] == sequence_object[x]:
#             result.add(sequence_object[ind])
#             ind += 1
#             x = ind + 1
#         elif x == length - 1:
#             ind += 1
#             x = ind + 1
#             continue
#         x += 1
#     return result
#
# print(identical_elements(last_names))
# ---------------



# Exercise 3
# ---------------

# def digit_sum(number):
#     result = 0
#     while number :
#         last_digit = number % 10
#         result += last_digit
#         number = (number - last_digit) // 10
#     return result
#
# print(digit_sum(789))

# ---------------




# Exercise 4
# ---------------



# def find_prime_numbers(start, end) :
#     result = []
#
#     for num in range(start, end):
#         if isPrime(num):
#             result.append(num)
#
#     return result
#
# def isPrime(number):
#     for elem in range(2, number // 2 + 1):
#         if number % elem == 0:
#             return False
#     return True
#
# print(find_prime_numbers(1,100))

# ---------------



# Exercise 5
# ---------------

# def fibon_series(n):
#     fib_num = [0,1]
#     ind = 1
#     flag = True
#     while len(fib_num) < n:
#         fib_num.append(fib_num[ind] + fib_num[ind - 1])
#         ind += 1
#
#     return fib_num[len(fib_num) - 1]
#
# print(fibon_series(7))
# ---------------


# Research
# -------------
# 1.
"""
Python Function Annotations ognuma mez mer kody aveli informativ
darcnelu hamar. Aysinqn mer haytararac popoxakannerin kam function-i
argumentnerin Annotations enq anum.
Orinak
"""
first: int = 100
# 2.
"""
erb vor uzum enq tal inch vor hajordakanutyun mer functionin parametri texum grum enq
*args ev heto erb functionin talis enq inch vor hajordakanutyun args-y darnuma tuple 
ev ayd hajordakanutyuny yngnuma args-i mej.
erb vor uzum enq tal anunavor argumentner functionin parametri texum grum enq **kwargs
ev heto erb functionin talis enq et argumentnery kwargs-y darnuma dict ev ira mej gruma ayd
popoxakannery key: value tarberakov.
ev kareli e ays erkusy irar het ogragorcel
"""


def foo(*args, **kwargs):
    print(kwargs, args)

# foo(1,2,3,4,5, name="Aghvan", last_name="Aslanyan")

# -------------
