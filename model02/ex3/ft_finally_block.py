def water_plants(plant_list: list[str | None]) -> None:
    is_successful = True
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        is_successful = False
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
        if is_successful:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    good_list = ["tomato", "lettuce", "carrots"]
    error_list = ["tomato", None]
    print("=== Garden Water System ===\n")
    print("Testing normal watering...")
    water_plants(good_list)
    print("\nTesting with error...")
    water_plants(error_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
