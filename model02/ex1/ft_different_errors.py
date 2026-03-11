def garden_operations(mode):
    if mode == "value":
        int("abc")
    elif mode == "division":
        10/0
    elif mode == "file":
        open("missing.txt")
    elif mode == "key":
        dct = {"a": 2}
        dct["missing plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()

    test_modes = ["value", "division", "file", "key"]

    for i in test_modes:
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError)as e:
            print(f"Testing {type(e).__name__}...")
            print(f"Caught an {type(e).__name__}: {e}")
            print()

    print("Testing multiple errors together...")

    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        print()

    print("All error types tested succesfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
