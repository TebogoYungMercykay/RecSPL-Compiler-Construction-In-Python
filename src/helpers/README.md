# Helpers

This directory contains helper modules and utility functions used across the project.

## Contents

- `__init__.py`: Initializes the helpers package, allowing its modules to be imported.
- `syntax_tree.py`: Contains functions related to syntax tree operations.
- `xml_methods.py`: Provides utility functions for XML processing.
- `...`

## Usage

To use these helpers in other parts of the project, you can import them like this:

```python
from helpers import syntax_tree
from helpers import xml_methods
# more here...

# Or to import specific functions:
from helpers.syntax_tree import some_function
from helpers.xml_methods import another_function
# more here...
```

## Maintenance

When adding new helper functions:

1. Consider whether they belong in an existing module or if a new module should be created.
2. Keep functions focused and well-documented.
3. Update this README if you add new modules.

---
