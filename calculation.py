class Banner:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def square(self):
        ''' вычесление площади баннера
        * / 10000 # площадь печати одной штуки (см приводим к метрам / 10 000 '''
        return (self.width * self.length) / 10000

    def count_luvers(self, distance):
        ''' подсчитываем количество люверсов на 1 метре
        distance - расстояние между люверсами'''
        return int((self.width + self.length) * 2 * 100 / distance)

    # Люверсы под загиб


# banner = Banner(2, 4)
# print(banner.perimeter())
# print(banner.square())
# print(banner.count_luvers(30))
#
# print(Banner(2, 3).perimeter())
# print(Banner(2, 3).square())
# # print(Banner(2, 3).count_luvers(30))
#
#
# # Люверсы под загиб баннер 2х3 м
# print(Banner(2, 3).count_luvers(30))

