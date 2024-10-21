import pytest

def test_pytest_is_working_1():
    print("\033[94m\n==== DEFAULT PYTEST ====\n\033[0m")
    assert 1 + 1 == 2, "Pytest is Working!"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
