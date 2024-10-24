from lexer import Lexer


def lexing(lexer_filepath, code_filename):
    print("\n--- Lexing The RecSPL Code ---")
    print("----------------------------------")

    # Insert Code Below for Testing The Lexer
    source_code = ""
    with open(code_filename, "r") as file:
        source_code = file.read()

    lexer = Lexer(source_code)

    result = lexer.write_tokens_to_xml(lexer_filepath)
    print("----------------------------------")

    return result
