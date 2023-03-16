inp_text = {
        "first_name": "Write your first name ",
        "last_name": "Write your last name ",
        "email": "Write your email ",
        "password": "Write your password ",
        "age": "Write your age ",
        "role": "user ",
        "country": "Write your country "
    }

error_messages = {
    "first_name": "ERROR:   The first name can have a maximum of 30 letters, a minimum of 4",
    "last_name": "ERROR:   The last name can have a maximum of 30 letters, a minimum of 4",
    "email": "ERROR:   It doesn't look like gmail",
    "password": "ERROR   Password must have at least 8 characters",
    "age": "ERROR   Age must be an int type. You can write minimum 0 maximum 112",
    "country": "ERROR   Country must have minimum 3 maximum 25 charactres"
}

def registration():
    return data_entry()




def data_entry():
    result = []
    text_list = list(inp_text.keys())
    ind = 0
    try:
        while ind < len(text_list):
            if text_list[ind] == "role":
                result.append("user")
                ind += 1
                continue
            result.append(check_data(text_list[ind], input(f"{inp_text[text_list[ind]]}")))
            ind += 1
        return result
    except Exception as e:
        print(e)




def check_data(key,value):
    if key == "first_name":
        length = len(value)
        if length < 4 or length > 30:
            raise Exception(error_messages[key])
    elif key == "last_name":
        length = len(value)
        if length < 4 or length > 30:
            raise Exception(error_messages[key])
    elif key == "email":
        if value.find("@gmail.com") + 1 == 0:
            raise Exception(error_messages[key])
    elif key == "password":
        length = len(value)
        if length < 8:
            raise Exception(error_messages[key])
    elif key == "age":
        age_int = int(value)
        if age_int < 0 or age_int > 112:
            raise Exception(error_messages[key])
    elif key == "country":
        length = len(value)
        if length < 3 or length > 25:
            raise Exception(error_messages[key])

    return value



