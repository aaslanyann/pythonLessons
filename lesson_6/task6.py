# Exercise 1
# -----------------

# x = {1,2,4,5,6}
# y = {5,6,7,8,9}

# 1.1
# print(y.intersection(x))

# 1.2

# print(x.difference(y))

# -----------------



# Exercise 2
# -----------------

# x = {1,2,4,5,6}
# y = {5,6,7,8,9}
#
# remove_items = list(x.intersection(y))
# x.remove(remove_items[0])
# x.remove(remove_items[1])
# print(x)


# -----------------



# Exercise 3
# -----------------

"""Default yndunuma r aysinqn read"""


# -----------------

# Exercise 4
# -----------------

# acc_premium = open("NF_premium.txt", "w")
# acc_premium.writelines([
#     "lquinon6@yahoo.com:Maca2016$ | Premium | Your next billing date is February 8, 2023.\n",
#     "zahirahanis@yahoo.com:CabbAgE_532XTiRed_John22 | Premium | Your next billing date is 29 January 2023.\n"
#                         ])
# acc_premium.close()
#
# acc_standart = open("NF_standart.txt", "w")
# acc_standart.writelines([
#     "melerojr5@gmail.com:Melerito5 | Standart | Sonraki faturalama tarihiniz: 25 Ocak 2023.\n",
#     "loviselimstrand@hotmail.com:Baby2017 | Standard | Din neste faktureringsdato er 26. januar 2023.\n"
# ])
#
# acc_standart.close()
#
# add_prem = open("NF_premium.txt", "a")
# add_prem.write("pame3111@gmail.com:Andriws2829 | Premium | Your next billing date is February 12, 2023.\n")
# add_prem.close()
#
# add_stan = open("NF_standart.txt", "a")
# add_stan.write("paullovett01@gmail.com:Ytrewq1304! | Standard | Your next billing date is 31 January 2023.")
# add_stan.close()
#
# file_name = input('which file do you want to read? ')
# with open(f"{file_name}.txt", "r") as need_file:
# 	print(need_file.read())
# 	need_file.close()


# -----------------

# Exercise 5
# -----------------

# users = [
# 			{
# 				'first_name': 'Jorj',
# 				'last_name' : 'Bush',
# 				'age':55
# 			},
#
# 			{
# 				'first_name': 'James',
# 				'last_name' : 'Bond',
# 				'age':100
# 			}
# 		]
#
# users_info = open("users_info.txt", "w")
# users_info.writelines([
#     f"user 1: first_name = {users[0]['first_name']}, last_name = {users[0]['last_name']}, age = {users[0]['age']}\n",
#     f"user 2: first_name = {users[1]['first_name']}, last_name = {users[1]['last_name']}, age = {users[1]['age']}"
# ])
# users_info.close()

# -----------------



# Research
# -----------------
# 1
# """Stuguma seti mej arkayutyuny yndhanur andamneri other (tuple, list, str, set) hajordakanutyan het
#    orinak"""
# set_x = {0, 1, 2, 3, 4}
# list_y = [5, 6, 7, 8, 9]
# set_x.isdisjoint(list_y)

# 2
"""Tarbervum en nranov ete uzum enq 
jnjenq element bayc elementy 
chka setum discardy error chi ta bayc remove kta keyerror"""

# -----------------

