__all__ = ["collect_info"]
def collect_info():
    user_info = {}
    inp_text = ["email", "password", "first_name", "last_name"]

    for elem in inp_text:
        value = input(f"Please write your {elem} ")
        user_info[elem] = value

    regist_user(user_info)


def regist_user(user_info):
    try:
        with open("users.txt", "r+") as file:
            if check_email(user_info["email"],file.readlines()[1:]):
                raise Exception("ERROR: Senc email arden registration exaca, urish gri")

            file.write(f"\n{','.join(list(user_info.values()))}")
    except Exception as e:
            print(e)


def check_email(email,list):
    print(list)
    for elem in list:
        if email in elem.split(","):
            return True
    return False