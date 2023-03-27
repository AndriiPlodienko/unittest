import re

def str_to_w(string):
    words = re.findall(r'\w+', string)
    return words

def test_str_to_w():
    assert str_to_w("Hello, world!") == ["Hello,", "world!"]
    assert str_to_w("   ") == []
    assert str_to_w("This is a sentence.") == ["This", "is", "a", "sentence."]
    assert str_to_w("1, 2, 3, 4, 5") == ["1,", "2,", "3,", "4,", "5"]
    assert str_to_w("") == []

test_str_to_w()