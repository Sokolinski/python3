import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name = sys.argv[0].split("/")[-1]
    print(f"Program name: {program_name}")
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argv_len - 1}")
        for i in range(1, argv_len):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {argv_len}")


if __name__ == "__main__":
    main()
