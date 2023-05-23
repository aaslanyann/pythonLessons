# ------------------

"""
call metody ashxatuma en jamanak erb classic stacac instance-y kanchum enq
vorpes function
"""

class A:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y

a = A(5)


# print(a(4))

"""
__new__ metody kanchvuma nor classi instace sexcelu jamanak. Inqy ogtagorcvuma
object sarqelu processy karavarelu hamar. Araji argumentov stanuma class-y u karuma avel argumentner stana.
Petq e veradarcni classi example. __init__ metody kanchvuma __new__-ic heto avtomat ev en argumentnery vor poxancvela __new__-in
poxancvuma naev initin. inity patasxanatu chi sarqelu example ayl patasxanatuya skzbnakan arjeqner tal example-in ev inicializaciya katarel.
"""

class M:
    def __new__(cls, name, lastName):
        instance = super().__new__(cls)

        instance.name = name
        instance.lastname = lastName

        return instance

    def __init__(self, name, lastname):
        self.age = 19

obj = M("Aghvan", "Aslanyan")

# print(obj.__dict__)


"""
ete class-um chka metod __new__ example sarqelu jamank avtomat kanchvuma metod __new__
ira parent classi __new__ metody. ev edranic heto kachvuma __init__ metody u talisa 
skzbnakan arjeqner
"""

class M:
    def __init__(self, a, b):

        self.a = a
        self.b = b

# obj = M("val1", "val")



"""
1. Bolor classnery jarangvum en Object-ic isk type-y prosty metaclassa vory sarquma classner
ev karavaruma dranq. type-y exampla type classi

2. Object-y ogtagorcvuma sovorakan classner stexcelu hamar. Bayc type-nel karoxa ogtagorcvi
nor classner sarqelu hamar bayc inqy karuma metaclassy additional functioner katari vory tuyla 
talis karavarel nor examplneri ashxatanqy.

"""
# ------------------



