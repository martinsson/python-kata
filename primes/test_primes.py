
from primes import Primes

def primesFor(number):
    return Primes().forNumber(number)

def commented_test_acceptance():
    assert primesFor(2 * 3 * 5 * 7 * 19 * 19) == [2, 3, 5, 7, 19, 19]

def test_returns_empty_list_for_numbers_below_2():
    assert primesFor(1) == []
    assert primesFor(0) == []
    
def test_for_primes_returns_prime_wrapped_in_list():
    assert primesFor(2) == [2]
    assert primesFor(3) == [3]
    
# def test_for_4_returns_a_list_of_2_2s():
#     assert primesFor(4)== [2, 2]
    




