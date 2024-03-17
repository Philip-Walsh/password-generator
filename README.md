# Password Generator 🛠️

This is a simple command-line tool to generate random passwords using Python.

2 hour coding challenge to build a command line interface with python 💻⏳

## Installation

To use this tool, make sure you have Poetry installed. Then run the following commands:

```bash
poetry shell && \
poetry update && \
poetry install && \
poetry run pytest  && \
poetry run pylint **/*.py && \
poetry run flake8 && \
echo "🧪 CI Passed! ✅" || echo "🧪 CI Failed! ❌"
```

## Usage

Generate a random password with a default length of 20 characters:

```bash
poetry run python -m pass_gen generate -len 20
```

You can also view the help message for more options:

```bash
poetry run python -m pass_gen --help
```

## Style and Functionality

- **Object-Oriented Design**: The code follows an object-oriented approach, with classes like `RandomChar` and `PasswordGenerator` encapsulating related functionality.
- **Modularity**: The code is modular, with separate methods for generating different types of characters (uppercase, lowercase, numbers, and special characters).
- **Flexibility**: The `PasswordGenerator` class allows for customization of password length and minimum requirements for different character types.
- **Randomization**: The generated passwords are randomized for increased security, with characters shuffled to create unique combinations.

Feel free to explore and modify the code according to your needs! Happy coding! 🚀
```