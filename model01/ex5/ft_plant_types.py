class Plant:
    def __int__(self, name: str, age: int, heigth: int):
        self.name = name.capitalize()
        self.age = age
        self.heigth = heigth


class flower(Plant):
    def __init__(self, name: str, age: int, heigth: int, collor: str):
        super().__init__(name, age, heigth)
        self.collor = collor.lower()

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(
            f"{self.name} (Flower): {self.heigth}cm, {self.age} days, {self.collor} color")


def main():
    Rose = flower("Rose")
