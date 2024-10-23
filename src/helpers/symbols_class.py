# Symbols Information Class

class Symbols:
    def __init__(self, node_table, symbol_table):
        self.node_table = node_table
        self.symbol_table = symbol_table

    def get_symbol_table(self):
        return self.symbol_table

    def get_node_table(self):
        return self.node_table

    def get_symbol_info(self, node_id):
        node_info = self.node_table.get(node_id)
        if not node_info:
            return None

        current_scope_id = node_info.scope_id
        word = node_info.word

        while current_scope_id is not None:
            for symbol_id, symbol_info in self.symbol_table.items():
                if symbol_info.scope_id == current_scope_id and symbol_info.old == word:
                    return symbol_info
            # Move to the parent scope
            current_scope_id = self._get_parent_scope_id(current_scope_id)

        return None

    def get_name(self, node_id):
        symbol_info = self.get_symbol_info(node_id)
        return symbol_info.word if symbol_info else None

    def get_type(self, node_id):
        symbol_info = self.get_symbol_info(node_id)
        return symbol_info.type if symbol_info else None

    def get_class(self, node_id):
        symbol_info = self.get_symbol_info(node_id)
        return symbol_info.classes if symbol_info else None

    def get_category(self, node_id):
        symbol_info = self.get_symbol_info(node_id)
        return symbol_info.category if symbol_info else None

    def _get_parent_scope_id(self, scope_id):
        # Helper method to get the parent scope ID
        for symbol_id, symbol_info in self.symbol_table.items():
            if symbol_info.scope_id == scope_id:
                return symbol_info.parent_scope_id
        return None
