from helpers.convert_to_dfa import convert_to_dfa
from helpers.lexing import lexing
from helpers.parsing import parsing
from helpers.analyser import analyser
from helpers.type_checker import check_types 

# from helpers.analyser import semantics

# Note 1 := The Source Code Should be witten in the file specifed in code_filename path file
# Note 2 := Replace Filename Bellow, Eg. out/lexer.xml
#        := This will attempt to store the XML file in out directory.

code_filename = "RecSPL.txt"

dfa_filepath = "out/dfa_output.txt"
lexer_filepath = "out/lexer.xml"
parser_filepath = "out/syntax_tree.xml"
crawling_filepath = "out/semantics_crawling_output.txt"
semantics_filepath = "out/semantics_sybols_output.txt"
syntax_tree = None
symbols = None

def test():
    LEXING_SUCCESSFUL = lexing(lexer_filepath, code_filename)
    if not LEXING_SUCCESSFUL:
        print(
            "\033[91mParsing Paused:  Please Fix Lexical Errors To Continue...\033[0m"
        )

    syntax_tree = parsing(lexer_filepath, parser_filepath)
    PARSING_SUCCESSFUL = (
        (syntax_tree != None) if LEXING_SUCCESSFUL else False
    )
    if not PARSING_SUCCESSFUL:
        if not LEXING_SUCCESSFUL:
            print()
        else:
            print(
                "\033[91mSemantic Analysis Paused:  Please Check for Syntax Errors...\033[0m"
            )

    symbols = analyser(parser_filepath, crawling_filepath, semantics_filepath)
    SEMANTICS_SUCCESSFUL = (
        (symbols != None)
        if PARSING_SUCCESSFUL
        else False
    )
    if not SEMANTICS_SUCCESSFUL:
        if not PARSING_SUCCESSFUL:
            print()
        else:
            print(
                "\033[91mType Checker Paused:  Please Check for Function & Variable Declaration Errors...\033[0m"
            )
    
    TYPE_SUCCESSFUL = (
        check_types(syntax_tree, symbols)
        if PARSING_SUCCESSFUL
        else False
    )
    if not TYPE_SUCCESSFUL:
        if not SEMANTICS_SUCCESSFUL:
            print()
        else:
            print(
                "\033[91mType Checker Paused:  Please Check for Type Errors...\033[0m"
            )
    
    if (TYPE_SUCCESSFUL):
        print(
            "\033[92mTesting Complete!.\033[0m"
        )
    else:
        print(
            "\033[91mSome Tests Were Unsuccessful!.\033[0m"
        )
    return True

test()
