# Dog model goes here
class Dog:
    def __init__(self, breed, name, age, checkup_date=None):
        self.breed = breed
        self.name = name
        self.set_age(age)
        self.checkup_date = checkup_date
    def checkup(self,date):
        self.checkup_date = date
        print(f"Checking up with {self.name} on {date}")
    def birthday_celebration(self):
        self.set_age(self.get_age() + 1)
    def get_age(self):
        return self.age 
    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self.age = value
        else:
            raise ValueError("Age must be a non-negative integer.")
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")
#creating instances of the Dog class
Jeremy = Dog("Golden Retriever", "Jeremy", 5, "2024-05-01")
Cliff = Dog("Bulldog", "Cliff", 3, "2024-06-15")
Marc = Dog("Poodle", "Marc", 2, "2024-07-20")
Tabby = Dog("Tabby Cat", "Tabby", 4, "2024-08-10")

Jeremy.birthday_celebration()# Output: Happy birthday Jeremy! You are now 6 years old.
print(Jeremy.get_age()) # Output: 6
Cliff.birthday_celebration()# Output: Happy birthday Cliff! You are now 4 years old.
print(Cliff.get_age()) # Output: 4
Marc.birthday_celebration()# Output: Happy birthday Marc! You are now 3 years old.
print(Marc.get_age()) # Output: 3
Tabby.birthday_celebration()# Output: Happy birthday Tabby! You are now 5 years old.
print(Tabby.get_age()) # Output: 5