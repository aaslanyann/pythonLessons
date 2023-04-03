
# Exercise 1
# --------------

"""
list comprehension sarquma nor lister isk generatory chi sarqum ayl elementnera generacnuma petq ekac jamanak.
Orinak list comprehension-um menq sarqum enq list u dra mej lcnum enq elementner u stanum enq list isk 
generatory sarquma object-iterator vory next() metodi jamanak elementa generacnum u ed patcharov inqy shat tex 
chi zbaxacnum hishoxutyan vra
"""

# --------------



# Exercise 2
# --------------

"""
ete function-i mej ka yield bary uremn da function generatora
"""

# --------------

# Exercise 3
# --------------

# def fibonacii(max):
#     a, b = 0, 1
#     count = 0
#     while count < max:
#         a, b = b, b + a
#         count += 1;
#     yield a
#
#
# for num in fibonacii(25):
#     print(num)

# --------------



# Exercise 4
# --------------

# def custom_range(start, end, step):
#     while start < end:
#         yield start
#         start += step
#
# gen = custom_range(0, 25, 4)
#
# for elem in gen:
#     print(elem)
# --------------


# Exercise 5
# --------------

# def is_symetric(word):
#     length = len(word)
#     ind = 0
#     while ind < length // 2:
#         if word[ind] != word[length - ind - 1]:
#             return False
#         ind += 1
#     return True
#


# --------------

# Exercise 6
# --------------
# x = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
# y = {elem : is_symetric(elem) for elem in x} # is_symetrick functiony hingerord taskic em vercrel
# print(y)
# --------------


# Research
# --------------

# 1.
"""
__iter__ methody special methoda vorov haskanum objecty karelia ogtagorcel vorpes iterator te che.
Inqy veradarcnuma iterator-object vori vrov karanq franq for
"""
# 2.
"""
string, list, tuple, set, generator
"""

# 3.
"""
string, list, tuple, range
"""
# 4.
"""
1.iterable objectnery karan unenan xary dasavorvatyuutyun isk sequence objectnery unen iranc hajordakanutyuny.
2.iterable objectneri erkarutyuny misht fixvac chi isk sequence objectneriny misht fixvac e
4.bolor sequence data typery iterable en bayc voch bolor iterable data typernen sequence data type
"""

# --------------