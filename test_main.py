import pytest
from main import PrintFibonacci, fibonacci


# First unit test
def test_fibonacci_0():
    assert (fibonacci(0) == [])


def test_fibonacci_1():
    assert (fibonacci(1) == [0])