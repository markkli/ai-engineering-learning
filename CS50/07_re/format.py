import re

name = input("what is your name? ").strip()
match = re.search(r"^(.+), *(.+)$", name)

if match := re.search(r"^(.+), *(.+)$", name):
    name = f"{match.group(2)} {match.group(1)}"

print(f"hello, {name}")