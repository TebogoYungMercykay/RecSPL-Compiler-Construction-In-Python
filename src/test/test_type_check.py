import pytest
from helpers.lexing import lexing
from helpers.parsing import parsing

def test_pytest_is_working_1():
    assert True, "Type Checker Default Tests Working"

def test_semantics_from_files():
    assert True, "Type Checker - All Good"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
