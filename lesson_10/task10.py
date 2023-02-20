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
# def sequence_object(multiplicity):
#     if type(multiplicity) == "int":
#         print('please send sequence object')
#         return
#
#     length = len(multiplicity)
#     result = []
#
#     for i in range(length):
#
#         for j in range(i + 1, length):
#
#             if multiplicity[i]  == multiplicity[j]:
#                 result.append(multiplicity[i])
#                 break
#
#     return result
#
# print(sequence_object(last_names))
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
#     def isPrime(number):
#         for elem in range(2, number // 2 + 1):
#             if number % elem == 0:
#                 return False
#         return True
#     for num in range(start, end):
#         if isPrime(num) :
#             result.append(num)
#
#     return result
#
# print(find_prime_numbers(1,100))

# ---------------



# Exercise 5
# ---------------

# def fibon_series(n):
#     result = [0,1]
#     ind = 1
#     flag = True
#     while flag:
#         if result[ind] + result[ind - 1] >= n:
#             flag = False
#             break
#         result.append(result[ind] + result[ind - 1])
#         ind += 1
#     return result
#
# print(fibon_series(10))
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

foo(1,2,3,4,5, name="Aghvan", last_name="Aslanyan")

# -------------
