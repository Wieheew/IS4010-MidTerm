# Emojihub CLI

[![Python Tests](https://github.com/Wieheew/IS4010-MidTerm/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Wieheew/IS4010-MidTerm/actions/workflows/python-tests.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command-line interface to interact with the Emojihub API.

## Description

This project provides a simple CLI to fetch and display emojis from the [Emojihub API](https://github.com/cheatsnake/emojihub). You can get random emojis, search by name, filter by category, and more.

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
├── LICENSE             # MIT License (MIT)
├── AGENTS.md           # Development guide
└── requirements.txt    # Project dependencies
```

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Wieheew/IS4010-MidTerm.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd IS4010-MidTerm
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Testing

Run all tests with coverage:
```bash
pytest tests/ -v --cov=src
```

Run specific test files:
```bash
pytest tests/test_emoji_cli.py -v    # Run unittest-style tests
pytest tests/test_emoji_pytest.py -v  # Run pytest-style tests
```

## Usage

Here are the available commands:

*   **Get a random emoji:**
    ```bash
    python src/main.py --random
    ```

*   **Search for emojis by name:**
    ```bash
    python src/main.py --search "cat"
    ```

*   **Get a random emoji from a specific category:**
    ```bash
    python src/main.py --random_by_category "smileys and people"
    ```

*   **Get all emojis:**
    ```bash
    python src/main.py --all
    ```

*   **Get all emojis from a specific category:**
    ```bash
    python src/main.py --all_by_category "food and drink"
    ```

Available categories:
- "smileys and people"
- "animals and nature"
- "food and drink"
- "activity"
- "travel and places"
- "objects"
- "symbols"
- "flags"

If you run the script without any arguments, it will fetch and display a random emoji by default.

## Output Format

Each emoji is displayed in the following format:
```
Name: [emoji_name]
Category: [category]
Group: [group]
HTML Code: [html_code]
Unicode: [unicode]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
