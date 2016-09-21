
from .primes import Primes



primes = Primes()

def factorsOf(number):
    return primes.factorsOf(number)

def test_returns_empty_list_for_numbers_below_2():
    assert factorsOf(0) == []
    assert factorsOf(1) == []


def test_returns_prime_number_wrapped_in_list_for_primes():
    assert factorsOf(2) == [2]
    assert factorsOf(3) == [3]
    assert factorsOf(7) == [7]
    assert factorsOf(17) == [17]

def test_factors_are_repeated_as_many_times_as_the_number_is_divisible():
    assert factorsOf(4) == [2, 2]
    assert factorsOf(8) == [2, 2, 2]
    assert factorsOf(9) == [3, 3]
    assert factorsOf(25) == [5, 5]
    
