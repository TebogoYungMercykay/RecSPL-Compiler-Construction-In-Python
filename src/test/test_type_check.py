import pytest
from runner import runner

print("\033[94m\n==== TYPE CHECKER: TEST CASES USING PYTEST ====\n\033[0m")

def test_pytest_is_working_1():
    assert 1 + 1 == 2, "Default Test For Type Checker Is Working!"

@pytest.mark.parametrize("file_number", range(1, 11))
def test_type_check_files_1_to_10(file_number):
    code_filename = f"out/testing/typechecker/recspl/code-{file_number}.txt"
    lexer_filepath = f"out/testing/typechecker/tokens/lexer-{file_number}.xml"
    parser_filepath = f"out/testing/typechecker/tree/tree-{file_number}.xml"
    crawling_filepath = f"out/testing/typechecker/crawling/crawl-{file_number}.txt"
    semantics_filepath = f"out/testing/typechecker/symbols/symbols-{file_number}.txt"
    
    assert runner(code_filename, lexer_filepath, parser_filepath, crawling_filepath, semantics_filepath) == True, f"Type Checker ({file_number}): All Tests Must Pass for This Case."

@pytest.mark.parametrize("file_number", range(11, 21))
def test_type_check_files_11_to_20(file_number):
    code_filename = f"out/testing/typechecker/recspl/code-{file_number}.txt"
    lexer_filepath = f"out/testing/typechecker/tokens/lexer-{file_number}.xml"
    parser_filepath = f"out/testing/typechecker/tree/tree-{file_number}.xml"
    crawling_filepath = f"out/testing/typechecker/crawling/crawl-{file_number}.txt"
    semantics_filepath = f"out/testing/typechecker/symbols/symbols-{file_number}.txt"

    assert runner(code_filename, lexer_filepath, parser_filepath, crawling_filepath, semantics_filepath) == True, f"Type Checker ({file_number}): All Tests Should Fail For This Case."

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
