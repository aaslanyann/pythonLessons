# Exercise 1
# ------------------
from decorators import decorator1, decorator2
@decorator2
@decorator1(7)
def get_sensitive_data():
    result = []
    i = 1
    with open("password.txt", "r") as txt:
        data = txt.readlines()

    while i < len(data):
        userData = data[i].split(",")
        result.append({userData[0]: userData[1].replace("\n", "")})
        i += 1

    return result



print(get_sensitive_data())


# ------------------

# Research
# ------------------

"""
vorpesi sarqenq decorator parametrov vory kareli e ogtagorcel classi hamar
petq e sarqenq function decorator vor yndunuma parametr ev veradarcnuma function decorator.
Orinak
"""

def decorator_with_parameter(parameter):
    def decorator(cls):
        cls.parameter = parameter

        return cls

    return decorator



@decorator_with_parameter("Значение параметра")
class MyClass:
    pass

print(MyClass.parameter)











# ------------------