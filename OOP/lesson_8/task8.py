# Exercise 3
# -------------------
import os

class File:

    def __init__(self):
        self._file = f"{self.__class__.mro()[0].__name__.lower()}.txt"
        self._child_file = ""


    @property
    def child_file(self):
        with open(f"{self.__class__.__name__.lower()}.txt", "r") as txt:
            return txt.read()

    @child_file.setter
    def child_file(self, new_text):
        with open(f"{self.__class__.__name__.lower()}.txt", "w") as txt:
            txt.write(new_text)

    @child_file.deleter
    def child_file(self):
        os.remove(f"{self.__class__.__name__.lower()}.txt")


    def get_file(self):
        if not os.path.exists(self._file):
            with open(self._file, "w+") as txt:
                pass
            return txt

        with open(self._file, "r") as txt:
            pass
        return txt


    def set_file(self, file):
        os.rename(self._file, file)
        self._file = file

    file = property(get_file, set_file)

fail = File()

class Tesla(File):
    pass

class Lexus(File):
    pass

tesla = Tesla()

print(tesla.child_file)