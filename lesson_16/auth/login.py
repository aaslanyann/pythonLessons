import time
def login():
    email = input("Please write your email ")
    password = input("Please write your password ")

    logged_user_data = []
    ind = 1

    with open("users.txt", "r") as users_data:
        data = users_data.readlines()

        while ind < len(data):
            user = data[ind].strip().split(",")

            if email in user and password in user:
                logged_user_data = user
                print(f"SUCCESSFULLY:   Hello dear {logged_user_data[0]}")
                ind += 1
                return logged_user_data

            ind += 1

    raise Exception("ERROR:   Wrong password or login")
    print(f"1.2 || Login function execution time {second_variant_end_time - start_time}")


def filter_users_info(logged_user):
    if logged_user[5] == "user":
        print("-------USER(S)--------")
        print(logged_user.strip().split(","))
        print("-------USER(S)--------")
        return

    with open("users.txt", "r") as users_data:
        print("-------USER(S)--------")
        for user in users_data.readlines()[1:]:
            data_list = user.strip().split(",")

            if logged_user[5] == "admin":
                if data_list[5] == "admin" or data_list[5] == "user":
                    print(",".join(data_list))
            else:
                print(",".join(data_list))
        print("-------USER(S)--------")
