# Exercise 1
# ----------------------

# class Animal:
#
#     """
#     Kendanineri class
#     """
#
#     def __init__(self,eyes, hands, lags, color, running_speed = "45(km/h)"):
#         self.eyes = eyes
#         self.hands = hands
#         self.lags = lags
#         self.color = color
#         self.running_speed = running_speed
#
#     def voice(self):
#         return "dzayn em hanum"
#
#     def running(self):
#         print(f"vazum em {self.running_speed} aragutyamb")
#
#     def __str__(self):
#         return "kendani"


# ----------------------



# Exercise 2
# ----------------------

# class Cat(Animal):
#
#     """
#     Katuneri class
#     """
#
#
#     def __init__(self,eyes, hands, lags, color, running_speed = "45(km/h)"):
#         super().__init__(eyes, hands, lags, color, running_speed)
#
#
#     def cat_voice(self):
#         return f"mlavelu {super().voice()}"
#
#
#     def voice_and_running(self):
#         print("meow")
#         super().running()
#
#     def __str__(self):
#         return "Katu"


# ----------------------


# Exercise 3
# ----------------------

# class Lion(Cat):
#     """
#     Aryucneri class
#     """
#
#     def __init__(self, eyes, hands, lags, color, running_speed = "45(km/h)"):
#         super().__init__(eyes, hands, lags, color, running_speed)
#
#
#     def eat_human(self):
#         return "nyam nyam"
#
#     def __str__(self):
#         return "Aryuc"


# ----------------------

# print(Animal.__doc__)            #karoxanum enq docmentation stananq kam help-ov kam __doc__
# print(Lion.__bases__)            #talisa mez te classy inch classica jarangvac
# print(issubclass(Lion, Cat))     # ays functionov stugum enq mi classy myusic jarangvaca te che naev karox enq erkrord argumentov tanq tuple ev aydpes stugel