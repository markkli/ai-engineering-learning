class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

        ...

class Student(Wizard):
    def __init__(self, name, house, patronus):
        super().__init__(name)
        self.house = house
        self.patronus = patronus

        ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

        ...

wizard = Wizard("Albus Dumbledore")
student = Student("Harry Potter", "Gryffindor", "Stag")
professor = Professor("Severus Snape", "Potions")