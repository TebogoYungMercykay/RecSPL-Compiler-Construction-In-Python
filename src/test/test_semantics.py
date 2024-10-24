import pytest
from helpers.analyser import analyser
# from helpers.lexing import lexing
# from helpers.parsing import parsing

print("\033[94m\n==== SEMANTICS: TEST CASES USING PYTEST ====\n\033[0m")

def test_pytest_is_working_1():
    assert 1 + 1 == 2, "Default Test For Semantics Is Working!"

# @pytest.mark.parametrize("file_number", range(1, 21))
# def test_lexing_files_1_to_20(file_number):
#     assert lexing(f"out/testing/semantics/tokens/lexer-{file_number}.xml", f"out/testing/semantics/recspl/code-{file_number}.txt") == True

# @pytest.mark.parametrize("file_number", range(1, 21))
# def test_parsing_files_1_to_20(file_number):
#     assert parsing(f"out/testing/semantics/tokens/lexer-{file_number}.xml", f"out/testing/semantics/tree/tree-{file_number}.xml") != None

# Testing Functions
@pytest.mark.parametrize("file_number", range(1, 6))
def test_analyser_files_1_to_5(file_number):
    assert analyser(
            f"out/testing/semantics/tree/tree-{file_number}.xml",
            f"out/testing/semantics/crawling/crawl-{file_number}.txt",
            f"out/testing/semantics/symbols/symbols-{file_number}.txt"
        ) != None, \
        f"Semantics Should Pass For Tree-{file_number}.xml"

@pytest.mark.parametrize("file_number", range(6, 11))
def test_analyser_files_6_to_10(file_number):
    assert analyser(
            f"out/testing/semantics/tree/tree-{file_number}.xml",
            f"out/testing/semantics/crawling/crawl-{file_number}.txt",
            f"out/testing/semantics/symbols/symbols-{file_number}.txt"
        ) == None, \
        f"Semantics Should Not Pass For Tree-{file_number}.xml"

# Testing Variables
@pytest.mark.parametrize("file_number", range(11, 16))
def test_analyser_files_11_to_15(file_number):
    assert analyser(
            f"out/testing/semantics/tree/tree-{file_number}.xml",
            f"out/testing/semantics/crawling/crawl-{file_number}.txt",
            f"out/testing/semantics/symbols/symbols-{file_number}.txt"
        ) == None, \
        f"Semantics Should Pass For Tree-{file_number}.xml"

@pytest.mark.parametrize("file_number", range(16, 21))
def test_analyser_files_16_to_20(file_number):
    assert analyser(
            f"out/testing/semantics/tree/tree-{file_number}.xml",
            f"out/testing/semantics/crawling/crawl-{file_number}.txt",
            f"out/testing/semantics/symbols/symbols-{file_number}.txt"
        ) == None, \
        f"Semantics Should Not Pass For Tree-{file_number}.xml"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
