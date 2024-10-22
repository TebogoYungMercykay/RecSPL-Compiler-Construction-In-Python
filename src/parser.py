# Parser for the RecSPL Language
from helpers.syntax_tree import SyntaxTree

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = tokens[0] if tokens else None
        self.syntax_tree = SyntaxTree()

    def advance(self):
        """Advance to the next token."""
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None  # End of tokens

    def consume(self, expected_class, expected_word):
        """Consume the current token if it matches the expected class."""
        if (
            self.current_token
            and self.current_token["class"] == expected_class
            and self.current_token["word"] == expected_word
        ):
            token = self.current_token
            self.advance()
            return token
        else:
            if self.current_token is None:
                raise SyntaxError(
                    f"Unexpected End of InputStream, Expected token '{expected_word}'"
                )
            elif expected_word is not None and self.current_token["word"] is None:
                raise SyntaxError(f"Unexpected token: {expected_word}")
            elif expected_word is None and self.current_token["word"] is not None:
                raise SyntaxError(
                    f"Unexpected End of InputStream, Missing '{self.current_token['word']}' in input"
                )
            else:
                raise SyntaxError(
                    f"Expected {expected_word}, But got '{self.current_token['word']}'"
                )

    def parse(self):
        return self.parse_prog()

    def parse_prog(self):
        """Parses PROG -> main GLOBVARS ALGO FUNCTIONS"""
        root = self.add_token_as_root("reserved_keyword", "main")

        global_var_node = self.syntax_tree.add_inner_node(root, "GLOBVARS")
        self.parse_globvars(global_var_node)

        self.parse_algo(root)

        functions_node = self.syntax_tree.add_inner_node(root, "FUNCTIONS")
        self.parse_functions(functions_node)
        
        if (self.current_token != None):
            raise SyntaxError(
                f"Expected end of the Input, But got '{self.current_token['word']}'"
            )
        else:
            return self.syntax_tree

    def parse_globvars(self, parent_node):
        """Parses GLOBVARS -> ε | VTYP VNAME , GLOBVARS"""

        if self.current_token is not None and (
            self.current_token["word"] in ["num", "text"]
        ):
            self.parse_vtyp(parent_node)
            self.parse_vname(parent_node)
            self.add_token_as_leaf("reserved_keyword", ",", parent_node)

            self.parse_globvars(parent_node)
        else:
            # TODO: Ignore Epsilon Transitions
            self.add_empty_node(parent_node)
            # pass  # epsilon case

    def parse_vtyp(self, parent_node):
        """Parses VTYP -> num | text"""
        vtyp_node = self.syntax_tree.add_inner_node(parent_node, "VTYP")

        if self.current_token["word"] in ["num", "text"]:
            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], vtyp_node
            )
        else:
            raise SyntaxError(
                f"Variable Type: Expected a num or text, But got '{self.current_token['word']}'"
            )

    def parse_vname(self, parent_node):
        """Parses VNAME -> V"""
        vname_node = self.syntax_tree.add_inner_node(parent_node, "VNAME")

        if self.current_token["class"] == "V":
            self.add_token_as_leaf("V", self.current_token["word"], vname_node)
        else:
            raise SyntaxError(
                f"Variable Name: Expected a VNAME (V), But got '{self.current_token['word']}'"
            )

    def parse_algo(self, parent_node):
        """Parses ALGO -> begin INSTRUC end"""
        algo_node = self.syntax_tree.add_inner_node(parent_node, "ALGO")
        self.add_token_as_leaf("reserved_keyword", "begin", algo_node)

        instruc_node = self.syntax_tree.add_inner_node(algo_node, "INSTRUC")
        self.parse_instruc(instruc_node)

        self.add_token_as_leaf("reserved_keyword", "end", algo_node)

    def parse_instruc(self, parent_node):
        """Parses INSTRUC -> ε | COMMAND ; INSTRUC"""

        if self.current_token is not None and (self.current_token["word"] != "end"):
            self.parse_command(parent_node)
            self.add_token_as_leaf("reserved_keyword", ";", parent_node)
            self.parse_instruc(parent_node)
        else:
            # TODO: Ignore Epsilon Transitions
            self.add_empty_node(parent_node)
            # pass  # epsilon case

    def parse_command(self, parent_node):
        """Parses COMMAND -> skip | halt | print ATOMIC | return ATOMIC | ASSIGN | CALL | BRANCH"""
        command_node = self.syntax_tree.add_inner_node(parent_node, "COMMAND")

        token = self.current_token["word"]
        if token == "skip":
            self.add_token_as_leaf("reserved_keyword", "skip", command_node)
        elif token == "halt":
            self.add_token_as_leaf("reserved_keyword", "halt", command_node)
        elif token == "print":
            self.add_token_as_leaf("reserved_keyword", "print", command_node)
            self.parse_atomic(command_node)
        elif token == "return":
            self.add_token_as_leaf("reserved_keyword", "return", command_node)
            self.parse_atomic(command_node)
        elif self.current_token["class"] == "V":
            self.parse_assign(command_node)
        elif self.current_token["class"] == "F":
            self.parse_call(command_node)
        elif token == "if":
            self.parse_branch(command_node)
        else:
            raise SyntaxError(f"Command: Unexpected Command Token: '{token}'")

    def parse_atomic(self, parent_node):
        """Parses ATOMIC -> VNAME | CONST"""
        atomic_node = self.syntax_tree.add_inner_node(parent_node, "ATOMIC")

        token = self.current_token["class"]
        if token == "V":
            self.parse_vname(atomic_node)
        elif token in ["N", "T"]:
            self.parse_const(atomic_node)
        else:
            raise SyntaxError(
                f"Atomic: Expected an ATOMIC, But got '{self.current_token['word']}'"
            )
    
    def parse_const(self, parent_node):
        """Parses CONST -> N | T"""
        const_node = self.syntax_tree.add_inner_node(parent_node, "CONST")

        if self.current_token["class"] in ["N", "T"]:
            self.add_token_as_leaf(
                self.current_token["class"], self.current_token["word"], const_node
            )
        else:
            raise SyntaxError(
                f"Constant: Expected a CONST (N or T), But got '{self.current_token['word']}'"
            )

    def parse_assign(self, parent_node):
        """Parses ASSIGN -> VNAME < input | VNAME = TERM"""
        assign_node = self.syntax_tree.add_inner_node(parent_node, "ASSIGN")

        self.parse_vname(assign_node)
        if self.current_token["word"] == "<":
            self.add_token_as_leaf("reserved_keyword", "<", assign_node)
            self.add_token_as_leaf("reserved_keyword", "input", assign_node)
        elif self.current_token["word"] == "=":
            self.add_token_as_leaf("reserved_keyword", "=", assign_node)
            self.parse_term(assign_node)
        else:
            raise SyntaxError(
                f"Assignment: Expected < or =, But got '{self.current_token['word']}'"
            )

    def parse_call(self, parent_node):
        """Parses CALL -> FNAME( ATOMIC , ATOMIC , ATOMIC )"""
        call_node = self.syntax_tree.add_inner_node(parent_node, "CALL")

        self.parse_fname(call_node)
        self.add_token_as_leaf("reserved_keyword", "(", call_node)
        self.parse_atomic(call_node)
        self.add_token_as_leaf("reserved_keyword", ",", call_node)
        self.parse_atomic(call_node)
        self.add_token_as_leaf("reserved_keyword", ",", call_node)
        self.parse_atomic(call_node)
        self.add_token_as_leaf("reserved_keyword", ")", call_node)

    def parse_branch(self, parent_node):
        """Parses BRANCH -> if COND then ALGO else ALGO"""
        branch_node = self.syntax_tree.add_inner_node(parent_node, "BRANCH")

        self.add_token_as_leaf("reserved_keyword", "if", branch_node)
        self.parse_cond(branch_node)
        self.add_token_as_leaf("reserved_keyword", "then", branch_node)
        self.parse_algo(branch_node)
        self.add_token_as_leaf("reserved_keyword", "else", branch_node)
        self.parse_algo(branch_node)

    def parse_term(self, parent_node):
        """Parses TERM -> ATOMIC | CALL | OP"""
        term_node = self.syntax_tree.add_inner_node(parent_node, "TERM")

        if self.current_token["class"] in ["V", "N", "T"]:
            self.parse_atomic(term_node)
        elif self.current_token["class"] == "F":
            self.parse_call(term_node)
        elif self.current_token["word"] in [
            "add",
            "sub",
            "mul",
            "div",
            "grt",
            "eq",
            "not",
            "sqrt",
            "or",
        ]:
            op_node = self.syntax_tree.add_inner_node(term_node, "OP")
            self.parse_op(op_node)
        else:
            raise SyntaxError(
                f"Term: Unexpected Token in TERM: '{self.current_token['word']}'"
            )

    def parse_op(self, parent_node):
        """Parses OP -> UNOP ( ARG ) | BINOP ( ARG , ARG )"""

        if self.current_token["word"] in [
            "add",
            "sub",
            "mul",
            "div",
            "grt",
            "eq",
            "or",
        ]:
            op_node = self.syntax_tree.add_inner_node(parent_node, "BINOP")

            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], op_node
            )
            self.add_token_as_leaf("reserved_keyword", "(", op_node)
            self.parse_arg(op_node)
            self.add_token_as_leaf("reserved_keyword", ",", op_node)
            self.parse_arg(op_node)
            self.add_token_as_leaf("reserved_keyword", ")", op_node)
        elif self.current_token["word"] in ["not", "sqrt"]:
            op_node = self.syntax_tree.add_inner_node(parent_node, "UNOP")

            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], op_node
            )
            self.add_token_as_leaf("reserved_keyword", "(", op_node)
            self.parse_arg(op_node)
            self.add_token_as_leaf("reserved_keyword", ")", op_node)
        else:
            raise SyntaxError(
                f"Operator: Unexpected Operator Token: '{self.current_token['word']}'"
            )

    def parse_arg(self, parent_node):
        """Parses ARG -> ATOMIC | OP"""
        arg_node = self.syntax_tree.add_inner_node(parent_node, "ARG")

        if self.current_token["class"] in ["V", "N", "T"]:
            self.parse_atomic(arg_node)
        elif self.current_token["word"] in [
            "add",
            "sub",
            "mul",
            "div",
            "grt",
            "eq",
            "not",
            "sqrt",
            "or",
        ]:
            op_node = self.syntax_tree.add_inner_node(arg_node, "OP")
            self.parse_op(op_node)
        else:
            raise SyntaxError(
                f"Argument: Expected an ARG, But got '{self.current_token['word']}'"
            )

    def parse_cond(self, parent_node):
        """Parses COND -> SIMPLE | COMPOSIT"""
        cond_node = self.syntax_tree.add_inner_node(parent_node, "COND")
        op_lists = [["N", "T", "V"], ["add", "sub", "mul", "div", "grt", "eq", "or"]]
        vals = [
            self.current_token_index + 2,
            self.current_token_index + 4,
            self.current_token_index + 9,
        ]

        if self.current_token is None:
            raise SyntaxError("Condition: Unexpected end of input in COND")

        # Checking if current token is a valid operator
        if self.current_token["word"] in op_lists[1]:
            if len(self.tokens) > vals[0] and vals[1] < len(self.tokens):
                if (self.tokens[vals[0]])["class"] in op_lists[0] and (
                    self.tokens[vals[1]]
                )["class"] in op_lists[0]:
                    self.parse_simple(cond_node)
                elif ((self.tokens[vals[0]])["word"] in op_lists[1]) and (
                    (vals[2] < len(self.tokens))
                    and (self.tokens[vals[2]])["word"] in op_lists[1]
                ):
                    self.parse_composit(cond_node)
                else:
                    raise SyntaxError(
                        "Condition: Invalid Input Combination for BINOP in COND"
                    )
            else:
                raise SyntaxError("Condition: Invalid BINOP input in COND")
        elif self.current_token["word"] in ["not", "sqrt"]:
            if len(self.tokens) > vals[0]:
                self.parse_composit(cond_node)
            else:
                raise SyntaxError("Condition: Invalid UNOP input in COND")
        else:
            raise SyntaxError(
                f"Condition: Expected SIMPLE or COMPOSIT, got '{self.current_token['word']}'"
            )

    def parse_simple(self, parent_node):
        """Parses SIMPLE -> BINOP ( ATOMIC , ATOMIC ) | COMPOSIT"""
        simple_node = self.syntax_tree.add_inner_node(parent_node, "SIMPLE")

        if self.current_token["word"] in self.binops():
            op_node = self.syntax_tree.add_inner_node(simple_node, "BINOP")

            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], op_node
            )
            self.add_token_as_leaf("reserved_keyword", "(", op_node)
            self.parse_atomic(op_node)
            self.add_token_as_leaf("reserved_keyword", ",", op_node)
            self.parse_atomic(op_node)
            self.add_token_as_leaf("reserved_keyword", ")", op_node)
        elif self.current_token["word"] in self.unops():
            self.parse_composit(simple_node)
        else:
            raise SyntaxError(
                f"Simple: Expected BINOP or COMPOSIT, got '{self.current_token['word']}'"
            )

    def parse_composit(self, parent_node):
        """Parses COMPOSIT -> BINOP ( SIMPLE , SIMPLE ) | UNOP ( SIMPLE )"""
        composit_node = self.syntax_tree.add_inner_node(parent_node, "COMPOSIT")

        if self.current_token["word"] in self.binops():
            op_node = self.syntax_tree.add_inner_node(composit_node, "BINOP")

            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], op_node
            )
            self.add_token_as_leaf("reserved_keyword", "(", op_node)
            self.parse_simple(op_node)
            self.add_token_as_leaf("reserved_keyword", ",", op_node)
            self.parse_simple(op_node)
            self.add_token_as_leaf("reserved_keyword", ")", op_node)
        elif self.current_token["word"] in self.unops():
            op_node = self.syntax_tree.add_inner_node(composit_node, "UNOP")

            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], op_node
            )
            self.add_token_as_leaf("reserved_keyword", "(", op_node)
            self.parse_simple(op_node)
            self.add_token_as_leaf("reserved_keyword", ")", op_node)
        else:
            raise SyntaxError(
                f"Composit: Expected BINOP or UNOP, got '{self.current_token['word']}'"
            )

    def binops(self):
        """Parses BINOP -> (add | sub | mul | div | grt | eq | or)"""
        return [
            "add",
            "sub",
            "mul",
            "div",
            "grt",
            "eq",
            "or",
        ]

    def unops(self):
        """Parses UNOP -> (sqrt | not)"""
        return ["sqrt", "not"]

    def parse_fname(self, parent_node):
        """Parses FNAME -> F"""
        fname_node = self.syntax_tree.add_inner_node(parent_node, "FNAME")

        if self.current_token["class"] == "F":
            self.add_token_as_leaf("F", self.current_token["word"], fname_node)
        else:
            raise SyntaxError(
                f"Function Name: Expected a FNAME (F), But got '{self.current_token['word']}'"
            )

    def parse_functions(self, parent_node):
        """Parses FUNCTIONS -> ε | FUNCTION FUNCTIONS"""

        if self.current_token is not None and (
            self.current_token["word"] == "num" or self.current_token["word"] == "void"
        ):
            self.parse_declaration(parent_node)
            self.parse_functions(parent_node)
        else:
            # TODO: Ignore Epsilon Transitions
            self.add_empty_node(parent_node)
            # pass  # epsilon case

    def parse_declaration(self, parent_node):
        """Parses DECL -> HEADER BODY"""
        declaration_node = self.syntax_tree.add_inner_node(parent_node, "DECL")

        self.parse_header(declaration_node)
        self.parse_body(declaration_node)

    def parse_header(self, parent_node):
        """Parses HEADER -> FTYP FNAME ( VNAME , VNAME , VNAME )"""
        header_node = self.syntax_tree.add_inner_node(parent_node, "HEADER")

        self.parse_ftyp(header_node)
        self.parse_fname(header_node)
        self.add_token_as_leaf("reserved_keyword", "(", header_node)
        self.parse_vname(header_node)
        self.add_token_as_leaf("reserved_keyword", ",", header_node)
        self.parse_vname(header_node)
        self.add_token_as_leaf("reserved_keyword", ",", header_node)
        self.parse_vname(header_node)
        self.add_token_as_leaf("reserved_keyword", ")", header_node)

    def parse_ftyp(self, parent_node):
        """Parses FTYP -> num | void"""
        ftyp_node = self.syntax_tree.add_inner_node(parent_node, "FTYP")

        if self.current_token["word"] in ["num", "void"]:
            self.add_token_as_leaf(
                "reserved_keyword", self.current_token["word"], ftyp_node
            )
        else:
            raise SyntaxError(
                f"Funtion Type: Expected num or void, But got '{self.current_token['word']}'"
            )

    def parse_body(self, parent_node):
        """Parses BODY -> PROLOG LOCVARS ALGO EPILOG SUBFUNCS end"""
        body_node = self.syntax_tree.add_inner_node(parent_node, "BODY")

        self.add_token_as_leaf("reserved_keyword", "{", body_node)
        self.parse_locvars(body_node)
        self.parse_algo(body_node)
        self.add_token_as_leaf("reserved_keyword", "}", body_node)

        functions_node = self.syntax_tree.add_inner_node(body_node, "FUNCTIONS")
        self.parse_functions(functions_node)

        self.add_token_as_leaf("reserved_keyword", "end", body_node)

    def parse_locvars(self, parent_node):
        """Parses LOCVARS -> VTYP VNAME , VTYP VNAME , VTYP VNAME ,"""
        locvars_node = self.syntax_tree.add_inner_node(parent_node, "LOCVARS")

        var_count = 0
        while True:
            self.parse_vtyp(locvars_node)
            self.parse_vname(locvars_node)
            self.add_token_as_leaf("reserved_keyword", ",", locvars_node)
            var_count += 1
            if var_count < 3:
                if self.current_token["word"] not in ["text", "num"]:
                    raise SyntaxError(
                        f"Local Vaiables: Expected exactly 3 variables, but got less than {var_count}"
                    )
            elif var_count >= 3:
                if self.current_token["word"] in ["text", "num"]:
                    raise SyntaxError(
                        f"Local Vaiables: Expected exactly 3 variables, but got more than {var_count}"
                    )
                break

    def add_token_as_leaf(self, expected_class, expected_word, parent_node):
        """Add the current token as a leaf node in the syntax tree."""
        token = self.consume(expected_class, expected_word)
        self.syntax_tree.add_leaf_node(parent_node, token)

    def add_token_as_root(self, expected_class, expected_word):
        """Add the current token as a leaf node in the syntax tree."""
        self.consume(expected_class, expected_word)
        root = self.syntax_tree.add_root(expected_word)

        return root

    def add_empty_node(self, parent_node):
        """Empty node to represent epsilon transitions"""
        self.syntax_tree.add_inner_node(parent_node, "ε")
