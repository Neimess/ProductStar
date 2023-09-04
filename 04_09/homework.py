class Pet(object):
    def __init__(self, name: str, species: str, age: int, gender: str):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Species - {self.species}, name is {self.name}, It's age is {self.age}, It's gender is {self.gender}"


class Dog(Pet):
    def __init__(self, name: str, species: str, age: int, gender: str, breed: str):
        super().__init__(name, species, age, gender)
        self.breed = breed

    def get_info(self):
        print(super().get_info() + f", breed is {self.breed}")

    def bark(self):
        print("Woof")


class Cat(Pet):
    def __init__(self, name: str, species: str, age: int, gender: str, color: str):
        super().__init__(name, species, age, gender)
        self.color = color

    def meow(self):
        print("Meow")

    def get_info(self):
        print(super().get_info() + f", has a {self.color} color")


dog = Dog("Max", "dogs", 8, "male", "sheepdog")
dog.get_info()
dog.bark()
cat = Cat("Mercy", "cats", 6, "kitty", "grey")
cat.get_info()
cat.meow()
