class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name.capitalize()
        self.age = age
        self.height = height


class Flower(Plant):
    def __init__(self, name: str, age: int, height: int, color: str):
        super().__init__(name, age, height)
        self.color = color.lower()

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    def __init__(self, name: str, age: int, height: int, trunk_diameter: int):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"{self.name} provides {self.trunk_diameter * 1.56:.2f} "
            f"square meters of shade"
        )

    def get_info(self):
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter} cm"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: int,
        nutritional_value: str,
        harvest_season: str,
    ):
        super().__init__(name, age, height)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self):
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} season"
        )
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def main():
    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Sunflower", 120, 40, "yellow")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Bamboo", 250, 200, 5)
    vege1 = Vegetable("Tomato", 80, 90, "C", "summer")
    vege2 = Vegetable("Cucumber", 70, 70, "K", "warm")

    print("=== Garden Plant Types ===")
    print()
    flower1.get_info()
    flower1.bloom()
    print()
    flower2.get_info()
    flower2.bloom()
    print()
    tree1.get_info()
    tree1.produce_shade()
    print()
    tree2.get_info()
    tree2.produce_shade()
    print()
    vege1.get_info()
    print()
    vege2.get_info()


if __name__ == "__main__":
    main()
