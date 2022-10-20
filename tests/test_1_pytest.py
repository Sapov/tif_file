import pytest

from main import *


def test_list_file():
    assert data.price_material.get('material', False) == False, 'Материал берется из словаря data.price_material.'


if __name__ == '__main__':
    pytest.main()
