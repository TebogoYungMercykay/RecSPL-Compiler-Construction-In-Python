# RecSPL Compiler Construction and Design Project

<img src="images/readme.jpg" style="width: 100%; height: 40%;" />

This `src/` directory contains the core components of our `Recursive Student Programming Language` Compiler Construction and Design project. The project aims to implement a complete compiler, including lexical analysis, parsing, semantic analysis, and code generation.

## Current Structure

- `lexer.py`: Implementation of the lexical analyzer.
- `parser.py`: Implementation of the syntactic parser.
- `test.py`: Test suite for various compiler components.
- `helpers/`: Directory containing helper functions and utilities.
- `utilities/`: Additional utility scripts and modules.
- `out/`: Directory for storing output files generated during compilation.
- `...`

## Planned Components

The project will include the following main components:

1. **Lexer**: Tokenizes the input source code.
2. **Parser**: Performs syntactic analysis and builds an abstract syntax tree.
3. **Scope-Analyser**: Handles scope resolution and symbol table management.
4. **Type-Checker**: Performs semantic analysis and type checking.
5. **Code-Generator**: Generates target code or intermediate representation.

## How to Run Compiler:

- ### Initial Compiler Setup and Usage Guide

  The set up is already configured that one can just add the filenames and run the code. The code is in the `src` directory.

  - #### Single File Compilation

    - ##### 1. Configure File Paths

      In `src/main.py`, set the following file paths:

      ```python
      code_filename = "RecSPL.txt"          # Input source code file
      lexer_filepath = "out/lexer.xml"      # Lexer output
      parser_filepath = "out/syntax_tree.xml"  # Parser output
      crawling_filepath = "out/semantics_crawling_output.txt"  # Semantic crawling results
      semantics_filepath = "out/semantics_symbols_output.txt"  # Symbol table output
      ```

    - ##### 2. Run the Compiler
    
      To compile a single file, use the `single()` function:

      ```python
      single(
          code_filename,
          lexer_filepath,
          parser_filepath,
          crawling_filepath,
          semantics_filepath
      )
      ```

  - #### Batch Compilation

      To compile multiple files at once, use the `bulk()` function. Here's how to set it up:

      ```python
      # Create a list of file configurations
      batch_files = []

      # Generate file paths for each test case (1 through 20)
      for k in range(1, 21):
          file_paths = {
              "code_filename": f"out/testing/typechecker/recspl/code-{k}.txt",
              "lexer_filepath": f"out/testing/typechecker/tokens/lexer-{k}.xml",
              "parser_filepath": f"out/testing/typechecker/tree/tree-{k}.xml",
              "crawling_filepath": f"out/testing/typechecker/crawling/crawl-{k}.txt",
              "semantics_filepath": f"out/testing/typechecker/symbols/symbols-{k}.txt"
          }
          batch_files.append(file_paths)

      # Run the compiler on all files
      bulk(batch_files)
      ```

- ### Installing Python Virtual Environment:

  ```bash
  # Installing dependencies
  sudo apt-get update
  sudo apt-get install python3-venv
  python3 -m venv venv
  ```
- ### Activating the Python Virtual Environment:

  ```bash
  source venv/bin/activate
  ```
- ### Deactivating the Python Virtual Environment:

  ```bash
  deactivate
  ```
- ### Run/Test The Compiler:

  ```bash
  # Change Directories
  cd src
  # Instling Dependencies
  pip install -r requirements.txt

  # Runnung the Compiler
  python main.py
  # Running the Tests
  pytest .
  # Running Tests and Showing Output
  pytest -s
  ```

- ### Project Structure

  ```txt
  .
  ├── conftest.py
  ├── helpers
  │   ├── analyser.py
  │   ├── convert_to_dfa.py
  │   ├── dfa_lexer.py
  │   ├── __init__.py
  │   ├── lexing.py
  │   ├── node_class.py
  │   ├── parsing.py
  │   ├── README.md
  │   ├── symbols_class.py
  │   ├── syntax_tree.py
  │   └── type_checker.py
  ├── __init__.py
  ├── lexer.py
  ├── main.py
  ├── out
  │   ├── dfa_output.txt
  │   ├── lexer.xml
  │   ├── README.md
  │   ├── semantics_crawling_output.txt
  │   ├── semantics_sybols_output.txt
  │   ├── semantics_symbols_output.txt
  │   ├── syntax_tree.xml
  │   └── testing
  │       ├── recspl
  │       │   ├── code-1.txt
  │       │   └── ...
  │       ├── semantics
  │       │   ├── crawling
  │       │   │   ├── crawl-1.txt
  │       │   │   └── ...
  │       │   ├── recspl
  │       │   │   ├── code-1.txt
  │       │   │   └── ...
  │       │   ├── symbols
  │       │   │   ├── symbols-1.txt
  │       │   │   └── ...
  │       │   ├── tokens
  │       │   │   ├── lexer-1.xml
  │       │   │   └── ...
  │       │   └── tree
  │       │       ├── tree-1.xml
  │       │       └── ...
  │       ├── tokens
  │       │   ├── lexer-1.xml
  │       │   └── ...
  │       ├── tree
  │       │   ├── tree-1.xml
  │       │   └── ...
  │       └── typechecker
  │           ├── crawling
  │           │   ├── crawl-1.txt
  │           │   └── ...
  │           ├── recspl
  │           │   ├── code-1.txt
  │           │   └── ...
  │           ├── symbols
  │           │   ├── symbols-1.txt
  │           │   └── ...
  │           ├── tokens
  │           │   ├── lexer-1.xml
  │           │   └── ...
  │           └── tree
  │               ├── tree-1.xml
  │               └── ...
  ├── parser.py
  ├── pytest.ini
  ├── RecSPL.txt
  ├── requirements.txt
  ├── runner.py
  ├── semantics.py
  ├── test
  │   ├── __init__.py
  │   ├── test_default.py
  │   ├── test_lexer.py
  │   ├── test_parser.py
  │   ├── test_semantics.py
  │   └── test_type_check.py
  ├── tree.txt
  ├── type_checker.py
  ├── utilities
  │   ├── __init__.py
  │   ├── nfa_to_dfa.py
  │   ├── random_id.py
  │   ├── README.md
  │   ├── tree_crawling.py
  │   └── xml_methods.py
  └── venv
      ├── bin
      │   ├── ...
      ├── include
      ├── lib
      │   └── ...
      ├── lib64 -> lib
      └── pyvenv.cfg
  ```

## Development Guidelines

1. **Modularity**: Keep each component (lexer, parser, etc.) in separate files or modules.
2. **Testing**: Write unit tests for each component in `/tests/filename_test.py` or a dedicated `tests/` directory.
3. **Documentation**: Document your code thoroughly, including function descriptions and complex logic explanations.
4. **Error Handling**: Implement robust error handling and reporting throughout the compilation process.

## Contributing

When working on this project:

1. Create a new branch for each feature or component you're working on.
2. Write clean, well-commented code.
3. Ensure all tests pass before merging your changes.
4. Update this README when adding new components or making significant changes to the project structure.

## Output

Compilation outputs and intermediate files are stored in the `out/` directory. Refer to the README in that directory for more details on the output files.

## Future Enhancements

- Optimization passes
- Support for additional language features
- Integration with IDEs or text editors

## Resources

- [Compiler Design Lecture Tips](./docs/lecture%20tips/README.md)
- [Language Specification](docs/specification/RecSPL_2024.md)
- [Project Documentation](docs/README.md)

---
