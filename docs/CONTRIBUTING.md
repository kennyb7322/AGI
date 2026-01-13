# Contributing to AGI Framework

Copyright © 2026 kennyb7322  
Licensed under the MIT License

First off, thank you for considering contributing to the AGI Framework! It's people like you that make this framework a great tool for the AI community.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, error messages)
- **Describe the behavior you observed** and what you expected
- **Include system information** (Python version, OS, etc.)

Example bug report:

```markdown
## Bug Description
Model training fails with large batch sizes

## Steps to Reproduce
1. Initialize AGIModel
2. Create training data with 10000 examples
3. Set batch_size=1024 in TrainingConfig
4. Call trainer.train()

## Expected Behavior
Training should complete successfully

## Actual Behavior
Raises ValueError: "Batch size too large"

## System Information
- Python: 3.9.0
- OS: Ubuntu 20.04
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **Provide examples** of how it would be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** if applicable
4. **Update documentation** to reflect your changes
5. **Ensure the test suite passes**
6. **Submit a pull request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/AGI.git
cd AGI

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: 100 characters maximum
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Double quotes for strings, single quotes for small string literals
- **Imports**: Organized in three groups (standard library, third-party, local)

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    Longer description if needed, explaining the function's
    purpose and behavior in detail.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param2 is negative
        
    Example:
        >>> result = function_name("test", 5)
        >>> print(result)
        True
    """
    pass
```

### Type Hints

Always include type hints:

```python
from typing import List, Dict, Optional, Any

def process_data(
    data: List[str],
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, float]:
    """Process data and return metrics."""
    pass
```

### Error Handling

- Use specific exception types
- Include helpful error messages
- Document exceptions in docstrings

```python
def validate_input(value: int) -> None:
    """
    Validate input value.
    
    Args:
        value: Integer value to validate
        
    Raises:
        ValueError: If value is negative or zero
    """
    if value <= 0:
        raise ValueError(f"Value must be positive, got {value}")
```

### Copyright Headers

All source files should include the copyright header:

```python
"""
AGI Framework - Module Name
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Brief module description
"""
```

## Testing

### Writing Tests

Create tests in the `tests/` directory mirroring the source structure:

```
tests/
├── test_core/
│   ├── test_model.py
│   ├── test_trainer.py
│   └── test_inference.py
└── test_utils/
    ├── test_prompt_engineering.py
    └── test_context_manager.py
```

Example test:

```python
"""
Tests for AGIModel
Copyright (c) 2026 kennyb7322
Licensed under the MIT License
"""

import unittest
from agi import AGIModel


class TestAGIModel(unittest.TestCase):
    """Test cases for AGIModel."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.model = AGIModel(model_name="TestModel")
    
    def test_initialization(self):
        """Test model initialization."""
        self.assertEqual(self.model.model_name, "TestModel")
        self.assertFalse(self.model.is_trained)
    
    def test_training(self):
        """Test model training."""
        data = ["example 1", "example 2"]
        metrics = self.model.train(data, epochs=2)
        
        self.assertTrue(self.model.is_trained)
        self.assertIn('loss', metrics)
        self.assertIn('accuracy', metrics)


if __name__ == '__main__':
    unittest.main()
```

### Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_core.test_model

# Run with coverage
pip install coverage
coverage run -m unittest discover tests
coverage report
```

## Documentation

### Code Documentation

- Write clear, concise docstrings for all public APIs
- Include examples in docstrings when helpful
- Keep documentation up-to-date with code changes

### README Updates

When adding features:
1. Update the main README.md
2. Add examples to demonstrate usage
3. Update the API reference if needed

### Writing Examples

Good examples should:
- Be self-contained and runnable
- Include explanatory comments
- Demonstrate best practices
- Handle errors gracefully

## Git Commit Messages

Write clear commit messages:

```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what changed, why, and any side effects.

- Bullet points are okay
- Use present tense ("Add feature" not "Added feature")
- Reference issues: "Fixes #123" or "Related to #456"
```

Examples:

```
Add batch generation support to InferenceEngine

Implements batch_generate() method for processing multiple
prompts efficiently. Includes progress reporting and error
handling for failed generations.

Fixes #42
```

## Feature Branches

Use descriptive branch names:

- `feature/add-batch-processing`
- `bugfix/fix-context-overflow`
- `docs/improve-api-reference`
- `refactor/simplify-trainer`

## Review Process

### Pull Request Checklist

Before submitting, ensure:

- [ ] Code follows style guidelines
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary files are included
- [ ] Copyright headers are present

### Code Review

Reviewers will check:

- **Correctness**: Does the code do what it claims?
- **Style**: Does it follow our guidelines?
- **Tests**: Are there adequate tests?
- **Documentation**: Is it well documented?
- **Performance**: Are there any performance concerns?

## Questions?

Feel free to:

- Open an issue for discussion
- Ask in pull request comments
- Contact the maintainers

## Recognition

Contributors will be:

- Listed in CONTRIBUTORS.md
- Credited in release notes
- Recognized in the community

Thank you for contributing to AGI Framework! 🎉