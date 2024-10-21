import pytest
from helpers.lexing import lexing

def test_pytest_is_working_1():
    print("\033[94m\n==== LEXER: TEST CASES USING PYTEST ====\n\033[0m")
    assert 1 + 1 == 2, "Default Test For Lexer Is Working!"

@pytest.mark.parametrize("file_number", range(1, 6))
def test_lexing_files_1_to_5(file_number):
    assert lexing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/recspl/code-{file_number}.txt") == True

@pytest.mark.parametrize("file_number", range(6, 21))
def test_lexing_files_6_to_20(file_number):
    assert lexing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/recspl/code-{file_number}.txt") == False, \
        f"Lexing Should Not Pass For this RecSPL code-{file_number}.txt"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
