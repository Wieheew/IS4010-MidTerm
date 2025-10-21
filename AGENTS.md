# Emoji Hub CLI - Agent Guide

This document serves as a comprehensive guide for AI coding assistants working on the Emoji Hub CLI project. It provides context about the project's architecture, design decisions, and coding standards.

## Project Overview

The Emoji Hub CLI is a Python-based command-line interface that interacts with the [Emojihub API](https://github.com/cheatsnake/emojihub). It allows users to fetch and display emojis in various ways, including random selection, category-based filtering, and name-based search.

### Key Features
- Fetch random emojis
- Get random emojis by category
- Retrieve all emojis
- Filter emojis by category
- Search emojis by name
- Human-readable output format

## Project Structure
```
IS4010-MidTerm/
├── src/                  # Source code directory
│   ├── __init__.py
│   └── main.py          # Main CLI application
├── tests/               # Test files directory
│   ├── __init__.py
│   ├── test_emoji_cli.py    # Unittest-style tests
│   └── test_emoji_pytest.py # Pytest-style tests
├── README.md            # Project documentation
├── LICENSE             # MIT License
├── AGENTS.md           # This guide
└── requirements.txt    # Project dependencies
```

## Architecture Decisions

### 1. Code Structure
- **Organized Directory Structure**: Code is organized into `src` and `tests` directories for clear separation
- **Modular Functions**: Each API endpoint has its dedicated function for clear separation of concerns
- **Comprehensive Testing**: Both unittest and pytest style tests with good coverage
- **Error Handling**: Comprehensive try-except blocks for both network and data parsing errors

### 2. Dependencies
- **requests**: Used for HTTP requests to the API
- **pytest**: Used for running tests and generating coverage reports
- **pytest-cov**: For test coverage reporting
- All dependencies are specified with minimum versions in requirements.txt

### 3. API Integration
- Base URL: `https://emojihub.yurace.pro/api`
- RESTful endpoint structure
- JSON response parsing

## CLI Command Structure

### Command Pattern
The CLI follows a consistent command pattern using argparse:
```bash
python main.py [--option] [value]
```

### Available Commands
1. Random Emoji (Default):
   ```bash
   python main.py
   ```

2. Explicit Random Emoji:
   ```bash
   python main.py --random
   ```

3. Random by Category:
   ```bash
   python main.py --random_by_category "category_name"
   ```

4. All Emojis:
   ```bash
   python main.py --all
   ```

5. All by Category:
   ```bash
   python main.py --all_by_category "category_name"
   ```

## Coding Standards

### 1. Python Style Guidelines
- Follow PEP 8 conventions
- Use meaningful variable and function names
- Include docstrings for all functions
- Maintain consistent indentation (4 spaces)

### 2. Function Structure
- Single responsibility principle
- Clear input/output expectations
- Proper error handling
- No side effects outside of print functions

### 3. Error Handling
- Network errors (RequestException)
- Data parsing errors (KeyError, IndexError)
- User-friendly error messages

### 4. Output Format
Standard emoji output format:
```
Name: [emoji_name]
Category: [category]
Group: [group]
HTML Code: [html_code]
Unicode: [unicode]
```

## Contributing Guidelines

When modifying or extending the project:

1. Maintain the existing error handling pattern
2. Add docstrings for new functions
3. Update the README.md for new features
4. Ensure backward compatibility with existing commands
5. Test all command variations before committing

## Common Tasks

### Adding a New Command
1. Add new argument in `parser.add_argument()`
2. Create corresponding function for API interaction
3. Add condition in main try-except block
4. Update documentation

### Modifying Output Format
1. Update the `print_emoji()` function
2. Ensure consistent formatting across all commands
3. Update documentation to reflect changes

### Error Handling
1. Catch specific exceptions when possible
2. Provide clear error messages
3. Maintain the existing error handling structure

## Future Considerations

Potential areas for enhancement:
1. Cache frequently used results
2. Add support for emoji search
3. Implement output formatting options
4. Add unit tests
5. Consider adding async support for bulk operations

This guide should be updated as the project evolves to maintain its usefulness for AI agents working on the codebase.