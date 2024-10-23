from type_checker import TypeChecker

def check_types(syntax_tree, symbol_table):
    print("\n--- Checking Types for The RecSPL Code ---")
    print("----------------------------------")

    try:
        checker = TypeChecker(syntax_tree, symbol_table)
        types_result = checker.check_types()

        print("\033[92mType Checking Successful.\033[0m")
        print("----------------------------------\n\n")
        
        return types_result
    except TypeError as e:
        print(f"Type Checking failed: {e}")
        print("----------------------------------\n\n")

        return False
