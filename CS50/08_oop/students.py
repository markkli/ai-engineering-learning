class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house # Even this goes through the setter
        self.patronus = patronus

    # Run whenever class is called as a string like print()
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter: when updating the house, has to going through this setter
    @house.setter 
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError("Invalid house")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Otter":
                return "🦦"
            case "Stag":
                return "🦌"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "🪄"

    @classmethod
    def get(cls):
        name = input("What is your name? ")
        house = input("What is your house? ")
        patronus = input("What is your patronus? ")
        return cls(name, house, patronus)

def main():
    student = Student.get()
    student.house = "Privet Drive" # Trigger setter
    print(student)

if __name__ == "__main__":
    main()