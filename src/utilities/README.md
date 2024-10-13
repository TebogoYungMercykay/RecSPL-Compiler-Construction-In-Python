# Utilities Directory

This directory contains various utility scripts and helper functions used across the project. These utilities are designed to assist with common tasks and provide reusable functionality.

## Contents

- `__init__.py`: Initializes the utilities package, allowing its modules to be imported.
- `nfa_to_dfa.py`: A utility script for converting Non-deterministic Finite Automata (NFA) to Deterministic Finite Automata (DFA).
- `...`

## Usage

To use these utilities in other parts of the project, you can import them like this:

```python
from utilities import nfa_to_dfa

# Or to import specific functions:
from utilities.nfa_to_dfa import convert_nfa_to_dfa
```

## Example: NFA to DFA Conversion

The `nfa_to_dfa.py` script is an example of a utility in this directory. Here's how to use it:

1. Edit the `nfa_to_dfa.py` file to add the required states and information for your NFA.
2. Run the conversion using the following command:

```python
from utilities.nfa_to_dfa import convert_nfa_to_dfa

dfa_filepath = "out/dfa_output.txt"
convert_nfa_to_dfa(dfa_filepath)
```

3. The resulting DFA will be written to `dfa_gen.txt`, which can be used with mermaid stateDiagram-v2 syntax for visualization.

## Adding New Utilities

When adding new utility scripts to this directory:

1. Create a new Python file with a descriptive name (e.g., `string_operations.py`).
2. Implement your utility functions or classes in the new file.
3. If necessary, update the `__init__.py` file to include imports for easy access to your new utilities.
4. Add documentation within the script and update this README with a brief description of the new utility.

## Maintenance

- Keep utility functions focused and well-documented.
- Regularly review and refactor utilities to ensure they remain relevant and efficient.
- When updating existing utilities, consider backwards compatibility to avoid breaking dependent code.

---
