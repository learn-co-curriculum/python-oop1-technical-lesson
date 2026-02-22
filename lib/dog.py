# Dog model goes here
class Dog:
    def __init__(self, name, breed, age, last_checkup=None):
        self.name =name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup
    def checkup (self, last_checkup):
        print(f"{self.name} was lasted checked on {last_checkup}")
        return last_checkup
    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age} years")
    def get_age(self):
        return self._age
    def set_age(self,value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age")
    age = property(get_age,set_age)
        
fido = Dog("Fido","Golden Retriever", 3, "05/22/2022")
clifford = Dog(
name = "Clifford",
age = 2, 
breed = "Big Red")

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)

balto = Dog("Balto", "Husky", 5)
steele = Dog("Steele", "Husky", 10)
