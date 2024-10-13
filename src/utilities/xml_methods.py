import xml.etree.ElementTree as ET
from xml.dom import minidom
import os


def parse_xml_tokens(xml_file):
    """Parse tokens from the XML file and return a list of token dictionaries."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    tokens = []
    for token_element in root.findall("TOK"):
        token_id = token_element.find("ID").text
        token_class = token_element.find("CLASS").text
        token_word = token_element.find("WORD").text
        tokens.append({"id": token_id, "class": token_class, "word": token_word})

    return tokens


import xml.dom.minidom as minidom


def convert_syntax_tree_to_pretty_xml(syntax_tree):
    rough_xml = syntax_tree.to_xml()

    reparsed = minidom.parseString(rough_xml.encode("utf-8"))
    result_with_extra_spaces = reparsed.toprettyxml(
        indent="    ", encoding="UTF-8"
    ).decode("utf-8")

    pretty_xml = "\n".join(
        [line for line in result_with_extra_spaces.splitlines() if line.strip()]
    )

    return pretty_xml


def write_to_file(content, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as xml_file:
        xml_file.write(content)


def tokens_to_xml(filename, tokens):
    root = ET.Element("TOKENSTREAM")
    for i, token in enumerate(tokens, start=1):
        tok_element = ET.SubElement(root, "TOK")

        id_element = ET.SubElement(tok_element, "ID")
        id_element.text = str(i)

        class_element = ET.SubElement(tok_element, "CLASS")
        class_element.text = token.token_class

        word_element = ET.SubElement(tok_element, "WORD")
        word_element.text = token.token_value

    # Creating New XML Tree
    rough_string = ET.tostring(root, "utf-8")
    reparsed = minidom.parseString(rough_string)
    xml_str = reparsed.toprettyxml(indent="    ", encoding="UTF-8").decode("utf-8")

    # Removing Blank Lines
    xml_str = "\n".join([line for line in xml_str.split("\n") if line.strip()])

    # Writing to XML File
    write_to_file(xml_str, filename)

    print(f"Tokens written to {filename}")
