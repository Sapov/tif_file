import pytest
from main import input_path


def test_input_path():
    assert (input_path('u8') == bool)


if __name__ == '__main__':
    pytest.main()
