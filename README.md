# Password Strength Analyzer

## Project Objective

The objective of this project is to create a simple password strength analyzer using Python. The tool checks whether a password is weak, medium, or strong based on common password security factors. It is designed to help users identify weak passwords before using them for personal or work accounts.

## Project Features

This password strength analyzer checks for:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Common weak passwords
- Common patterns such as `1234`, `abcd`, and `qwerty`
- Repeated characters

The program provides a strength rating of:

- Weak
- Medium
- Strong

It also gives feedback to help users improve their passwords.

## Security Note

This program does not store, save, or transmit passwords. The password is only analyzed while the program is running. The program uses Python's `getpass` module so the password does not appear on the screen while being typed.

## Prerequisites

To run this project, you need:

- Python 3 installed
- Visual Studio Code, Git Bash, Command Prompt, or another terminal
- GitHub account for uploading the project repository

No external Python libraries are required. This project only uses built-in Python modules.

## Files Included

```text
password_strength_analyzer.py
README.md
```

## How to Run the Program

1. Download or clone this repository.

```bash
git clone https://github.com/jdel91/password-strength-analyzer.git
```

2. Open the project folder.

```bash
cd password-strength-analyzer
```

3. Run the Python file.

```bash
python password_strength_analyzer.py
```

If `python` does not work, try:

```bash
python3 password_strength_analyzer.py
```

4. Enter a password when prompted.

The program will display a rating, score, and feedback.

## Example Output

```text
Password Strength Results
------------------------------
Rating: Medium
Score: 5/7

Feedback:
- Good length. 12 or more characters is recommended.
- Good character variety.
- No common weak patterns detected.
```

## Code Documentation

The code includes comments and function docstrings that explain the purpose of each section. The main functions are:

- `check_password_length()` checks whether the password is long enough.
- `check_character_variety()` checks for uppercase letters, lowercase letters, numbers, and special characters.
- `check_common_patterns()` checks for common weak passwords and patterns.
- `analyze_password()` calculates the final score and rating.
- `display_results()` prints the results for the user.
- `main()` runs the program.

## GitHub Submission Instructions

For the GitHub repository submission:

1. Create a new public repository on GitHub.
2. Upload `password_strength_analyzer.py` and `README.md`.
3. Do not upload passwords, API keys, or private information.
4. Copy the repository URL and submit it to the instructor.

Repository Link:

```text
https://github.com/jdel91/password-strength-analyzer
```
