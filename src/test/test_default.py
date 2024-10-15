import pytest
from helpers.lexing import lexing
from helpers.parsing import parsing

def test_pytest_is_working_1():
    assert True, "Pytest is working 1"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
