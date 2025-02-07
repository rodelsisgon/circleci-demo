import pytest
from main import addme

def test_addme():
    assert addme(1,1) == 2
    assert addme(10,11) == 21
    assert addme(-1,20) == 19
    print("addme Function works correctly")

if __name__ == '__main__':
    test_addme()
