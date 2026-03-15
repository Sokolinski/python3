def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} " f"is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} " f"is too high (max 12)"
            )
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing correct values...")
    check_plant_health("tomato", 4, 5)
    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 3)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
