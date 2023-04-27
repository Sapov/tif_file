import pytest


def test_list_file():
    assert 1 == 1, 'Not okey'


# def test_number_of_pieces():
#     assert type(number_of_pieces('10штбвннерю.tif')) == int, "Возвращает число "
#     assert number_of_pieces('тбвннерю.tif') == 1, "Если явно не указано количество *в штуках Возвращает число 1"
#
if __name__ == '__main__':
    pytest.main()
    # test_list_file()
    # test_number_of_pieces()
