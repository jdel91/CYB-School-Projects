#!/usr/bin/env python3
"""
Password Strength Analyzer
Author: Jessica Delatorre
Course: CYB333 Security Automation

This program analyzes a password and gives it a strength rating.
It checks password length, uppercase letters, lowercase letters,
numbers, special characters, and common weak patterns.

Important security note:
This program does NOT store, save, or transmit passwords.
"""

import re
import getpass


# A small list of common weak passwords and patterns.
# This can be expanded later if needed.
COMMON_PASSWORDS = {
    "password",
    "password1",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "letmein",
    "welcome",
    "admin",
    "iloveyou",
    "monkey",
    "dragon",
    "football",
}


def check_password_length(password):
    """
    Checks the length of the password and returns a score and feedback.
    Longer passwords are usually harder to crack.
    """
    length = len(password)

    if length >= 16:
        return 3, "Excellent length. Passwords with 16 or more characters are stronger."
    elif length >= 12:
        return 2, "Good length. 12 or more characters is recommended."
    elif length >= 8:
        return 1, "Fair length, but using at least 12 characters would be better."
    else:
        return 0, "Password is too short. Use at least 12 characters."


def check_character_variety(password):
    """
    Checks whether the password contains uppercase letters, lowercase letters,
    numbers, and special characters.
    """
    score = 0
    feedback = []

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character, such as !, @, #, or $.")

    if not feedback:
        feedback.append("Good character variety.")

    return score, feedback


def check_common_patterns(password):
    """
    Checks for common weak passwords and easy-to-guess patterns.
    """
    password_lower = password.lower()
    warnings = []
    penalty = 0

    if password_lower in COMMON_PASSWORDS:
        warnings.append("This password is very common and should not be used.")
        penalty += 3

    if "password" in password_lower:
        warnings.append("Avoid using the word 'password' in your password.")
        penalty += 2

    if re.search(r"(1234|2345|3456|4567|5678|6789)", password_lower):
        warnings.append("Avoid simple number sequences like 1234 or 5678.")
        penalty += 2

    if re.search(r"(abcd|qwerty|asdf)", password_lower):
        warnings.append("Avoid keyboard patterns or alphabet sequences.")
        penalty += 2

    if re.search(r"(.)\1\1", password):
        warnings.append("Avoid repeating the same character multiple times.")
        penalty += 1

    if not warnings:
        warnings.append("No common weak patterns detected.")

    return penalty, warnings


def analyze_password(password):
    """
    Analyzes the password and returns a final rating with detailed feedback.
    """
    total_score = 0
    feedback = []

    # Check password length
    length_score, length_feedback = check_password_length(password)
    total_score += length_score
    feedback.append(length_feedback)

    # Check character variety
    variety_score, variety_feedback = check_character_variety(password)
    total_score += variety_score
    feedback.extend(variety_feedback)

    # Check common weak patterns
    pattern_penalty, pattern_feedback = check_common_patterns(password)
    total_score -= pattern_penalty
    feedback.extend(pattern_feedback)

    # Prevent negative scores
    if total_score < 0:
        total_score = 0

    # Determine password strength rating
    if total_score >= 7:
        rating = "Strong"
    elif total_score >= 4:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, total_score, feedback


def display_results(rating, score, feedback):
    """
    Displays the password strength results in a clear format.
    """
    print("\nPassword Strength Results")
    print("-" * 30)
    print(f"Rating: {rating}")
    print(f"Score: {score}/7")
    print("\nFeedback:")

    for item in feedback:
        print(f"- {item}")


def main():
    """
    Main function that runs the password strength analyzer.
    """
    print("Password Strength Analyzer")
    print("=" * 30)
    print("This tool checks password strength without storing your password.")

    # getpass hides the password while the user types it.
    password = getpass.getpass("Enter a password to analyze: ")

    if not password:
        print("No password entered. Please run the program again.")
        return

    rating, score, feedback = analyze_password(password)
    display_results(rating, score, feedback)


if __name__ == "__main__":
    main()
