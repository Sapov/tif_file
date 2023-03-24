# # decorators
# import time
#
#
# def test_time(fun):
#     def wrapper(*args, **kwargs):
#         print('--------------start-----------------')
#         st = time.time()
#         res = fun(*args, **kwargs)
#         print('--------------Finish-----------------')
#         fn = time.time()
#         dt = fn-st
#         print(f'Время работы функции {dt} cек')
#         return res
#
#     return wrapper
#
# @test_time  # Это тоже декорирование
# def get_node(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
# def get_fast_node(a,b):
#     if a <b:
#         a,b, = b,a
#         while b:
#             a,b = b,a % b
#     return a
#
#
# # get_node = test_time(get_node) # Это тоже декорирование
# # get_fast_node = test_time(get_fast_node) # Это тоже декорирование
# res = get_node(2,10000000)
# res2 = get_fast_node(2,10000000)
# print(res)
# print(res2)
# 27. Remove Element

class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        n = len(nums)
        for i in range(n):
            if val in nums:
                nums.remove(val)
        print(nums, len(nums))
        return len(nums)


Solution.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
