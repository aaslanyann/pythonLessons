from datetime import datetime
def decorator1(size):
    def wrapForDecorator(func):
        def wrap():
            result = func()
            if len(result) > size:
                raise Exception("ERROR: Too many passwords")
            return result
        return wrap

    return wrapForDecorator

def decorator2(func):
    def wrap():
        try:
            result = func()
            return result
        except Exception as e:
            with open("log.txt", "a+") as txt:
                txt.write(f"{datetime.utcnow()} :: {e}\n")
                print(e)


    return wrap