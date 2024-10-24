# Symbols Information Class

class Symbols:
    def __init__(self, node_table, symbol_table):
        self.node_table = node_table
        self.symbol_table = symbol_table

    def get_symbol_table(self):
        return self.symbol_table

    def get_node_table(self):
        return self.node_table

    def get_symbol_info(self, node_id, visited_scopes=None):
        # Initialize visited_scopes set on first call
        if visited_scopes is None:
            visited_scopes = set()

        node_info = self.node_table.get(f"{node_id}")
        
        if not node_info:
            print(f"No node info found for node ID: {node_id}")
            return None

        current_scope_id = node_info.scope_id
        word = node_info.word

        if current_scope_id in visited_scopes:
            return None

        # Add current scope to visited set
        visited_scopes.add(current_scope_id)

        # Look for symbol in current scope
        symbols_in_scope = self.get_symbol_by_scope_id(current_scope_id)
        for symbol in symbols_in_scope:
            if symbol.old == word:
                return symbol

        parent_scope_id = node_info.get_parent_scope_id()
        
        if parent_scope_id is None:
            if node_info.scope != 0:
                root_nodes = [
                    node for node in self.node_table.values()
                    if node.scope == 0
                ]
                
                # Check each node in root scope
                for root_node in root_nodes:
                    if root_node.scope_id not in visited_scopes:
                        result = self.get_symbol_info(root_node.node_id, visited_scopes.copy())
                        if result:
                            return result
            return None

        parent_nodes = [
            node for node in self.node_table.values()
            if node.scope_id == parent_scope_id
        ]

        for parent_node in parent_nodes:
            result = self.get_symbol_info(parent_node.node_id, visited_scopes.copy())
            if result:
                return result
        
        # check root scope as last resort
        if all(node.scope != 0 for node in parent_nodes):
            root_nodes = [
                node for node in self.node_table.values()
                if node.scope == 0
            ]
            
            for root_node in root_nodes:
                if root_node.scope_id not in visited_scopes:
                    result = self.get_symbol_info(root_node.node_id, visited_scopes.copy())
                    if result:
                        return result

        return None

    def get_symbol_by_scope_id(self, scope_id):
        return [
            node for node in self.symbol_table.values()
            if node.scope_id == scope_id
        ]

    def get_name(self, node_id):
        symbol_info = self.get_symbol_info(f"{node_id}")
        return symbol_info.get_word() if symbol_info else None

    def get_type(self, node_id):
        symbol_info = self.get_symbol_info(f"{node_id}")
        return symbol_info.get_type() if symbol_info else None

    def get_class(self, node_id):
        symbol_info = self.get_symbol_info(f"{node_id}")
        return symbol_info.get_token_class() if symbol_info else None

    def get_category(self, node_id):
        symbol_info = self.get_symbol_info(f"{node_id}")
        return symbol_info.get_category() if symbol_info else None
