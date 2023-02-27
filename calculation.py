class Banner:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def square(self):
        return self.width * self.length

    def count_luvers(self, distance):
        ''' подсчитываем количество люверсов на 1 метре
        distance - расстояние между люверсами'''
        return (self.width + self.length) * 2 * 100 / distance



# banner = Banner(2, 4)
# print(banner.perimeter())
# print(banner.square())
# print(banner.count_luvers(30))
#
