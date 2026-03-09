# Dog model goes here
class Dog:
    def __init__(self, name, breed, age, last_checkup = None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup

    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date

    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")

    # GETTER
    def get_age(self):
        return self._age
    
    # SETTER
    def set_age(self, value):
        if type(value) is int and value >= 0:
            self._age = value
        else:
            print("Invalid age.")

    age = property(get_age, set_age)

# ---------------- TESTS ----------------

# fido = Dog("Fido", "Golden Retriever", 3, "05/22/2022")

# clifford = Dog(name = "Clifford",
#                breed = "Big Red",
#                age = 2
#                )

# print(fido.age)
# fido.birthday_celebration()
# print(fido.age)

# print(clifford.last_checkup)
# clifford.checkup("03/02/2024")
# print(clifford.last_checkup)

# fido.age = -10
# fido.age = "-10"
# fido.age = 10
# print(fido.age)

# balto = Dog("Balto", "Husky", "Not an age")
# steele = Dog("Steele", "Husky", "-10")