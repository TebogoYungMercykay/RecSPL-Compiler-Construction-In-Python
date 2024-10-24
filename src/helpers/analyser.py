from semantics import SemanticAnalyzer
from utilities.tree_crawling import XMLSemanticAnalyzer
from utilities.xml_methods import write_to_file
from helpers.symbols_class import Symbols

def analyser(parser_filepath, crawling_filepath, semantics_filepath):
    print("\n-- Analysing The RecSPL Code --")
    print("----------------------------------")
    try:
        # Tree-Crawling Algirithm Output
        analyzer = XMLSemanticAnalyzer(parser_filepath)
        analyzer.analyze()
        crawl_result = (
            analyzer.print_hash_table()
        )  # Assuming this returns a string or you can capture its output
        write_to_file(crawl_result, crawling_filepath)
        print(f"Table for the Tree-Crawling Algorithm saved to {crawling_filepath}")

        # Example Usage
        semantic_an = SemanticAnalyzer(parser_filepath, analyzer.get_node_table().items())
        semantic_an.analyze()  # Start the semantic analysis
        # Get the analysis result (you can modify this based on what you want to write)
        result = semantic_an.print_symbol_table()  # Print the symbol table
        write_to_file(result, semantics_filepath)

        print(f"Semantics' Symbol Table Generated and Saved to {semantics_filepath}")
        print("\033[92mSemantic Analysis successful.\033[0m")
        print("----------------------------------")

        symbols = Symbols(analyzer.get_node_table(), semantic_an.get_symbol_table())
        return symbols
    except Exception as e:
        print(f"Error Occurred: {str(e)}")

    return None

def semantics(parser_filepath, write_to, semantics_filepath):
    # TEMP FUNCTION: Call the semantic analysis function
    return analyser(parser_filepath, write_to, semantics_filepath)
