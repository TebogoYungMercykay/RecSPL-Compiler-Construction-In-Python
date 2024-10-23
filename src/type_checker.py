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
    
