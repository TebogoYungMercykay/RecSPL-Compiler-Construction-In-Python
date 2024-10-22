class SymbolTableEntry:
    def __init__(self, type):
        self.type = type

class SyntaxTreeNode:
    def __init__(self, type, value=None, children=[]):
        self.type = type
        self.value = value
        self.children = children

def typecheck(node):
    if node.type == "PROG":
        return typecheck_prog(node)
    elif node.type == "GLOBVARS":
        return typecheck_globvars(node)
    elif node.type == "ALGO":
        return typecheck_algo(node)
    elif node.type == "INSTRUC":
        return typecheck_instruc(node)
    elif node.type == "COMMAND":
        return typecheck_command(node)
    elif node.type == "ATOMIC":
        return typecheck_atomic(node)
    elif node.type == "ASSIGN":
        return typecheck_assign(node)
    elif node.type == "CALL":
        return typecheck_call(node)
    elif node.type == "OP":
        return typecheck_op(node)
    elif node.type == "ARG":
        return typecheck_arg(node)
    elif node.type == "UNOP":
        return typecheck_unop(node)
    elif node.type == "BINOP":
        return typecheck_binop(node)
    elif node.type == "BRANCH":
        return typecheck_branch(node)
    elif node.type == "COND":
        return typecheck_cond(node)
    elif node.type == "SIMPLE":
        return typecheck_simple(node)
    elif node.type == "COMPOSIT":
        return typecheck_composit(node)
    elif node.type == "FNAME":
        return typecheck_fname(node)
    elif node.type == "FUNCTIONS":
        return typecheck_functions(node)
    elif node.type == "DECL":
        return typecheck_decl(node)
    elif node.type == "HEADER":
        return typecheck_header(node)
    elif node.type == "FTYP":
        return typecheck_ftyp(node)
    elif node.type == "BODY":
        return typecheck_body(node)
    elif node.type == "PROLOG":
        return typecheck_prolog(node)
    elif node.type == "EPILOG":
        return typecheck_epilog(node)
    elif node.type == "LOCVARS":
        return typecheck_locvars(node)
    elif node.type == "SUBFUNCS":
        return typecheck_subfuncs(node)
    else:
        raise TypeError("Unknown node type: {}".format(node.type))

def typecheck_prog(node):
    if len(node.children) != 4 or node.children[0].type != "main":
        raise TypeError("Invalid PROG structure")
    return (
        typecheck(node.children[1])
        and typecheck(node.children[2])
        and typecheck(node.children[3])
    )

def typecheck_globvars(node):
    if node.type == "epsilon":
        return True
    if len(node.children) % 2 != 0:
        raise TypeError("Invalid GLOBVARS structure")
    for i in range(0, len(node.children), 2):
        if node.children[i].type != "VTYP":
            raise TypeError("Invalid GLOBVARS structure")
        if node.children[i + 1].type != "VNAME":
            raise TypeError("Invalid GLOBVARS structure")
        symbol_table[node.children[i + 1].value] = SymbolTableEntry(node.children[i].value)
    return typecheck_globvars(node.children[-1])

def typecheck_algo(node):
    if len(node.children) != 3 or node.children[0].type != "begin" or node.children[2].type != "end":
        raise TypeError("Invalid ALGO structure")
    return typecheck(node.children[1])

def typecheck_instruc(node):
    if node.type == "epsilon":
        return True
    if len(node.children) != 2 or node.children[1].type != "INSTRUC":
        raise TypeError("Invalid INSTRUC structure")
    return (
        typecheck(node.children[0]) and typecheck(node.children[1])
    )

def typecheck_command(node):
    if node.type == "skip":
        return True
    elif node.type == "halt":
        return True
    elif node.type == "print":
        return typecheck_atomic(node.children[0]) in ("n", "t")
    elif node.type == "return":
        # Implement tree-crawling to check return type consistency
        return True
    elif node.type == "ASSIGN":
        return typecheck_assign(node)
    elif node.type == "CALL":
        return typecheck_call(node)
    elif node.type == "BRANCH":
        return typecheck_branch(node)
    else:
        raise TypeError("Unknown command type: {}".format(node.type))

def typecheck_atomic(node):
    if node.type == "VNAME":
        return symbol_table[node.value].type
    elif node.type == "CONST":
        return node.value.type
    else:
        raise TypeError("Invalid ATOMIC structure")

def typecheck_assign(node):
    if len(node.children) != 2 or node.children[0].type != "VNAME" or node.children[1].type != "TERM":
        raise TypeError("Invalid ASSIGN structure")
    return typecheck_atomic(node.children[0]) == typecheck(node.children[1])

def typecheck_call(node):
    if len(node.children) != 4 or node.children[0].type != "FNAME":
        raise TypeError("Invalid CALL structure")
    for child in node.children[1:4]:
        if typecheck_atomic(child) != "n":
            raise TypeError("Function arguments must be numeric")
    return symbol_table[node.children[0].value].type

def typecheck_op(node):
    if node.type == "UNOP":
        return typecheck_unop(node)
    elif node.type == "BINOP":
        return typecheck_binop(node)
    else:
        raise TypeError("Invalid OP structure")

def typecheck_arg(node):
    return typecheck(node.children[0])

def typecheck_unop(node):
    if len(node.children) != 1:
        raise TypeError("Invalid UNOP structure")
    if node.value == "not":
        return "b"
    elif node.value == "sqrt":
        return "n"
    else:
        raise TypeError("Unknown UNOP: {}".format(node.value))

def typecheck_binop(node):
    if len(node.children) != 2:
        raise TypeError("Invalid BINOP structure")
    type1 = typecheck(node.children[0])
    type2 = typecheck(node.children[1])
    if node.value in ("or", "and"):
        return "b" if type1 == type2 == "b" else "u"
    elif node.value in ("eq", "grt"):
        return "b" if type1 == type2 == "n" else "u"
    elif node.value in ("add", "sub", "mul", "div"):
        return "n" if type1 == type2 == "n" else "u"
    else:
        raise TypeError("Unknown BINOP: {}".format(node.value))

def typecheck_branch(node):
    if len(node.children) != 4 or node.children[1].type != "then" or node.children[3].type != "else":
        raise TypeError("Invalid BRANCH structure")
    return (
        typecheck_cond(node.children[0]) == "b"
        and typecheck(node.children[2])
        and typecheck(node.children[4])
    )

def typecheck_cond(node):
    if node.type == "SIMPLE":
        return typecheck_simple(node)
    elif node.type == "COMPOSIT":
        return typecheck_composit(node)
    else:
        raise TypeError("Invalid COND structure")

def typecheck_simple(node):
    if len(node.children) != 2 or node.children[0].type != "BINOP":
        raise TypeError("Invalid SIMPLE structure")
    return typecheck_binop(node.children[0])

def typecheck_composit(node):
    if node.children[0].type == "BINOP":
        return typecheck_binop(node.children[0])
    elif node.children[0].type == "UNOP":
        return typecheck_unop(node.children[0])
    else:
        raise TypeError("Invalid COMPOSIT structure")

def typecheck_fname(node):
    return symbol_table[node.value].type

def typecheck_functions(node):
    if node.type == "epsilon":
        return True
    if len(node.children) != 2 or node.children[1].type != "FUNCTIONS":
        raise TypeError("Invalid FUNCTIONS structure")
    return (
        typecheck(node.children[0]) and typecheck(node.children[1])
    )

def typecheck_decl(node):
    if len(node.children) != 2 or node.children[0].type != "HEADER" or node.children[1].type != "BODY":
        raise TypeError("Invalid DECL structure")
    return (
        typecheck(node.children[0]) and typecheck(node.children[1])
    )

def typecheck_header(node):
    if len(node.children) != 4 or node.children[0].type != "FTYP" or node.children[1].type != "FNAME":
        raise TypeError("Invalid HEADER structure")
    for child in node.children[2:5]:
        if typecheck_atomic(child) != "n":
            raise TypeError("Function arguments must be numeric")
    return (
        symbol_table[node.children[1].value].type == typecheck_ftyp(node.children[0])
    )

def typecheck_ftyp(node):
    if node.value == "num":
        return "n"
    elif node.value == "void":
        return "v"
    else:
        raise TypeError("Invalid FTYP value: {}".format(node.value))

def typecheck_body(node):
    if len(node.children) != 5 or node.children[0].type != "PROLOG" or node.children[2].type != "ALGO" or node.children[3].type != "EPILOG" or node.children[4].type != "SUBFUNCS":
        raise TypeError("Invalid BODY structure")
    return (
        typecheck(node.children[0])
        and typecheck(node.children[1])
        and typecheck(node.children[2])
        and typecheck(node.children[3])
        and typecheck(node.children[4])
    )

def typecheck_prolog(node):
    return True

def typecheck_epilog(node):
    return True

def typecheck_locvars(node):
    if len(node.children) % 2 != 0:
        raise TypeError("Invalid LOCVARS structure")
    for i in range(0, len(node.children), 2):
        if node.children[i].type != "VTYP":
            raise TypeError("Invalid LOCVARS structure")
        if node.children[i + 1].type != "VNAME":
            raise TypeError("Invalid LOCVARS structure")
        symbol_table[node.children[i + 1].value] = SymbolTableEntry(node.children[i].value)
    return True

def typecheck_subfuncs(node):
    return typecheck_functions(node)