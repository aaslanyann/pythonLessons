# Exercise 1
# -------------------

# print(1 + 2.0 + 3) #type = float

# kveradarcni float vorovhetev 2.0 floata

# -------------------

# Exercise 2
# -------------------

# print(2 * (3 + 4))

# -------------------


# Exercise 3
# -------------------

# print(round(2.555, 2))

# -------------------


# Exercise 4
# -------------------

# text = "Hello world"
# ind_division = text.find(" ")
#
# text = f"{text[ind_division :]} {text[: ind_division]}"
# print(text)

# -------------------


# Exercise 5
# -------------------

# first_word = "simply"
# second_word = 1500
# third_word = "galley"

# s1 = "Lorem Ipsum is  %s  dummy text of the printing and typesetting industry." \
#      "Lorem Ipsum has been the industry's standard dummy text ever since the %ds," \
#      "when an unknown printer took a %s  of type and scrambled it to make a type" \
#      "specimen book"

# s1 = "Lorem Ipsum is {0} dummy text of the printing and typesetting industry." \
#      "Lorem Ipsum has been the industry's standard dummy text ever since the {1}s," \
#      "when an unknown printer took a {2}  of type and scrambled it to make a type" \
#      "specimen book"

# s1 = f"Lorem Ipsum is  {first_word}  dummy text of the printing and typesetting industry." \
#      f"Lorem Ipsum has been the industry's standard dummy text ever since the {second_word}s," \
#      f"when an unknown printer took a {third_word}  of type and scrambled it to make a type" \
#      "specimen book"

# print(s1.format(first_word, second_word, third_word))
# print(s1 % (first_word, second_word, third_word))
# print(s1)

# -------------------


# Exercise 6
# -------------------

# tiv = 90
#
# print((tiv - tiv % 10) // 10, tiv % 10 )

# -------------------

# Exercise 7
# -------------------

# num = 797
# total = 0
#
# total += num % 10
# num = (num - num % 10) // 10
# total += num % 10
# num = (num - num % 10) // 10
# total += num % 10
# num = (num - num % 10) // 10
#
# print(total)

# -------------------