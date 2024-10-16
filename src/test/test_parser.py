import pytest
from helpers.parsing import parsing

@pytest.mark.parametrize("file_number", range(1, 2))
def test_parsing_files_1_to_5(file_number):
    assert parsing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/tree/tree-{file_number}.xml") == True

@pytest.mark.parametrize("file_number", range(2, 21))
def test_parsing_files_6_to_20(file_number):
    assert parsing(f"out/testing/tokens/lexer-{file_number}.xml", f"out/testing/tree/tree-{file_number}.xml") == False, \
        f"Parsing Should Not Pass For lexer-{file_number}.xml"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
