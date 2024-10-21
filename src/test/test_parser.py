import pytest
from helpers.parsing import parsing

def test_pytest_is_working_1():
    print("\033[94m\n==== PARSER: TEST CASES USING PYTEST ====\n\033[0m")
    assert 1 + 1 == 2, "Default Test For Parser Is Working!"

@pytest.mark.parametrize("file_number", range(1, 2))
def test_parsing_files_first(file_number):
    assert parsing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/tree/tree-{file_number}.xml") == True

@pytest.mark.parametrize("file_number", range(2, 21))
def test_parsing_files_2_to_20(file_number):
    assert parsing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/tree/tree-{file_number}.xml") == False, \
        f"Parsing Should Not Pass For lexer-{file_number}.xml"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
