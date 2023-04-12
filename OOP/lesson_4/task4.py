# Exercise 1
# -----------------
"""
amenaskzbic man kga et metody d-i mej heto kgna b ktesni vor b-en a-ica jarangvum u ktena vor c-nela jarangvum
kichni nerqev mi hat c-ei mej knayi u kontrolni a-i mej knayi u durs kga
"""

# -----------------



# Exercise 2
# -----------------

# from abc import ABC, abstractmethod
#
#
# class AbstractFile(ABC):
#
#     @abstractmethod
#     def translate(self):
#         pass
#
#
#     @abstractmethod
#     def write(self):
#         pass
#
#
#
# class EnglishFile(AbstractFile):
#     last_translated = ""
#
#
#     def translate(self, text):
#         translatedText = ""
#         translated_chars = {
#             'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH',
#             'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
#             'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
#             'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'YU',
#             'Я': 'YA', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
#             'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
#             'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh',
#             'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
#             'ю': 'yu', 'я': 'ya', " ": " "
#         }
#
#         for char in text:
#             translatedText += translated_chars[char]
#
#         self.last_translated = translatedText
#
#         return translatedText
#
#     def write(self):
#         with open("EnglishTranslated.txt", "w+") as txt:
#             txt.write(self.last_translated)
#
#
#
# class RussianFile(AbstractFile):
#     last_translated = ""
#     def translate(self, text):
#         translatedText = ""
#         translated_chars = {
#             'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х',
#             'I': 'И', 'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
#             'Q': 'КЬЮ', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У', 'V': 'В', 'W': 'В', 'X': 'КС',
#             'Y': 'Ы', 'Z': 'З', 'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф',
#             'g': 'г', 'h': 'х', 'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
#             'o': 'о', 'p': 'п', 'q': 'кью', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в',
#             'w': 'в', 'x': 'кс', 'y': 'ы', 'z': 'з'
#         }
#
#         for char in text:
#             translatedText += translated_chars[char]
#
#         self.last_translated = translatedText
#
#         return translatedText
#
#     def write(self):
#         with open("RussianTranslated.txt", "w+") as txt:
#             txt.write(self.last_translated)
#
#
# eng_translate = EnglishFile()
# print(eng_translate.translate("привет брат"))
# eng_translate.write()
# -----------------
