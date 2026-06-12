import re

"""
Basic patterns:
- . any character
- * zero or more of the preceding element
- + one or more of the preceding element
- ? zero or one of the preceding element
- {n} exactly n of the preceding element
- {n,} n or more of the preceding element
- {,m} up to m of the preceding element
- {n,m} between n and m of the preceding element
- [A-Z] any uppercase letter
- [a-z] any lowercase letter
- [0-9] any digit
- ^ start of string
- $ end of string
- \w any word character (alphanumeric & underscore)
- \d any digit
- \s any whitespace character
- \W any non-word character
- \D any non-digit character
- [^] any character not in the brackets

Common re syntax:
- re.search(pattern, string): Searches for the pattern in the string.
- re.match(pattern, string): Checks if the string starts with the pattern.
- re.fullmatch(pattern, string): Checks if the entire string matches the pattern.
- re.sub(pattern, replacement, string): Replaces occurrences of the pattern with the replacement in the string.

Common re patterns:
- r"\w+@\w+\.\w+": Matches a basic email format.
- r"^[A-Z][a-z]*": Matches a capitalized word at the start of a string.
- r"\d{3}-\d{2}-\d{4}": Matches a social security number format.
"""

email = input("Email: ").strip().lower()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email") 