import pytest
from helpers.lexing import lexing

@pytest.mark.parametrize("file_number", range(1, 5))
def test_lexing_files_1_to_5(file_number):
    assert lexing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/recspl/code-{file_number}.txt") == True

@pytest.mark.parametrize("file_number", range(6, 21))
def test_lexing_files_6_to_20(file_number):
    assert lexing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/recspl/code-{file_number}.txt") == False, \
        f"Lexing Should Not Pass For RecSPL code-{file_number}.txt"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
