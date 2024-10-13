# RecSPL Compiler Construction and Design Project

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

## Usage

To run the compiler:

```bash
python test.py
```

## Development Guidelines

1. **Modularity**: Keep each component (lexer, parser, etc.) in separate files or modules.
2. **Testing**: Write unit tests for each component in `test.py` or a dedicated `tests/` directory.
3. **Documentation**: Document your code thoroughly, including function descriptions and complex logic explanations.
4. **Error Handling**: Implement robust error handling and reporting throughout the compilation process.

## Contributing

When working on this project:

1. Create a new branch for each feature or component you're working on.
2. Write clean, well-commented code.
3. Ensure all tests pass before merging your changes.
4. Update this README when adding new components or making significant changes to the project structure.

## Building and Running

(Add specific instructions for building and running your compiler, including any dependencies or setup required.)

## Output

Compilation outputs and intermediate files are stored in the `out/` directory. Refer to the README in that directory for more details on the output files.

## Future Enhancements

- Optimization passes
- Support for additional language features
- Integration with IDEs or text editors

## Resources

- [Compiler Design Theory](../docs/Introduction%20to%20Compiler%20Design-Springer%20International%20Publishing%20(2017).pdf)
- [Language Specification](docs/specification/RecSPL_2024.md)
- [Project Documentation](docs/README.md)

---
