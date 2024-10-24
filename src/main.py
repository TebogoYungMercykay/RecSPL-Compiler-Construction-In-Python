from runner import runner

def single(
    code_filename,
    lexer_filepath = "output/lexer.xml",
    parser_filepath = "output/syntax_tree.xml",
    crawling_filepath = "output/semantics_crawling_output.txt",
    semantics_filepath = "output/semantics_symbols_output.txt",
):
    print(f"\033[94m===== START ({code_filename}) =====\033[0m")
    
    result = runner(code_filename, lexer_filepath, parser_filepath, crawling_filepath, semantics_filepath)
    
    print(f"\033[94m===== DONE ({result == True}) =====\n\n\033[0m")

def bulk(list_files=[]):
    for i, files in enumerate(list_files):
        print(f"\033[94m===== START ({files['code_filename']}) =====\033[0m")

        result = runner(files['code_filename'], files['lexer_filepath'], files['parser_filepath'], files['crawling_filepath'], files['semantics_filepath'])
        
        print(f"\033[94m===== DONE ({result == True}) =====\n\n\033[0m")
        
        if not result:
            if (i >= 15):
                print(f"Test ({i}) Case Works")
            elif not result:
                break

# TODO: Replace Filename with Appropriate Filename/Path
code_filename = "RecSPL.txt"
lexer_filepath = "output/lexer.xml"
parser_filepath = "output/syntax_tree.xml"
crawling_filepath = "output/semantics_crawling_output.txt"
semantics_filepath = "output/semantics_symbols_output.txt"

single(code_filename, lexer_filepath, parser_filepath, crawling_filepath, semantics_filepath)

# L = []
# for k in range(1, 21):
#     file_paths = {
#         # TODO: Replace code_filename
#         "code_filename": f"out/testing/typechecker/recspl/code-{k}.txt",
#         "lexer_filepath": f"output/tokens/lexer-{k}.xml",
#         "parser_filepath": f"output/tree/tree-{k}.xml",
#         "crawling_filepath": f"output/crawling/crawl-{k}.txt",
#         "semantics_filepath": f"output/symbols/symbols-{k}.txt"
#     }
#     L.append(file_paths)

# bulk(L)

