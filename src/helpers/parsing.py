from parser import Parser
from utilities.xml_methods import (
    write_to_file,
    parse_xml_tokens,
    convert_syntax_tree_to_pretty_xml,
)

def parsing(lexer_filepath, parser_filepath):
    print("\n-- Parsing The RecSPL Code --")
    print("----------------------------------")

    tokens = parse_xml_tokens(lexer_filepath)
    parser = Parser(tokens)

    try:
        parser = Parser(tokens)
        syntax_tree = parser.parse()

        pretty_xml = convert_syntax_tree_to_pretty_xml(syntax_tree)
        write_to_file(pretty_xml, parser_filepath)

        print(f"Syntax Tree Generated and Saved to {parser_filepath}")
        print("\033[92mParsing successful.\033[0m")
        print("----------------------------------")

        return syntax_tree

    except SyntaxError as e:
        print(f"Parsing failed: {e}")
        print("----------------------------------")

        return None
