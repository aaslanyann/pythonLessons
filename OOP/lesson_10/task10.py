# Exercise 1
# ----------------
import datetime

def decorator_log(func):
    def wrapper(log, password):
        try:
            func(log, password)
        except Exception as e:
            with open("log.txt", "a") as txt:
                txt.write(f"{datetime.datetime.now()} {e} \n")
            print(e)
    return wrapper

@decorator_log
def login(log, password):
    if log != "admin":
        raise Exception("Invalid User")
    elif password != "admin":
        raise Exception("Invalid User")

    return True

# login("admin", "admn")



# ----------------



# Exercise 3
# ----------------

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.file = open("log.txt", "a")

    def write(self,text, dateTime):
        self.file.write(f"{dateTime}: {text}\n")


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Hello Admin")
            self.file.close()
        else:
            print("Invalid user")
            self.write(exc_val, datetime.datetime.now())

            return True

    def do_login(self):
        if self.login != "admin" or self.password != "admin":
            raise Exception("Invalid User")

        return True


# with User("admin", "admn") as user:
#     user.do_login()


# ----------------


# Research
# --------------

"""
decoratory patatum enq mi hatel functioni mej 
"""

# ---------------
