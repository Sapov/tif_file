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


# def palindrom_nums(nums: int):
#     if nums < 0 or (nums % 10 == 0 and nums != 0):
#         return False
#
#     half = 0
#     while nums > half:
#         half = (half * 10) + nums % 10
#         nums = nums // 10
#     return half == nums or nums == half // 10
#
#
# print(palindrom_nums(12821))
import requests


def download_arh(url_file):
    response = requests.get(url_file)
    print(response.headers['content-type'][-3:])
    print(response.headers['content-type'])
    print(response.text)

    with open('1temp_arh.zip', 'wb') as file:
        file.write(response.content)  # Retrieve HTTP meta-data print(r.status_code)


download_arh(
    # url_file='https://cloclo-stock2.datacloudmail.ru/stock/get/hkKTPxyugoZKVqXTCrA3GoykjWdUifpSrZthjGQAn4noFgGMWSQLaYCRrkQxCsgQ42d6vTxThu92/2%D1%88%D1%82_%D0%B1%D0%B0%D0%BD%D0%BD%D0%B5%D1%80_3000%D1%856000%D0%BC%D0%BC_%D0%BF%D0%BE%D0%BB%D0%B55%D1%81%D0%BC.zip?x-email=sapov%40mail.ru')
    url_file='https://yadi.sk/d/Gtz7keThu1497w%5Cn')