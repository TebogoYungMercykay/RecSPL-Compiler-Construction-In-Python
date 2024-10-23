# TYPE CHECKING PART

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
            return 'n'
        elif ftype == "num":
            return 'v'
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

