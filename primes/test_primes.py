
from primes import Primes

def func(number):
    return number + 1


def test_returns_empty_list_for_numbers_below_2():
    primes = Primes()
    assert primes.factorsOf(1) == []


