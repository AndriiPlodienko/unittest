import re

def is_palindrome(string):
    #Set to low register and delete other unuseful symbols
    string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    #Return string and compare with original
    if (string == string[::-1 ]):
        return True

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("Hello, world!") == False
    assert is_palindrome("12321") == True
    assert is_palindrome("") == True

string = input("Input your palindrome:")
is_palindrome(string)