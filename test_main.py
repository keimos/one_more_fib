import pytest
from main import print_fibonacci

def test_print_fibonacci_length_zero(capsys):
    """Test with length = 0 (invalid case)."""
    print_fibonacci(0)
    captured = capsys.readouterr()
    assert "Length" in captured.out

def test_print_fibonacci_length_one(capsys):
    """Test with length = 1."""
    print_fibonacci(1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "0 1"

def test_print_fibonacci_length_five(capsys):
    """Test with a length of 5."""
    print_fibonacci(5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "0 1 1 2 3"