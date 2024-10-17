import pytest
from helpers.analyser import analyser

@pytest.mark.parametrize("file_number", range(1, 2))
def test_analyser_files_first(file_number):
    assert analyser(
            f"out/testing/tree/tree-{file_number}.xml",
            f"out/testing/semantics/crawling/crawl-{file_number}.txt",
            f"out/testing/semantics/symbols/symbols-{file_number}.txt"
        ) == True

@pytest.mark.parametrize("file_number", range(2, 21))
def test_analyser_files_2_to_20(file_number):
    assert analyser(
            f"out/testing/tree/tree-{file_number}.xml",
            f"out/testing/semantics/crawling/crawl-{file_number}.txt",
            f"out/testing/semantics/symbols/symbols-{file_number}.txt"
        ) == True, \
        f"Semantics Should Not Pass For Tree-{file_number}.xml"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
