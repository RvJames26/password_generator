# Password Generator

A simple, cryptographically secure password generator written in Python.  
It lets you specify total length and the number of digits, uppercase letters, and special characters, then generates a shuffled password that meets those requirements.

## Features
- Cryptographically secure random generation (`secrets` module)
- Customizable character requirements
- Automatic lowercase filler to reach total length
- Input validation (prevents required characters from exceeding total length)
- Loop to generate multiple passwords in one session

## Project Structure
```text
password_generator/
├── main.py            # Entry point / CLI loop
├── pass_requirement.py# Collects and validates user requirements
├── generator.py       # Password generation logic
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Requirements
- Python 3.8+

No external dependencies required.

## Usage
Run the program from the project directory:

```bash
python main.py
```

You will be prompted for:
1. Total password length
2. Number of digits
3. Number of uppercase letters
4. Number of special characters

Example:
```text
Total password length: 16
Number of digits: 4
Number of uppercase letters: 4
Number of special characters: 2
Password Generated:  k9#LmP2@wQ8!xR4y
Another one?: (y/n) y
...
```

## Notes
- `digits + uppercase + special` must not exceed `total length`; otherwise a `ValueError` is raised.
- Remaining slots are automatically filled with lowercase letters.
- Passwords are shuffled cryptographically after generation.
