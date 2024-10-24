# Semantic Analyser for the RecSPL Language

from utilities.tree_crawling import XMLSemanticAnalyzer
from helpers.node_class import SymbolInfo

class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    def __init__(self, parser_filepath, table):
        self.table = table
        self.node_table = dict(sorted(self.table, key=lambda item: item[1].scope))
        self.symbol_table = {}
        self.parser_filepath = parser_filepath
        self.scopes = self.all_scopes()
        self.reversed = list(reversed(self.all_scopes()))
        self.counter_variable = 0
        self.counter_function = 0

    def get_and_increment_counter_var(self):
        self.counter_variable += 1
        return f"v{self.counter_variable}"

    def get_and_increment_counter_func(self):
        self.counter_function += 1
        return f"f{self.counter_function}"

    def all_scopes(self):
        # Creating a list of all scope values from the node table and return it sorted
        return sorted([info.scope for info in self.node_table.values()])

    def analyze(self):
        """Start the analysis from the top-level nodes."""
        for node_id, node_info in self.node_table.items():
            self.analyze_node(node_id, node_info.scope)

    def analyze_node(self, node_id, current_scope):
        node_info = self.node_table[node_id]

        if node_info.is_function_decl():  # Function Declaration
            self.process_function_declaration(node_info, current_scope)
            # Adding current node to the symbol table
            self.add_to_symbol_table(node_info, "declaration")
        elif node_info.is_variable_decl():  # Variable Declaration
            self.process_variable_declaration(node_info, current_scope)
            # Adding current node to the symbol table
            self.add_to_symbol_table(node_info, "declaration")
        elif node_info.is_function_parameter():  # Function Parameter
            self.add_to_symbol_table(node_info, "parameter")
        else:
            if node_info.token_class == "V":
                self.check_variable_usage(node_info, current_scope)
            else:
                self.check_function_usage(node_info, current_scope)

    def process_function_declaration(self, node_info, current_scope):
        function_name = node_info.word

        # Checking if function is already declared in the current scope
        result = self.check_function_declaration(
            node_info, function_name, current_scope
        )
        if result is not None:
            raise SemanticError(
                f"Function '{function_name}' already declared in {result} scope."
            )

    def process_variable_declaration(self, node_info, current_scope):
        variable_name = node_info.word

        # Checking if variable is already declared in the current scope
        result = self.check_variable_declaration(
            node_info, variable_name, current_scope
        )
        if result is not None:
            if result == "Parameter":
                raise SemanticError(
                    f"Variable '{variable_name}' already declared as a function parameter."
                )    
            else:
                raise SemanticError(
                    f"Variable '{variable_name}' already declared in {result} scope."
                )

    def check_variable_usage(self, node_info, current_scope):
        for scope in self.reversed:
            if scope <= current_scope:
                nodes_in_scope = self.get_nodes_by_scope(scope)
                if len(nodes_in_scope) > 0:
                    for node in nodes_in_scope:
                        if node_info.word == node.word and (
                            node.is_variable_decl() or ("HEADER" in node.classes)
                        ):
                            return

        raise SemanticError(
            f"Variable '{node_info.word}' used but not declared."
        )

    def check_function_usage(self, node_info, current_scope):
        for scope in self.reversed:
            if scope <= current_scope:
                nodes_in_scope = self.get_nodes_by_scope(scope)
                if len(nodes_in_scope) > 0:
                    for node in nodes_in_scope:
                        if (
                            node_info.word == node.word and node.is_function_decl()
                        ):  # node_info.token_id != node.token_id
                            return

        raise SemanticError(
            f"Function '{node_info.word}' used but not declared."
        )

    def add_to_symbol_table(self, node_info, category):
        unique_name = (
            self.get_and_increment_counter_var()
            if node_info.token_class == "V"
            else self.get_and_increment_counter_func()
        )

        # Adding to symbol table
        vtype = 'num' if category == 'parameter' else node_info.type
        self.symbol_table[node_info.node_id] = SymbolInfo(
            node_info.node_id,
            unique_name,
            node_info.parent_id,
            node_info.token_class,
            node_info.scope_id,
            node_info.parent_scope_id,
            vtype,
            node_info.word,
            category
        )

    def check_variable_declaration(self, node_info, name, scope):
        # Checking for declarations in the current scope and the immediate parent scope
        nodes_in_scope = self.get_nodes_by_scope(scope)
        if len(nodes_in_scope) > 0:
            for node in nodes_in_scope:
                if (
                    node.word == name
                    and node_info.token_id != node.token_id
                    and node.is_variable_decl()
                    and node.scope_id == node_info.scope_id
                ):
                    return "Current"  # Found in the current scope
                elif (
                    node.word == name
                    and node_info.token_id != node.token_id
                    and node.is_function_parameter()
                    and node.scope_id == node_info.scope_id
                ):
                    return "Parameter" # Matching Function Parameter

        # Checking in the immediate parent scope
        parent_scope = self.get_parent_scope(scope)
        nodes_in_parent_scope = self.get_nodes_by_scope(parent_scope)
        if len(nodes_in_parent_scope) > 0:
            for node in nodes_in_parent_scope:
                if (
                    node.word == name
                    and node_info.token_id != node.token_id
                    and node.is_variable_decl()
                    and node.scope_id != node_info.scope_id
                ):
                    return "Parent"  # Found in the parent scope

        return None

    def check_function_declaration(self, node_info, name, scope):
        # Checking for declarations in the current scope and the immediate parent scope
        nodes_in_scope = self.get_nodes_by_scope(scope)
        if len(nodes_in_scope) > 0:
            for node in nodes_in_scope:
                if (
                    node.word == name
                    and node_info.token_id != node.token_id
                    and node.is_function_decl()
                    and node.parent_scope_id == node_info.parent_scope_id
                ):
                    return "Current"  # Found in the current scope

        # Checking in the immediate parent scope
        parent_scope = self.get_parent_scope(scope)
        nodes_in_parent_scope = self.get_nodes_by_scope(parent_scope)
        if len(nodes_in_parent_scope) > 0:
            for node in nodes_in_parent_scope:
                if (
                    node.word == name
                    and node_info.token_id != node.token_id
                    and node.is_function_decl()
                    and node.scope_id != node_info.scope_id
                ):
                    return "Parent"  # Found in the parent scope

        return None

    def get_parent_scope(self, scope):
        for s in self.reversed:
            if s < scope:
                return s
        return None  # No parent scope found

    def get_nodes_by_scope(self, scope):
        nodes_in_scope = []

        for node_id, node in self.node_table.items():
            if node.scope == scope:
                nodes_in_scope.append(node)

        return nodes_in_scope

    def get_symbol_table(self):
        return self.symbol_table

    def print_symbol_table(self):
        output = []

        output.append("\nHash Table Contents:")
        output.append("=" * 95)
        output.append(
            f"{'Node ID':<10} {'Type':<10} {'Word':<10} {'Value':<15} {'Parent ID':<10} {'Class':<6} {'Real Name':<15} {'Category':<15}"
        )

        output.append("-" * 95)

        for symbol_id, symbol_info in self.symbol_table.items():
            if symbol_info is not None:
                output.append(symbol_info.print(symbol_id))

        output.append("=" * 95)

        return "\n".join(output)
