# Lexer for the RecSPL Language
import re
from src.utilities.xml_methods import tokens_to_xml

class Token:
    def __init__(self, token_type, token_value, token_class):
        self.token_type = token_type
        self.token_value = token_value
        self.token_class = token_class


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
            elif self.text[self.pos :].startswith("V_") or self.text[
                self.pos :
            ].startswith("F_"):
                token = self.user_defined()
                if token is None:
                    # An Error Has Occurred Here...
                    return None
                tokens.append(token)
            elif self.text[self.pos].isdigit() or self.text[self.pos] == "-":
                token = self.number()
                if token is None:
                    # An Error Has Occurred Here...
                    return None
                tokens.append(token)
            elif self.text[self.pos] == '"':
                token = self.string()
                if token is None:
                    # An Error Has Occurred Here...
                    return None
                tokens.append(token)
            else:
                token = self.keyword()
                if token is None:
                    # An Error Has Occurred Here...
                    return None
                tokens.append(token)
        return tokens

    def user_defined(self):
        start = self.pos
        while self.pos < len(self.text) and (
            self.text[self.pos].isalnum() or self.text[self.pos] == "_"
        ):
            self.pos += 1
        token_value = self.text[start : self.pos]

        if re.match(r"V_[a-z]([a-z]|[0-9])*$", token_value):
            return Token("VNAME", token_value, "V")
        elif re.match(r"F_[a-z]([a-z]|[0-9])*$", token_value):
            return Token("FNAME", token_value, "F")
        else:
            print(f"Error: Invalid User Defined Name '{token_value}'")
            return None

    def number(self):
        start = self.pos
        number_regex = r"^(0|0\.([0-9])*[1-9]|-0\.([0-9])*[1-9]|[1-9]([0-9])*|-[1-9]([0-9])*|[1-9]([0-9])*\.([0-9])*[1-9]|-[1-9]([0-9])*\.([0-9])*[1-9])$"

        # Moving to the end of the potential number
        while self.pos < len(self.text) and (
            self.text[self.pos].isdigit() or self.text[self.pos] in ".-"
        ):
            self.pos += 1

        token_value = self.text[start : self.pos]

        if re.match(number_regex, token_value):
            return Token("NUMBER", token_value, "N")
        else:
            print(f"Error: Invalid Number '{token_value}'")
            return None

    def string(self):
        start = self.pos
        # Skipping opening quote
        self.pos += 1
        while self.pos < len(self.text) and self.text[self.pos] != '"':
            self.pos += 1

        if self.pos >= len(self.text):
            print("Error: Unterminated String")
            return None

        # Including closing quote
        self.pos += 1
        token_value = self.text[start : self.pos]

        if re.match(r'^"[A-Z][a-z]{0,7}"$', token_value):
            # Removing quotes
            return Token("STRING", token_value, "T")
        else:
            print(f"Error: Invalid String '{token_value}'")
            return None

    def keyword(self):
        keywords = [
            "skip",
            "halt",
            "(",
            ")",
            ",",
            "not",
            "sqrt",
            "or",
            "and",
            "eq",
            "grt",
            "add",
            "sub",
            "mul",
            "div",
            "return",
            "{",
            "}",
            ";",
            "=",
            "<",
            "input",
            "main",
            "begin",
            "end",
            "if",
            "then",
            "else",
            "print",
            "num",
            "text",
            "void",
        ]

        for keyword in keywords:
            if self.text[self.pos :].startswith(keyword):
                self.pos += len(keyword)
                return Token("KEYWORD", keyword, "reserved_keyword")

        # Here, We Know the Input is not a KEYWORD
        print(f"Error: Invalid input '{self.text[self.pos]}'")
        return None

    def write_tokens_to_xml(self, filename):
        tokens = self.tokenize()

        if tokens is None:
            print("Lexing failed due to errors. XML file not generated.")
            return False
        else:
            tokens_to_xml(filename, tokens)
            print("Lexing Successful.")
            return True
