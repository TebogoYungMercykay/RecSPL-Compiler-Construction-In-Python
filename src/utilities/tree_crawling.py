# Tree-Crawling Algorythm

import xml.etree.ElementTree as ET
from helpers.node_class import NodeInfo
from utilities.random_id import generate_random_id


class XMLSemanticAnalyzer:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.scope = 0
        self.node_table = {}  # Hash table to store nodes
        self.filters = ["FTYP", "VTYP", "VNAME", "FNAME"]
        self.scope_ids = []  # All generated scope identifiers

    def analyze(self):
        program_node = self.root.find(".//ROOT")
        scope_id = generate_random_id()
        self.scope_ids.append(scope_id)
        self.analyze_program(program_node, self.scope, [], "ROOT", scope_id)
        self.set_types()

    def analyze_program(self, program_node, scope, class_list, node_type, scope_id):
        children = program_node.find("CHILDREN")
        num_children = self.len_children(children)

        node_id = program_node.find("UNID").text
        symb = program_node.find("SYMB")
        if symb is not None and symb.text != "ε":
            class_list.append(symb.text)

        new_scope = (
            scope + 1
            if (
                symb is not None
                and symb.text != "ε"
                and symb.text in ["BODY", "ALGO", "BRANCH"]
            )
            else scope
        )
        if new_scope != scope:
            while scope_id in self.scope_ids:
                scope_id = generate_random_id()
            self.scope_ids.append(scope_id)

        # Adding node to hash table
        if (
            any(keyword in class_list for keyword in self.filters)
            and node_type == "LEAF_NODE"
        ):
            self.node_table[node_id] = NodeInfo(
                node_id,  # node_id
                class_list.copy(),  # classes
                program_node.find("TERMINAL/TOK/WORD").text,  # word
                scope,  # scope
                program_node.find("PARENT").text,  # parent_id
                program_node.find("TERMINAL/TOK/ID").text,  # token_id
                program_node.find("TERMINAL/TOK/CLASS").text,  # token_class
                scope_id,  # scope id
            )

        for counter in range(1, (num_children + 1)):
            child_id = children.find(f"ID[{counter}]").text
            var_name_in_node = self.find_inner_node_by_id(child_id)
            var_name_leaf_node = self.find_leaf_node_by_id(child_id)

            if (
                var_name_in_node is not None
                and var_name_in_node.find("SYMB").text != "ε"
            ):
                self.analyze_program(
                    var_name_in_node,
                    new_scope,
                    class_list.copy(),
                    "INNER_NODE",
                    scope_id,
                )
            elif (
                var_name_leaf_node is not None
                and var_name_leaf_node.find("TERMINAL/TOK/WORD").text != "ε"
            ):
                self.analyze_program(
                    var_name_leaf_node,
                    new_scope,
                    class_list.copy(),
                    "LEAF_NODE",
                    scope_id,
                )

    def set_types(self):
        ids = []
        for node_id, node_info in self.node_table.items():
            if node_info is not None and node_info.token_class == "reserved_keyword":
                target = self.node_table.get(str(int(node_id) + 2), None)
                if target is not None:
                    target.set_type(node_info.word)
                    ids.append(node_id)
                else:
                    raise ValueError(
                        f"404: Matching Variable Name for this Type:'{node_info.word}' NOT FOUND."
                    )

        for id in ids:
            removed = self.node_table.pop(id, None)
            if removed is None:
                raise ValueError(
                    f"404: Node with ID '{node_id}' NOT FOUND in Hash Table."
                )

    def gen_tabs(self, scope=1):
        return "\t" * (scope - 1)

    def len_children(self, children):
        return len(children.findall("ID")) if children is not None else 0

    def find_leaf_node_by_id(self, node_id):
        return self.root.find(f".//LEAF[UNID='{node_id}']")

    def find_inner_node_by_id(self, node_id):
        return self.root.find(f".//IN[UNID='{node_id}']")

    def print_hash_table(self):
        output = []

        output.append("\nHash Table Contents:")
        output.append("=" * 239)
        output.append(
            f"{'Node ID':<10} {'Type':<10} {'Word':<15} {'Scope':<10} {'Parent ID':<10} {'Token ID':<10} {'Token Class':<17} {'Classes'}"
        )
        output.append("-" * 239)

        for node_id, node_info in self.node_table.items():
            if node_info is not None:
                output.append(node_info.print(node_id))

        output.append("=" * 239)

        return "\n".join(output)

    def get_node_table(self):
        return self.node_table
