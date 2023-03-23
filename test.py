# class Dog:
#     species = 'Canis'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} is {self.age} old'
#
#     def speak(self, sound):
#         return f'{self.name} рычит из основного класса {sound}'
#
#
# class Jack(Dog):
#     def speak(self, sound='ARF'):
#         return f'{self.name} say {sound}'
#
#
# class Colli(Dog):
#     def speak(self, sound='Mur'):
#         return f'{self.name} say {sound}'
#
#
# class Buldog(Dog):
#     def speak(self, sound='HRU'):
#         # return f'{self.name} say {sound}'
#         return super().speak(sound)
#
# class GoldenRetriver(Dog):
#     def speak(self, sound='Bark'):
#         return f' Says {sound}'
#
#
# print(GoldenRetriver('Milies', 1).speak())
#
#
# class Rectangel:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def area(self):
#         return self.width * self.length
#
#
# class Square(Rectangel):
#     side_length = 0
#
# #
# # print(Rectangel(2, 3).area())
#
# class Animal:
#     def __init__(self, name, age, length):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         return f'{self.name} sleep Pfff...'
#
#     def say(self, sound='GAV'):
#         return f' {self.name} say {sound}'
#
#
# class Cat(Animal):
#     def __init__(self, color):
#         super().__init__(color, color)
#
#     def Mau(self):
#         return f' {self.name} Murr Myau'
#
#
# class Dog(Animal):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#     def __str__(self):
#         return f' {self.name} is {self.color} color '
#
#
# mili = Dog('Mili', 'red')
# print(mili.say())
# # mili
# print(mili)
# if  a> b:
#     выводим в порядка возрастания от b до a
# #
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
# если A < B, или в порядке убывания в противном случае. Использовать только рекурсию, а в меню можно использовать циклы

# def recursiv(a, b):
#     if a < b:
#         print(a + 1)
#         recursiv(a+1, b)
#     else:
#         print(a - 1)
#         recursiv(a-1, b)
#
#
# recursiv(1, 4)
# def foo(a, b):
#     def bar(x, y, d):
#         if x == y:
#             print(x)
#             return
#         else:
#             print(x)
#             bar(x + d, y, d)
#
#     d = 1 if b > a else -1
#     bar(a, b, d)
#
#
# foo(1, 10)


# def isvald(s):
#     stack = []
#     dict = {"{": '}', "(": ")", "[": '}'}
#     for char in s:
#         if char in dict:
#             stack.append(char)
#         elif not stack or dict[stack.pop()] != char:
#             print('False')
#             return False
#     print('Tr')
#     return len(stack) == 0
#
# isvald("()[]{}")
