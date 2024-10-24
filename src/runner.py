from helpers.convert_to_dfa import convert_to_dfa
from helpers.lexing import lexing
from helpers.parsing import parsing
from helpers.analyser import analyser
from helpers.type_checker import check_types
from translator import generate_assembly

def runner(code_filename, lexer_filepath, parser_filepath, crawling_filepath, semantics_filepath):
    syntax_tree = None
    symbols = None

    LEXING_SUCCESSFUL = lexing(lexer_filepath, code_filename)
    if not LEXING_SUCCESSFUL:
        print(
            "\033[91mParsing Paused:  Please Fix Lexical Errors To Continue...\033[0m"
        )
        return False

    syntax_tree = parsing(lexer_filepath, parser_filepath)
    PARSING_SUCCESSFUL = (
        (syntax_tree != None) if LEXING_SUCCESSFUL else False
    )
    if not PARSING_SUCCESSFUL:
        if not LEXING_SUCCESSFUL:
            return False
        else:
            print(
                "\033[91mSemantic Analysis Paused:  Please Check for Syntax Errors...\033[0m"
            )
            return False

    symbols = analyser(parser_filepath, crawling_filepath, semantics_filepath)
    SEMANTICS_SUCCESSFUL = (
        (symbols != None)
        if PARSING_SUCCESSFUL
        else False
    )
    if not SEMANTICS_SUCCESSFUL:
        if not PARSING_SUCCESSFUL:
            return False
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
            return False
        else:
            print(
                "\033[91mType Checker Paused:  Please Check for Type Errors...\033[0m"
            )
    
    if (TYPE_SUCCESSFUL):
        print(generate_assembly(code_filename))
        print(
            "\033[92mTesting Complete!.\033[0m"
        )
    else:
        print(
            "\033[91mSome Tests Were Unsuccessful!.\033[0m"
        )
        return False

    return True
