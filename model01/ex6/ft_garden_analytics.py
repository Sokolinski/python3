class Plant:
    def __init__(self, name: str, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.kind = "regular"

    def grow(self, grow_height=1):
        self.height += grow_height
        print(f"{self.name} grew {grow_height}cm")

    def print_info(self):
        print(f"{self.name.capitalize()} {self.height}cm")


class FloweringPlant(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.kind = "flowering"

    def print_info(self):
        print(f"{self.name.capitalize()} {self.height}cm (blooming)")


class PrizeFlower(FloweringPlant):

    def __init__(self, name, height, age, color, prize_point):
        super().__init__(name, height, age, color)
        self.prize_point = prize_point
        self.kind = "prize"

    def print_info(self):
        print(
            f"{self.name.capitalize()} {self.height}cm (blooming) "
            f"Prize point: {self.prize_point}"
        )


class Garden:

    def __init__(self, garden_owner):
        self.garden_owner = garden_owner
        self.plants: list[Plant] = []
        self.total_grow = 0

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.garden_owner}'s garden")

    def grow_all(self):
        print(f"{self.garden_owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_grow += 1

    def garden_report(self):
        print(f"=== {self.garden_owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            plant.print_info()

        plants_count = len(self.plants)
        print(f"\nPlants added: {plants_count}, Total growth:"
              f"{self.total_grow}cm")

        reg = flower = prize = 0
        for plant in self.plants:
            if plant.kind == "regular":
                reg += 1
            elif plant.kind == "flowering":
                flower += 1
            elif plant.kind == "prize":
                prize += 1
        print(
            f"Plant types: {reg} regular, {flower} flowering, {prize} prize"
            f"flowers"
        )


class GardenManager:

    @staticmethod
    def is_valid_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        return cls()

    def __init__(self):
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)


def main():
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    alice_garden.add_plant(Plant("Oak Tree", 100, 5))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 1, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, 1, "yellow", 10))

    bob_garden.add_plant(Plant("Pine", 80, 3))
    bob_garden.add_plant(FloweringPlant("Tulip", 12, 1, "pink"))

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    for garden in manager.gardens:
        garden.grow_all()

    for garden in manager.gardens:
        garden.garden_report()
        print("---")

    valid_heights = all(
        GardenManager.is_valid_height(plant.height)
        for garden in manager.gardens
        for plant in garden.plants
    )
    print(f"Height validation test: {valid_heights}")

    scores = {}
    for garden in manager.gardens:
        score = sum(plant.height for plant in garden.plants)
        score += sum(getattr(plant, "prize_point", 0)
                     for plant in garden.plants)
        scores[garden.garden_owner] = score
    print(
        "Garden scores - "
        + ", ".join(f"{name}: {score}" for name, score in scores.items())
    )

    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()
