# Exercise 1
# -------------------

"""
__delete__ kanchvuma atribut jnjelu jamanak
isk __del__ kanchvuma erb vor jnjum esobjecty
"""

# -------------------


# Exercise 2
# -------------------

import os

class FileError(Exception):

    def __init__(self, err_text = "Default message"):
        self.err_text = err_text
    def __str__(self):
        return self.err_text



class SingleError(FileError):
    def __init__(self,err_message, line):
        self.err_message = err_message
        self.line = line

    def __str__(self):
        return f"{self.line} {self.err_message}"

class ManyError(FileError):
    def __init__(self, err_message, line):
        self.err_message = err_message
        self.lines = line

    def __str__(self):
        return f"{self.line} {self.err_message}"

class DescriptorFile:

    def __get__(self, instance, owner):
        if not os.path.exists(instance._file):
            with open(instance._file, "w+") as txt:
                pass
            return txt

        with open(instance._file, "r") as txt:
            pass
        return txt

    def __set__(self, instance, value):
        os.rename(instance._file, value)
        instance._file = value


class DescriptorChildFile:

    def __get__(self, instance, owner):
        error_lines = []
        with open(f"{instance.__class__.__name__.lower()}.txt", "r") as txt:
            text_lines = txt.readlines()

        for line in text_lines:
            if "__error__" in line:
                error_lines.append(line[0])

        if len(error_lines) > 1:
            raise ManyError("ManyError: You have errors in line", ','.join(error_lines))
        elif len(error_lines) == 1:
            raise SingleError("SingleError: You have error in line", ','.join(error_lines))
    def __set__(self, instance, value):
        with open(f"{instance.__class__.__name__.lower()}.txt", "w") as txt:
            txt.write(value)

    def __delete__(self, instance):
        os.remove(f"{instance.__class__.__name__.lower()}.txt")

class File:
    file = DescriptorFile()
    child_file = DescriptorChildFile()

    def __init__(self):
        self._file = f"{self.__class__.mro()[0].__name__.lower()}.txt"
        self._child_file = ""


fail = File()

class Tesla(File):
    pass

class Lexus(File):
    pass

# tesla = Tesla()
# lexus = Lexus()
#
# try:
#     print(tesla.child_file)
#     # print(lexus.child_file)
#
# except FileError as e:
#     print(e)

# -------------------
