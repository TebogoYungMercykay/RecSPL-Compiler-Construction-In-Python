from type_checker import TypeChecker

def check_types(syntax_tree, symbols):
    print("\n--- Checking Types for The RecSPL Code ---")
    print("----------------------------------")

    try:
        checker = TypeChecker(syntax_tree, symbols)
        types_result = checker.check_types()

        if types_result:
            print("\033[92mType Checking Successful.\033[0m")
            print("----------------------------------")
        
        return types_result
    except TypeError as e:
        print(f"Type Checking failed: {e}")
        print("----------------------------------")

        return False
