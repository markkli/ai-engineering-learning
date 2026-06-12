name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(name + "\n")

# with doesn't need you to close the file