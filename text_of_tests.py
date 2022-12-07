import pytest

from Circle_K import gen, read_list, print_pass, add_new_item, encrypt, decrypt, main
SITE_INDEX = 0

def test_make_list():
    items_list = gen()
    assert isinstance(items_list, list)
def test_make_dic():
    items_dict = read_list("111/Week 12/private.txt", SITE_INDEX)
    # print(items_dict)
    assert isinstance(items_dict, dict)
def test_add_new_item():
    try:
        with open ("111/Week 12/private.txt"):
            pass
    except:
        assert False
def test_encrypt():
    assert encrypt
def test_decrypt():
    assert decrypt
def test_print():
    assert print_pass


    
pytest.main(["-v", "--tb=line", "-rN", __file__])