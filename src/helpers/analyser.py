from semantics import SemanticAnalyzer
from utilities.tree_crawling import XMLSemanticAnalyzer
from src.utilities.xml_methods import write_to_file


def analyser(parser_filepath, crawling_filepath, semantics_filepath):
    print("-- Analysing The RecSPL Code --")
    print("----------------------------------")
    try:
        # Example Usage
        parser_filepath = "out/syntax_tree.xml"
        semantic_an = SemanticAnalyzer(parser_filepath)
        semantic_an.analyze()  # Start the semantic analysis

        # Tree-Crawling Algirithm Output
        analyzer = XMLSemanticAnalyzer(parser_filepath)
        analyzer.analyze()
        crawl_result = (
            analyzer.print_hash_table()
        )  # Assuming this returns a string or you can capture its output
        write_to_file(crawl_result, crawling_filepath)
        print(f"Table for the Tree-Crawling Algorithm saved to {crawling_filepath}")

        # Get the analysis result (you can modify this based on what you want to write)
        result = semantic_an.print_symbol_table()  # Print the symbol table
        write_to_file(result, semantics_filepath)

        print(f"Semantics' Symbol Table Generated and Saved to {semantics_filepath}")
        print("Semantic Analysis successful.")
        print("----------------------------------\n\n")

        return True
    except Exception as e:
        print(f"Error Occurred: {str(e)}")

    return False


def semantics(parser_filepath, write_to, semantics_filepath):
    # TEMP FUNCTION: Call the semantic analysis function
    analyser(parser_filepath, write_to, semantics_filepath)
    return True
