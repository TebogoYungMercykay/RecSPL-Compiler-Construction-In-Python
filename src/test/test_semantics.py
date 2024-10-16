import pytest

def test_pytest_is_working_1():
    assert 1 + 1 == 2, "Semantics Default Tests Working"

def test_semantics_from_files():
    assert 1 + 1 == 2, "Semantics - All Good"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
