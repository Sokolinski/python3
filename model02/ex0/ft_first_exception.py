def check_temperature(temp_str: str) -> None:
    try:
        number = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if number < 0:
        print(f"Error: {number}°C is too cold for plants (min 0°C)")
    elif number > 40:
        print(f"Error: {number}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {number}°C is perfect for plants!")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    user_temp = input("Testing temperature: ")
    check_temperature(user_temp)


if __name__ == "__main__":
    main()
