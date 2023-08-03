# Exercise 1
# ------------------

# 1.1
"qani anyndhat petqa mejy ban avelacnenq u verjum hashvenq aveli lav klini ogtagorcenq array"

# 1.2
"Xoharary hachaxordneri patverneri vrov gnuma amen mi patver mejy kara unena shat data u dra hamar harmar klini linked listy"

# ------------------



# Exercise 2
# ------------------

# class Node:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     def set_data(self, data):
#         self.__data = data
#
#     def get_data(self):
#         return self.__data
#
#     def set_next(self, node):
#         self.__next = node
#
#     def get_next(self):
#         return self.__next
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.__head = None
#
#     def is_empty(self):
#         return self.__head is None
#
#     def add(self, item):
#         node = Node(item)
#         node.set_next(self.__head)
#         self.__head = node
#
#     def size(self):
#         current = self.__head
#         count = int(bool(current))
#         while current and current.get_next():
#             current = current.get_next()
#             count += 1
#         return count
#
#     def remove_item(self, val):
#         current = self.__head
#
#         if current.get_data() == val:
#             self.__head = current.get_next()
#             return "Item removed"
#
#         while current:
#             if current.get_next().get_data() == val:
#                 current.set_next(current.get_next().get_next())
#                 return "Item removed"
#
#             if current.get_next() is None:
#                 return "There is no such element"
#
#             current = current.get_next()
#
#     def __str__(self):
#         if self.__head is None:
#             return '[]'
#         current = self.__head
#         data = f"[{current.get_data()}"
#         while not current.get_next() is None:
#             current = current.get_next()
#             data += ", " + str(current.get_data())
#         return data + "]"
#
#     def search(self, val):
#         current = self.__head
#         while current:
#             if  current.get_data() == val:
#                 return current
#
#         return "Not found"
#
#     def __iter__(self):
#         self.current = self.__head
#         return self
#
#     def __next__(self):
#         if self.current is None:
#             raise StopIteration
#         data = self.current.get_data()
#         self.current = self.current.get_next()
#         return data
#






# my_list = LinkedList()
# my_list.add(1)
# my_list.add(5)
# my_list.add(75)
# print(my_list.remove_item(75))
# print(my_list)
# print(my_list.search(5).get_data())

# for elem in my_list:
#     print(elem)


# ------------------


# Research
"""
Inqy data structure vory iranic nerkayacnuma dinamic popoxelu ira razmernery.
Sovorakan array-ic tarbervuma nranov vor ira razmery kara poxvi programmi katarelu jamanak,
inchy iran darcnuma aveli flexible u aveli harmar data collectioneri het ashxatelu hamar.
"""