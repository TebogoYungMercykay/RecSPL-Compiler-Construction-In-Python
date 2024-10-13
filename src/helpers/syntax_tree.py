import xml.etree.ElementTree as ET
from xml.dom import minidom


class SyntaxTree:
    def __init__(self):
        self.unique_id_counter = 1
        self.root = None
        self.inner_nodes = []
        self.leaf_nodes = []

    def generate_unique_id(self):
        """Generate a unique ID for each node."""
        uid = self.unique_id_counter
        self.unique_id_counter += 1
        return uid

    def add_root(self, symbol):
        """Create the root of the syntax tree."""
        uid = self.generate_unique_id()
        self.root = {"unid": uid, "symbol": symbol, "children": []}
        return self.root

    def add_inner_node(self, parent, symbol):
        """Add an inner node and link it to its parent."""
        uid = self.generate_unique_id()
        inner_node = {
            "parent": parent["unid"],
            "unid": uid,
            "symbol": symbol,
            "children": [],
        }
        self.inner_nodes.append(inner_node)
        parent["children"].append(uid)
        return inner_node

    def add_leaf_node(self, parent, token):
        """Add a leaf node and link it to its parent."""
        uid = self.generate_unique_id()
        leaf_node = {"parent": parent["unid"], "unid": uid, "token": token}
        self.leaf_nodes.append(leaf_node)
        parent["children"].append(uid)
        return leaf_node

    def to_xml(self):
        """Convert the syntax tree to XML format."""
        root = ET.Element("SYNTREE")

        # Root
        root_element = ET.SubElement(root, "ROOT")
        ET.SubElement(root_element, "UNID").text = str(self.root["unid"])
        ET.SubElement(root_element, "SYMB").text = self.root["symbol"]
        children = ET.SubElement(root_element, "CHILDREN")
        for child_id in self.root["children"]:
            ET.SubElement(children, "ID").text = str(child_id)

        # Inner nodes
        inner_nodes = ET.SubElement(root, "INNERNODES")
        for node in self.inner_nodes:
            inner_node = ET.SubElement(inner_nodes, "IN")
            ET.SubElement(inner_node, "PARENT").text = str(node["parent"])
            ET.SubElement(inner_node, "UNID").text = str(node["unid"])
            ET.SubElement(inner_node, "SYMB").text = node["symbol"]
            children = ET.SubElement(inner_node, "CHILDREN")
            for child_id in node["children"]:
                ET.SubElement(children, "ID").text = str(child_id)

        # Leaf nodes
        leaf_nodes = ET.SubElement(root, "LEAFNODES")
        for node in self.leaf_nodes:
            leaf_node = ET.SubElement(leaf_nodes, "LEAF")
            ET.SubElement(leaf_node, "PARENT").text = str(node["parent"])
            ET.SubElement(leaf_node, "UNID").text = str(node["unid"])
            terminal = ET.SubElement(leaf_node, "TERMINAL")
            token = node["token"]
            token_element = ET.SubElement(terminal, "TOK")
            ET.SubElement(token_element, "ID").text = token["id"]
            ET.SubElement(token_element, "CLASS").text = token["class"]
            ET.SubElement(token_element, "WORD").text = token["word"]

        # Pretty-print XML
        xml_str = ET.tostring(root, "utf-8")
        reparsed = minidom.parseString(xml_str)
        return reparsed.toprettyxml(indent="    ")
