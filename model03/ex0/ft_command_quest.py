import sys


def main() -> None:
    print("=== Command Quest ===")
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if argv_len > 1:
        print(f"Arguments received: {argv_len-1}")
        for i in range(1, argv_len):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {argv_len}")


if __name__ == "__main__":
    main()
