# Type Checker for the RecSPL Language

class TypeChecker:
    def __init__(self, syntax_tree, symbols):
        self.symbols = symbols
        self.syntax_tree = syntax_tree
        self.node_table = symbols.get_node_table() if symbols else None
        self.symbol_table = symbols.get_symbol_table() if symbols else None
    
    def find_node_by_id(self, node_id):
        if self.syntax_tree.root and self.syntax_tree.root["unid"] == node_id:
            return self.syntax_tree.root

        for node in self.syntax_tree.inner_nodes:
            if node["unid"] == node_id:
                return node

        for node in self.syntax_tree.leaf_nodes:
            if node["unid"] == node_id:
                return node

        return None

    def find_decl_ancestor(self, node_id):
        target_node = self.find_node_by_id(node_id)

        if not target_node:
            return None

        current_node = target_node
        while current_node is not None:
            if current_node.get("symbol") == "DECL":
                return current_node

            parent_id = current_node["parent"] if "parent" in current_node else None
            if parent_id is None:
                break
            current_node = self.find_node_by_id(parent_id)

        return None
    
    def check_types(self):
        try:
            if self.symbols is not None and self.syntax_tree is not None:
                node = self.syntax_tree.root
                if (
                    "symbol" in node and node["symbol"] == "main"
                    and "parent" not in node and "children" in node
                ):
                    return self.typecheck_prog(node)
        except Exception as e:
            print(f"Error in Type ROOT: {str(e)}")

        return False

    def typecheck_prog(self, node):
        if len(node["children"]) != 3 or node["symbol"] != "main":
            raise TypeError("Invalid PROG structure")

        try:
            children = node["children"]
            return (
                self.typecheck_globvars(self.find_node_by_id(children[0]))
                and self.typecheck_algo(self.find_node_by_id(children[1]))
                and self.typecheck_functions(self.find_node_by_id(children[2]))
            )
        except Exception as e:
            print(f"Error in Type PROG: {str(e)}")

        return False

    def typecheck_globvars(self, node):
        if not node["children"] or len(node["children"]) <= 1:
            return True
        
        try:
            children = node["children"]
            for i in range(0, len(children), 3):
                if i >= len(children):
                    break
                    
                vtyp_node = self.find_node_by_id(children[i])
                if not vtyp_node:
                    return False
                    
                vname_node = self.find_node_by_id(children[i + 1])
                if not vname_node:
                    return False

                if not self.typecheck_vname(vname_node):
                    return False
                
                comma_node = self.find_node_by_id(children[i + 2])
                if not comma_node or "token" not in comma_node or comma_node["token"]["word"] != ",":
                    return False

            return True
            
        except Exception as e:
            print(f"Error in Type GLOBVARS: {str(e)}")

        return False

    def typecheck_vtyp(self, node):
        children = node["children"]
        vname_node = self.find_node_by_id(children[0])

        if not vname_node or "token" not in vname_node:
            return False
        
        vtype = self.symbols.get_type(vname_node['unid'])
        if vtype == "num":
            return 'n'
        elif vtype == "text":
            return 't'
        else:
            return 'u'

    def typecheck_ftyp(self, node):
        children = node["children"]
        fname_node = self.find_node_by_id(children[0])

        if not fname_node or "token" not in fname_node:
            return False
        
        ftype = self.symbols.get_type(fname_node['unid'])
        if ftype == "void":
            return 'v'
        elif ftype == "num":
            return 'n'
        else:
            return 'u'

    def typecheck_vname(self, node):
        children = node["children"]
        vname_node = self.find_node_by_id(children[0])

        if not vname_node or "token" not in vname_node:
            return False
        
        return vname_node["token"]["class"]
        
    def typecheck_fname(self, node):
        children = node["children"]
        fname_node = self.find_node_by_id(children[0])

        if not fname_node or "token" not in fname_node:
            return False
        
        return fname_node["token"]["class"]
    
    def typecheck_const(self, node):
        children = node["children"]
        const_node = self.find_node_by_id(children[0])

        if not const_node or "token" not in const_node:
            return False
        
        return const_node["token"]["class"].lower()

    def typecheck_algo(self, node):
        if "symbol" not in node or "unid" not in node:
            raise TypeError("Invalid ALGO structure")
        
        try:
            children = node["children"]
            begin = self.find_node_by_id(children[0])
            if not begin or "token" not in begin or begin["token"]["word"] != "begin":
                return False
                
            instr = self.find_node_by_id(children[1])
            if not instr:
                return False
                
            if not self.typecheck_instruc(instr):
                return False
            
            end = self.find_node_by_id(children[2])
            if not end or "token" not in end or end["token"]["word"] != "end":
                return False
            
            return True
        except Exception as e:
            print(f"Error in Type ALGO: {str(e)}")
        
        return False

    def typecheck_instruc(self, node):
        if len(node["children"]) < 1:
            return False
        
        try:
            children = node["children"]
            for i in range(0, len(children), 2):
                if i >= len(children):
                    break
                
                command = self.find_node_by_id(children[i])
                if not command:
                    return False
                
                if not self.typecheck_command(command):
                    return False
                
                semicolon = self.find_node_by_id(children[i + 1])
                if not semicolon or "token" not in semicolon or semicolon["token"]["word"] != ";":
                    return False

            return True
            
        except Exception as e:
            print(f"Error in Type INSTRUC: {str(e)}")

        return False

    def typecheck_command(self, node):
        if len(node["children"]) < 1:
            return False
        
        try:
            children = node["children"]
            command = self.find_node_by_id(children[0])
            
            if ("token" in command and command["token"]["word"] in ["skip", "halt"]):
                return True
            else:
                if "token" in command and command["token"]["word"] == "print":
                    atomic = self.find_node_by_id(children[1])
                    if atomic is None:
                        return False
                    return self.typecheck_atomic(atomic) in ("n", "t")
                elif "token" in command and command["token"]["word"] == "return":
                    decl = self.find_decl_ancestor(node["unid"])
                    if decl is None:
                        return False
                    
                    header = self.find_node_by_id(decl["children"][0])
                    f_type = self.find_node_by_id(header["children"][0])
                    ftype = self.find_node_by_id(f_type["children"][0])["token"]["word"]
                    
                    atomic = self.find_node_by_id(children[1])
                    if atomic is None:
                        return False

                    return self.typecheck_atomic(atomic) == ftype == 'n'
                else:
                    if command["symbol"] == "ASSIGN":
                        return self.typecheck_assign(command)
                    elif command["symbol"] == "CALL":
                        return self.typecheck_call(command) == 'v'
                    elif command["symbol"] == "BRANCH":
                        return self.typecheck_branch(command)

        except Exception as e:
            print(f"Error in Type COMMAND: {str(e)}")

        return False

    def typecheck_atomic(self, node):
        if len(node["children"]) < 1:
            return False
        
        try:
            children = node["children"]
            atomic = self.find_node_by_id(children[0])
            
            if "symbol" in atomic and atomic["symbol"] == "VNAME":
                return self.typecheck_vtyp(atomic)
            elif "symbol" in atomic and atomic["symbol"] == "CONST":
                return self.typecheck_const(atomic)
            else:
                return False

        except Exception as e:
            print(f"Error in Type ATOMIC: {str(e)}")

        return False

    def typecheck_assign(self, node):
        if len(node["children"]) < 3:
            return False
        
        try:
            vname = self.find_node_by_id(node["children"][0])
            op = self.find_node_by_id(node["children"][1])
            
            if vname is None or op is None:
                return False
            
            if "token" in op:
                if op["token"]["word"] == "<":
                    vtype = f"{self.typecheck_vtyp(vname)}"
                    return vtype == 'n'
                else:
                    val = self.find_node_by_id(node["children"][2])
                    return val is not None and self.typecheck_vtyp(vname) == self.typecheck_term(val)

        except Exception as e:
            print(f"Error in Type ASSIGN: {str(e)}")

        return False

    def typecheck_term(self, node):
        try:
            child = self.find_node_by_id(node["children"][0])
            if child is not None:
                if child["symbol"] == "ATOMIC":
                    return self.typecheck_atomic(child)
                elif child["symbol"] == "CALL":
                    return self.typecheck_call(child)
                elif child["symbol"] == "OP":
                    return self.typecheck_op(child)

        except Exception as e:
            print(f"Error in Type TERM: {str(e)}")

        return 'u'

    def typecheck_call(self, node):
        try:
            fname = self.find_node_by_id(node["children"][0])
            vone = self.find_node_by_id(node["children"][2])
            vtwo = self.find_node_by_id(node["children"][4])
            vthree = self.find_node_by_id(node["children"][6])
            
            if fname is None or vone is None or vtwo is None or vthree is None:
                return 'u'
            
            if self.typecheck_atomic(vone) == self.typecheck_atomic(vtwo) == self.typecheck_atomic(vthree) == 'n':
                return self.typecheck_ftyp(fname)

        except Exception as e:
            print(f"Error in Type TERM: {str(e)}")

        return 'u'

    def typecheck_op(self, node):
        try:
            op = self.find_node_by_id(node["children"][0])
            if "symbol" in op and op["symbol"] == "UNOP" and len(op["children"]) == 4:
                arg = self.find_node_by_id(op["children"][2])
                if arg is None:
                    return 'u'
                if self.typecheck_unop(op) == self.typecheck_arg(arg) == 'b':
                    return 'b'
                elif self.typecheck_unop(op) == self.typecheck_arg(arg) == 'n':
                    return 'n'
            elif "symbol" in op and op["symbol"] == "BINOP" and len(op["children"]) == 6:
                arg1 = self.find_node_by_id(op["children"][2])
                arg2 = self.find_node_by_id(op["children"][4])
                if arg1 is None or arg2 is None:
                    return 'u'
                elif self.typecheck_binop(op) == self.typecheck_arg(arg1) == self.typecheck_arg(arg2) == 'b':
                    return 'b'
                elif self.typecheck_binop(op) == self.typecheck_arg(arg1) == self.typecheck_arg(arg2) == 'n':
                    return 'n'
                elif self.typecheck_binop(op) == 'c' and (self.typecheck_arg(arg1) == self.typecheck_arg(arg2) == 'n'):
                    return 'b'
        except Exception as e:
            print(f"Error in Type OP: {str(e)}")

        return 'u'

    def typecheck_unop(self, node):
        try:
            if "symbol" in node and node["symbol"] == "UNOP" and len(node["children"]) == 4:
                unop = self.find_node_by_id(node["children"][0])
                if "token" in unop and unop["token"]["word"] == "not":
                    return "b"
                elif "token" in unop and unop["token"]["word"] == "sqrt":
                    return "n"
        except Exception as e:
            print(f"Error in Type UNOP: {str(e)}")

        return 'u'

    def typecheck_binop(self, node):
        try:
            if "symbol" in node and node["symbol"] == "BINOP" and len(node["children"]) == 6:
                binop = self.find_node_by_id(node["children"][0])
                if "token" in binop and binop["token"]["word"] in ("or", "and"):
                    return "b"
                elif "token" in binop and binop["token"]["word"] in ("eq", "grt"):
                    return "c"
                elif "token" in binop and binop["token"]["word"] in ("add", "sub", "mul", "div"):
                    return "n"
        except Exception as e:
            print(f"Error in Type BINOP: {str(e)}")

        return 'u'

    def typecheck_arg(self, node):
        try:
            arg = self.find_node_by_id(node["children"][0])
            if "symbol" in arg and arg["symbol"] == "ATOMIC":
                return self.typecheck_atomic(arg)
            elif "symbol" in arg and arg["symbol"] == "OP":
                return self.typecheck_op(arg)
        except Exception as e:
            print(f"Error in Type ARG: {str(e)}")

        return 'u'

    def typecheck_cond(self, node):
        try:
            arg = self.find_node_by_id(node["children"][0])
            if "symbol" in arg and arg["symbol"] == "SIMPLE":
                return self.typecheck_simple(arg)
            elif "symbol" in arg and arg["symbol"] == "COMPOSIT":
                return self.typecheck_composit(arg)
        except Exception as e:
            print(f"Error in Type COND: {str(e)}")

        return 'u'
    
    def typecheck_simple(self, node):
        try:
            op = self.find_node_by_id(node["children"][0])
            if "symbol" in op and op["symbol"] == "BINOP" and len(op["children"]) == 6:
                atomic1 = self.find_node_by_id(op["children"][2])
                atomic2 = self.find_node_by_id(op["children"][4])

                if atomic1 is None or atomic2 is None:
                    return 'u'
                elif self.typecheck_binop(op) == self.typecheck_atomic(atomic1) == self.typecheck_atomic(atomic2) == 'b':
                    return 'b'
                elif self.typecheck_binop(op) == 'c' and (self.typecheck_atomic(atomic1) == self.typecheck_atomic(atomic2) == 'n'):
                    return 'b'
        except Exception as e:
            print(f"Error in Type BRANCH: {str(e)}")

        return 'u'

    def typecheck_composit(self, node):
        try:
            op = self.find_node_by_id(node["children"][0])
            if "symbol" in op and op["symbol"] == "BINOP" and len(op["children"]) == 6:
                simple1 = self.find_node_by_id(op["children"][2])
                simple2 = self.find_node_by_id(op["children"][4])
                
                if simple1 is None or simple2 is None:
                    return 'u'

                if self.typecheck_binop(op) == self.typecheck_simple(simple1) == self.typecheck_simple(simple2) == 'b':
                    return 'b'
            elif "symbol" in op and op["symbol"] == "UNOP" and len(op["children"]) == 4:
                simple = self.find_node_by_id(op["children"][2])
                if simple is None:
                    return 'u'
                elif self.typecheck_binop(op) == self.typecheck_simple(simple) == 'b':
                    return 'b'
        except Exception as e:
            print(f"Error in Type COMPOSIT: {str(e)}")

        return 'u'

    def typecheck_branch(self, node):
        try:
            if "symbol" in node and node["symbol"] == "BRANCH" and len(node["children"]) == 6:
                cond = self.find_node_by_id(node["children"][1])
                algo1 = self.find_node_by_id(node["children"][3])
                algo2 = self.find_node_by_id(node["children"][5])
                
                if cond is None or algo1 is None or algo2 is None:
                    return False

                if self.typecheck_cond(cond) == 'b':
                    return (self.typecheck_algo(algo1) and self.typecheck_algo(algo2))
                else:
                    return False
        except Exception as e:
            print(f"Error in Type BRANCH: {str(e)}")

        return False

    def typecheck_functions(self, node):
        try:
            if "symbol" in node and node["symbol"] == "FUNCTIONS":
                children = node["children"]
                for i in range (0, len(children)):
                    if i >= len(children):
                        break
                    
                    decl = self.find_node_by_id(children[i])
                    if decl is None:
                        return False

                    if not self.typecheck_decl(decl):
                        return False

                return True
        except Exception as e:
            print(f"Error in Type FUNCTIONS: {str(e)}")

        return False

    def typecheck_decl(self, node):
        try:
            children = node["children"]
            if "symbol" in node and node["symbol"] == "DECL" and len(children) == 2:
                header = self.find_node_by_id(children[0])
                body = self.find_node_by_id(children[1])
                if header is None or body is None:
                    return False
                
                return self.typecheck_header(header) and self.typecheck_body(body)
        except Exception as e:
            print(f"Error in Type FUNCTIONS: {str(e)}")

        return False

    def typecheck_subfuncs(self, node):
        try:
            if "symbol" in node and node["symbol"] in ("SUBFUNCS", "FUNCTIONS"):
                return self.typecheck_functions(node)
        except Exception as e:
            print(f"Error in Type FUNCTIONS: {str(e)}")

        return False

    def typecheck_prolog(self, node):
        return "token" in node and node["token"]["word"] == "{"

    def typecheck_epilog(self, node):
        return "token" in node and node["token"]["word"] == "}"

    def typecheck_header(self, node):
        try:
            ftyp = self.find_node_by_id(node["children"][0])
            fname = self.find_node_by_id(node["children"][1])
            vone = self.find_node_by_id(node["children"][3])
            vtwo = self.find_node_by_id(node["children"][5])
            vthree = self.find_node_by_id(node["children"][7])
            
            if (
                ftyp is not None and fname is None or vone
                is None or vtwo is None or vthree is None
            ):
                return False
            
            return self.typecheck_vtyp(vone) == self.typecheck_vtyp(vtwo) == self.typecheck_vtyp(vthree) == 'n'

        except Exception as e:
            print(f"Error in Type HEADER: {str(e)}")

        return False

    def typecheck_body(self, node):
        try:
            children = node["children"]
            if "symbol" in node and node["symbol"] == "BODY" and len(children) == 6:
                prolog = self.find_node_by_id(children[0])
                locvars = self.find_node_by_id(children[1])
                algo = self.find_node_by_id(children[2])
                epilog = self.find_node_by_id(children[3])
                subfunctions = self.find_node_by_id(children[4])
                endnode = self.find_node_by_id(children[5])
                if (
                    prolog is None or locvars is None or algo is None or 
                    epilog is None or subfunctions is None or endnode is None
                ):
                    return False
                
                return (
                    self.typecheck_prolog(prolog) and self.typecheck_locvars(locvars) and
                    self.typecheck_algo(algo) and self.typecheck_epilog(epilog) and
                    self.typecheck_subfuncs(subfunctions) and endnode["token"]["word"] == 'end'
                )
        except Exception as e:
            print(f"Error in Type FUNCTIONS: {str(e)}")

        return False

    def typecheck_locvars(self, node):
        try:
            children = node["children"]
            for i in range(0, len(children), 3):
                if i >= len(children):
                    break
                    
                vtyp_node = self.find_node_by_id(children[i])
                if not vtyp_node:
                    return False
                    
                vname_node = self.find_node_by_id(children[i + 1])
                if not vname_node:
                    return False

                if not self.typecheck_vname(vname_node):
                    return False
                
                comma_node = self.find_node_by_id(children[i + 2])
                if not comma_node or "token" not in comma_node or comma_node["token"]["word"] != ",":
                    return False

            return True
            
        except Exception as e:
            print(f"Error in Type LOCVARS: {str(e)}")

        return False
