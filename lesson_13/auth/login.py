__all__ = ["authorization"]
def authorization():
    email = input("Please write your email ")
    password = input("Please write your password ")
    checkEmailAndPass(email,password)

def checkEmailAndPass(email,password):
    need_user = []
    with open("users.txt", "r") as file:
        try:
            for ind, elem in enumerate(file.readlines()[1:],0):
                list_of_values = elem.split(",")
                if email in list_of_values and password in list_of_values:
                    need_user = list_of_values
            if need_user:
                print(f"Hello {need_user[2]} {need_user[3]}")
            else:
                raise Exception("Sxala loginy kam paroly")
        except Exception as e:
            print(e)