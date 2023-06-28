# Exercise 1
# ----------------
"""
__getattr__ - kanchvuma en jamanak erb vor atributy chi gtnum isk __getattribute__
kanchvuma amen angam erb objectic atributi arjeq enq uzum
"""
# ----------------



# Exercise 2
# ----------------

"""
Aravelutyunner

1. Mekusacnuma popoxotyunnery classi mej, private attributnery
tuyla talis taqcnel classi nersi irakanacman bardutyuny, inchy tuyla 
talis popoxel kam tarmacnel ira voch azdecutyuny cody vra vory ogtagorcum e
ayd classy

2. Sxalneri kanxum, private attributnery kanxum en patahakan
attributneri popoxutyunneri katarumy drsic. Inchy kara beri errorneri
programy ashxatacnelu jamanak ete chykanxenq

3. Taqcnel karevor datan, private attributnery tuyl en talis taqcnel karevor
datanery koxmnaki mardkancic inch apahovum e lracucich security

Terutyunner

1. Sahmanapak access, private attributneri ogragorcumy kara sahmanapaki 
classi ogtagorcman hnaravorutyunnery iranic durs, inchy kdjvarecni test anely
u errorneri  haytnaberumy

2. Canrabernavacutyun, private atributneri ogtagorcumy kara beri bazmativ 
getterner ev setterner ogtagorcelu kariq vorpesi menq unenanq access iranc hamar
inch kara mer cody aveli xuchuch ev djvar haskanali sarqi

"""

# ----------------


# Exercise 3
# ----------------


class God:

    def __init__(self, first_name, count_of_hands, super_power):
        self.first_name = first_name
        self.count_of_hands = count_of_hands
        self.super_power = super_power


    def clap(self):
        if self.count_of_hands >= 2:
            self.__voice_after_clap()
        else:
            raise Exception("Puu dzernery chyheriqec")

    def __voice_after_clap(self):
        print("chlp")


class Zeus(God):
    vay = "day"
    _bay = "zay"
    __lai = "bai"
    def levin(self):
        self.voice_after_levin()
    def _voice_after_levin(self):
        print("pyuuuu")

class Hercules(Zeus):

    def get_public(self):
        members = []
        for cls in self.__class__.mro():
            if cls == object:
                continue

            for member_name, member in cls.__dict__.items():
                if not member_name.startswith("_"):
                    members.append((member_name, member))

        return members

    def get_protected(self):
        members = []
        for cls in self.__class__.mro():
            if cls == object:
                continue

            for member_name, member in cls.__dict__.items():
                if member_name.startswith("_") and not member_name.startswith(f"_{cls.__name__}") and not member_name.startswith("__"):
                    members.append((member_name, member))

        return members

    def get_private(self):
        members = []
        for cls in self.__class__.mro():

            if cls == object:
                continue

            for member_name, member in cls.__dict__.items():
                if member_name.startswith(f"_{cls.__name__}"):
                    members.append((member_name, member))

        return members



txa = Hercules("Valod", 2, 1000)

print(txa.get_public())
# print(txa.get_protected())
# print(txa.get_private())

# print(txa.__dict__.items())



# ----------------


# Research
# -------------
# 1

"""
__slots__- ira mej grvaca te inch anunov atributner karas kces classi instansin
"""

# 2

"""
propertyn da  decoratora vory ogragorcvuma stexcel attributner voronq unen getter, setter, deleter
"""


# -------------




