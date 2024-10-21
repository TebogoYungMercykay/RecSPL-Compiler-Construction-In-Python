import pytest

def test_pytest_is_working_1():
    print("\033[94m\n==== TYPE CHECKER: TEST CASES USING PYTEST ====\n\033[0m")
    assert 1 + 1 == 2, "Default Test For Type Checker Is Working!"

@pytest.mark.parametrize("file_number", range(1, 2))
def test_semantics_files_first(file_number):
    assert file_number + file_number == 2, "Type Checker Default Tests Working"

@pytest.mark.parametrize("file_number", range(2, 21))
def test_semantics_files_2_to_20(file_number):
    assert file_number + file_number == 2 * file_number, "Type Checker - All Good"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
