
from primes import Primes

def func(number):
    return number + 1


primes = Primes()

def test_returns_empty_list_for_numbers_below_2():
    assert primes.factorsOf(0) == []
    assert primes.factorsOf(1) == []


def test_returns_prime_number_wrapped_in_list_for_primes():
    assert primes.factorsOf(2) == [2]
    assert primes.factorsOf(3) == [3]

