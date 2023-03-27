def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(29) == True
    assert is_prime(31) == True
    assert is_prime(57) == False
    assert is_prime(100) == False
    assert is_prime(101) == True
    assert is_prime(997) == True
    assert is_prime(1000) == False


n = int(input("Write your simple number:"))
is_prime(n)