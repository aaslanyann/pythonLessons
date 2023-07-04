# Exercise 1
# ----------------
"log2(256) answer 8"


# ----------------


# Exercise 2
# ----------------
"mi angam kavelana"

# ----------------


# Exercise 3
# ----------------

"nkary directoriuma"



# ----------------


# Exercise 4
# ----------------

# def number_predictor(num):
#     if num < 1 or num >= 100:
#         raise Exception("ERROR: Write a number from 1 to 100")
#     number_list = list(range(1, 100))
#     low = 0
#     high = len(number_list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = number_list[mid]
#
#         if guess == num:
#             return f"Your number {guess}"
#
#         user_answer = input(f"Is your number greater than {guess}?(Yes Or No)").lower()
#
#         if user_answer == "no":
#             high = mid - 1
#         else:
#             low = mid + 1
#     return "Maybe you wrong answer"

# print(number_predictor(24))
# ----------------



# Exercise 5
# ----------------
# import random
#
# def user_predicted():
#     computer_num = random.randint(1, 99)
#     low = 1
#     high = 99
#     print(computer_num)
#     while low <= high:
#         user_answer = int(input(f"Predict number {low} to {high} "))
#
#
#         if user_answer < low or user_answer > high:
#             print(f"Write number {low} to {high}")
#             continue
#
#         if user_answer == computer_num:
#             return "You win!"
#
#         if user_answer > computer_num:
#             print("My number lower")
#             high = user_answer - 1
#         else:
#             print("My number higer")
#             low = user_answer + 1
#
#
#
# print(user_predicted())


# ----------------