def meow(n: int) -> str:
    """
    Make a cat meow n times.

    :param n: The number of times to meow.
    :return: A string containing the meow sound repeated n times.
    """
    return "Meow!\n" * n

number: int = int(input("Give a number"))
meows: str = meow(number)
print(meows)
