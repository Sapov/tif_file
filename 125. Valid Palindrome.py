# '''125. Valid Palindrome'''
#
#
# def isPalindrome(s) -> bool:
#     kak = '!@#$%^&*()_+[]\'-={}"|\\/.,<>:`;? '
#     new_str = []
#     for i in s:
#         if i not in kak:
#             new_str.append(i.lower())
#     a = ''.join(new_str)
#
#     if a == a[::-1]:
#         return True
#     else:
#         return False
#
#
# print(isPalindrome("A man, a plan, a canal: Panama"))
#
# ''' two line'''
# # def isPalindrome(self, s: str) -> bool:
# #     arr = [x.lower() for x in s if x.isalnum()]
# #     return arr == arr[::-1]
#
# '''Solution 2: O(1) space (two-pointer)!!!!!!!!!!!!1'''
#
#
# def isPalindrome(s: str) -> bool:
#     i, j = 0, len(s) - 1
#     while i < j:
#         a, b = s[i].lower(), s[j].lower()
#         if a.isalnum() and b.isalnum():
#             if a != b: return False
#             else:
#                 i, j = i + 1, j - 1
#                 continue
#         i, j = i + (not a.isalnum()), j - (not b.isalnum())
#     return True

# def longestPalindrome(s: str) -> str:
#     max_pall = ''
#     for j in range(len(s)):
#         word = ''
#         for i in range(j, len(s)):
#             word += s[i]
#             if word == word[::-1] and len(word)> len(max_pall):
#                 max_pall = word
#     return max_pall
#
#
# print(longestPalindrome('avabbttbb'))


class Car:
    def __init__(self, color, miliage):
        self.color = color
        self.miliage = miliage
    def description(self):
        print(f' The {self.color} car has {self.miliage} miles.')

blue = Car('Blue', 100)
red = Car("RED", 200)
print(red)
print(red.__dict__)
blue.description()
blue.__str__()