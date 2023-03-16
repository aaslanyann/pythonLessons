# Exercise 1
# -------------------
# from auth import login,registration
# import time
#
# def login_wrapp(func):
#     def wrapp():
#         print("Loading....")
#         try:
#             start_time = time.time()
#             user_data = func()            #the func must return user data
#             end_time = time.time()
#             print(f"1.2 || Func execution time {end_time - start_time}")
#
#             login.filter_users_info(user_data)
#         except Exception as e:
#             print(e)
#         print("Loading end")
#
#     return wrapp

# -------------------




# Exercise 2
# -------------------
# def register_wrapp(list):
#     def register(func):
#         def wrapp():
#             user_data = func()
#             if user_data[6] in list:
#                 return user_data
#             else:
#                 raise Exception("ERROR:   This country is not available for registration")
#         return wrapp
#     return register

# -------------------


#
# variant = input("Login or Registratrion ").lower().strip()
#
# if variant == "login":
#     login_wrapp(login.login)()
# elif variant == "registration":
#     try:
#         user_data = register_wrapp(["Armenia", "Russia", "USA", "Morocco"])(registration.registration)()
#         with open("users.txt", "a") as data_txt:
#             data_txt.write(f"\n{','.join(user_data)}")
#     except Exception as e:
#         print(e)
