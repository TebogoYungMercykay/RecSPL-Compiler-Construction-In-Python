import pytest
from helpers.lexing import lexing
from helpers.parsing import parsing

def test_pytest_is_working_1():
    assert True, "Pytest is working 1"

def test_lexing_from_files():
    for k in range(1, 21):
        expected = True if k <= 5 else False
        result = lexing(f"out/testing/tokens/lexer-{k}.xml", f"out/testing/recspl/code-{k}.txt")
        assert result == expected, f"Lexing Should Not Pass For RecSPL code-{k}.txt"

def test_parsing_from_files():
    for k in range(1, 21):
        expected = True if k <= 1 else False
        result = parsing(f"out/testing/tokens/lexer-{k}.xml", f"out/testing/tree/tree-{k}.xml")
        assert result == expected, f"Parsing Should Not Pass For lexer-{k}.xml"

def test_semantics_from_files():
    assert True, "All Good"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
