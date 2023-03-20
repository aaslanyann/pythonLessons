import re
from functools import reduce

# Exercise 1
# ------------------

# reg_exp = r"[A-Z].[A-Z][a-z]+_\d|[A-Z].[A-Z][a-z]+|[A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+_[A-Z][a-z]+"
#
# print(re.findall(reg_exp,'S.Paloyan Vardan Vardanyan Miqayel_Abrahamyan H.Stepanyan P.Petrosyan_5 J.Blade'))

# ------------------




# Exercise 2
# ------------------

# text = """
#             There are many variations of passages of Lorem Ipsum available, but the $6700 majority have suffered alteration in some form,
# 			by injected humour, or randomised words which don't look even slightly  believable. If you are going to use a passage $3,200
# 			of Lorem Ipsum, 8,200 you need to be sure there isn't anything embarrassing hidden in the middle of text. All $5,200 the Lorem Ipsum
# 			generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator  $3,200.00 on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of $5200  model sentence structures, to generate Lorem Ipsum which looks reasonable.
# 			The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
#         """
#
# reg_exp = r"[$][0-9],[0-9]+"
# money_list = re.findall(reg_exp,text)

# 2.2

# print(reduce(lambda aggr, elem: aggr + int("".join(re.findall(r"\d", elem))), money_list,0))

# ------------------




# Exercise 3
# ------------------

# links = "https://www.youtube.com http://translate.google.ru www.github.com https://www.w3schools.com https://www.python.org"
#
# reg_exp = r"https://www.[a-z,_,0-9]+.[com,org]++"
#
# print(re.findall(reg_exp, links))

# ------------------



# Exercise 4
# ------------------
# reg_exp = r"[a-z]{5,}@[a-z]{2,4}.ru"
#
# email = input("Write your email please ")
#
#
# if re.search(reg_exp,email) :
#     print("Successfully")
# else:
#     print("Wrong format")
#

# ------------------



# Research
# --------------------

"""
regex compile anum patterni object u heto et object-y karanq ogtagorcenq et search anelu 
hamar. Erb vor menq kanchum enq re.compile-y mez veradarcnuma patterni object vori ira mej
uni compilacvac regex-y
"""

pattern = re.compile(r'\d+')


# --------------------
