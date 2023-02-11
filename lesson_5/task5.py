# Exercise 1
# -----------------

# user = {
#     'name':'Jarviz',
# 	'age' : '100',
# 	'professions':['robot', 'dancer'],
# 	'test_result':[14,5,8,99,12,2,3,5,4]
# }
#
# # 1.1
# print(user['professions'][0])
# user['professions'][1] = "bad dancer"
#
# # 1.2
# user["test_result"].sort(reverse=True)


# -----------------

# Exercise 2
# -----------------

# fruits = {
# 		"banana": 4,
# 		"apple": 2,
# 		"orange": 1.5,
# 		"pear": 3
# }


#
# # 1.1
#
# dic_values = fruits.values()
# print(sum(dic_values))
#
# # 1.2
#
# fruits["dzmeruk"] = 10
# print(fruits)
# -----------------


# Exercise 3
# -----------------
# users = [
# 			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
# 			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
# 		]
#
# # 3.1
# users[0]["first_name"], users[1]["first_name"] = "Aghvan", "Vazgen"
# users[0]["last_name"], users[1]["last_name"] = "Aslanyan", "Barsexyan"
# users[0]["age"], users[1]["age"] = 19, 17
# users[0]["phone"], users[1]["phone"] = {"brend": "Apple", "number": 37443887456, "is_5g": True }, {"brend": "Xiaomi", "number": 37498574231, "is_5g": False }
#
# # 3.2
# users[0]["car"], users[1]["car"] = {"model": "Volga", "type": "sedan", "max_speed": 80}, {"model": "Jiguli", "type": "sedan", "max_speed": 90}
#
# # 3.3
#
# # print(f"Aghvans is 5g {users[0]['phone']['is_5g']} Vazgen is 5g {users[1]['phone']['is_5g']}")
#
# # 3.4
# x = users[1]["age"] > 18 and users[1]['phone']['is_5g'] or users[1]["first_name"] != "Bill" and users[1]["last_name"] != "Gates"
# print(f"chipavorvac e {x}")
# -----------------


# Exercise 4
# -----------------
# first_dict = dict(zip("jar", "siv"))
# second_dict = dict(zip("vis", "raj"))
# first_dict.update(second_dict)
# print(first_dict)


# -----------------


# Research
# -----------------
"""1. Ete dimum enq dict-in key-ov ev key-in chka veradarcnum e ayn arjeqy vory defaultov tvel enq
orinak
"""
# my_dict = {"kov" : "cul"}
# my_dict.setdefault("cul", "chka")
# print(my_dict["cul"])

"""2. Tvac harjordakanutyunic sarquma dict ete value chenq tvel default None e drvum ashxatuma list-eri, str-neri het
orinak
"""
# new_dict = dict.fromkeys("kov", "Tver")
# print(new_dict)

# -----------------

