# Node Information Class

class NodeInfo:
    def __init__(
        self,
        node_id,
        classes,
        word,
        scope,
        parent_id,
        token_id,
        token_class,
        scope_id,
        parent_scope_id,
        type="undefined",
        data="undefined",
    ):
        self.parent_id = parent_id
        self.node_id = node_id
        self.token_id = token_id
        self.token_class = token_class
        self.classes = classes
        self.scope = scope
        self.word = word
        self.scope_id = scope_id
        self.parent_scope_id = parent_scope_id
        self.type = type
        self.data = data

    def get_node_id(self):
        return self.node_id

    def get_classes(self):
        return self.classes

    def get_word(self):
        return self.word

    def get_scope(self):
        return self.scope

    def get_parent_id(self):
        return self.parent_id

    def get_token_id(self):
        return self.token_id

    def get_token_class(self):
        return self.token_class

    def get_scope_id(self):
        return self.scope_id

    def get_parent_scope_id(self):
        return self.parent_scope_id

    def get_type(self):
        return self.type

    def get_data(self):
        return self.data

    def update_symbol(self, name, scope_id, new_data):
        if name == self.word and scope_id == self.scope_id:
            self.data = new_data
        else:
            raise ValueError(f"Invalid symbol '{name}' update attempt.")

    def set_type(self, type):
        if self.token_class != "reserved_keyword" and (
            self.word.startswith("V_") or self.word.startswith("F_")
        ):
            self.type = type
        else:
            self.type = "unknown"

    def is_function_decl(self):
        return (
            self.token_class == "F"
            and self.word.startswith("F_")
            and self.type != "undefined"
        )

    def is_variable_decl(self):
        return (
            self.token_class == "V"
            and self.word.startswith("V_")
            and self.type != "undefined"
        )
    
    def is_function_parameter(self):
        return (
            self.token_class == "V"
            and "HEADER" in self.classes
            and self.word.startswith("V_")
            and self.type == "undefined"
        )

    def print(self, node_id):
        class_str = " > ".join(self.classes)
        if len(class_str) > 149:
            class_str = class_str[:146] + "..."

        return f"{self.node_id:<10} {self.type:<10} {self.word:<15} {self.scope:<10} {self.parent_id:<10} {self.token_id:<10} {self.token_class:<17} {class_str}"


class SymbolInfo:
    def __init__(
        self,
        node_id,
        word,
        parent_id,
        token_class,
        scope_id,
        parent_scope_id,
        type_info,
        old,
        category,
        data="undefined",
    ):
        self.parent_id = parent_id
        self.node_id = node_id
        self.token_class = token_class
        self.word = word
        self.scope_id = scope_id
        self.parent_scope_id = parent_scope_id
        self.type = type_info
        self.data = data
        self.old = old
        self.category = category

    def get_node_id(self):
        return self.node_id

    def get_word(self):
        return self.word

    def get_parent_id(self):
        return self.parent_id

    def get_token_class(self):
        return self.token_class

    def get_scope_id(self):
        return self.scope_id

    def get_parent_scope_id(self):
        return self.parent_scope_id

    def get_type(self):
        return self.type

    def get_data(self):
        return self.data

    def get_old(self):
        return self.old

    def get_category(self):
        return self.category

    def update_symbol(self, name, scope_id, new_data, old):
        if name == self.word and scope_id == self.scope_id and self.old == old:
            self.data = new_data
        else:
            raise ValueError(f"Invalid symbol '{name}' update attempt.")

    def set_type(self, type_info):
        if self.token_class != "reserved_keyword" and (
            self.word.startswith("V_") or self.word.startswith("F_")
        ):
            self.type = type_info
        else:
            self.type = "unknown"

    def is_function_decl(self):
        return (
            self.token_class == "F"
            and self.word.startswith("F_")
            and self.type != "undefined"
        )

    def is_variable_decl(self):
        return (
            self.token_class == "V"
            and self.word.startswith("V_")
            and self.type != "undefined"
        )
        
    def is_function_parameter(self):
        return (
            self.token_class == "V"
            and "HEADER" in self.classes
            and self.word.startswith("V_")
            and self.type == "undefined"
        )

    def print(self, node_id):
        return f"{self.node_id:<10} {self.type:<10} {self.word:<10} {self.data:<15} {self.parent_id:<10} {self.token_class:<6} {self.old:<15} {self.category:<15}"
