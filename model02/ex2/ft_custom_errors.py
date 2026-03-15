class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_eror(plant_name: str, watter_level: int, plant_status: str) -> None:
    if plant_status == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")
    elif watter_level < 5:
        raise WaterError("Not enough water in the tank")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        test_eror("tomato", 10, "wilting")
    except PlantError:
        print(f"Caught PlantError: {PlantError.__name__}\n")

    try:
        print("Testing WaterError...")
        test_eror("tomato", 3, "raising")

    except WaterError:
        print(f"Caught WatterEror: {WaterError.__name__}\n")

    print("Testing catching all garden errors...")
    try:
        test_eror("tomato", 10, "wilting")

    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        test_eror("tomato", 3, "abs")

    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
