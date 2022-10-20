import pytest

from main import *


def test_list_file():
    assert data.price_material.get('material', True) == True, 'Материал берется из словаря data.price_material.'


# def test_number_of_pieces():
#     assert type(number_of_pieces('10штбвннерю.tif')) == int, "Возвращает число "
#     assert number_of_pieces('тбвннерю.tif') == 1, "Если явно не указано количество *в штуках Возвращает число 1"
#
# if __name__ == '__main__':
    pytest.main()
    test_list_file()
    test_number_of_pieces()
