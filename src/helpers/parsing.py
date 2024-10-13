from parser import Parser
from utilities.xml_methods import (
    write_to_file,
    parse_xml_tokens,
    convert_syntax_tree_to_pretty_xml,
)

def parsing(lexer_filepath, parser_filepath):
    print("-- Parsing The RecSPL Code --")
    print("----------------------------------")

    tokens = parse_xml_tokens(lexer_filepath)
    parser = Parser(tokens)

    try:
        parser = Parser(tokens)
        syntax_tree = parser.parse()

        pretty_xml = convert_syntax_tree_to_pretty_xml(syntax_tree)
        write_to_file(pretty_xml, parser_filepath)

        print(f"Syntax Tree Generated and Saved to {parser_filepath}")
        print("Parsing successful.")
        print("----------------------------------\n\n")

        return True

    except SyntaxError as e:
        print(f"Parsing failed: {e}")
        print("----------------------------------\n\n")

        return False
