class Vault:
    def __init__(self, gallieons=0, sickles=0, knuts=0):
        self.gallieons = gallieons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.gallieons} gallieons, {self.sickles} sickles, and {self.knuts} knuts"

    def __add__(self, other):
        if not isinstance(other, Vault):
            return NotImplemented
        return Vault(
            self.gallieons + other.gallieons,
            self.sickles + other.sickles,
            self.knuts + other.knuts
        )

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(75, 30, 15)
print(weasley)

total = potter + weasley
print(total)