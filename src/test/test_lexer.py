import pytest
from helpers.lexing import lexing
from helpers.parsing import parsing

def test_pytest_is_working_1():
    assert True, "Lexer Default Tests Working"

def test_lexing_from_files():
    for k in range(1, 21):
        expected = True if k <= 5 else False
        result = lexing(f"out/testing/tokens/lexer-{k}.xml", f"out/testing/recspl/code-{k}.txt")
        assert result == expected, f"Lexing Should Not Pass For RecSPL code-{k}.txt"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
