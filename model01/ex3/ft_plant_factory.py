class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def blueprinter(self):
        print(f"{self.name}: {self.height}cm , {self.age} days old")

    def grow(self):
        self.height += 6

    def age_up(self):
        self.age += 6

    def get_info(self):
        self.blueprinter()


def main():
    data = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120},
    ]
    plants = [Plant(**d)for d in data]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ")
        plant.blueprinter()
    print(f"Total plants created:  {len(plants)}")


if __name__ == "__main__":
    main()
