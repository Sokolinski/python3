import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, 'r')
        content = file.read()
        print("---")
        print(content, end='')
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    lines = content.splitlines()
    transformed = '\n'.join(line + '#' for line in lines) + '\n'
    print("Transform data:")
    print("---")
    print(transformed, end='')
    print("---")

    new_filename = input("Enter new file name (or empty): ")
    if new_filename.strip():
        try:
            f = open(new_filename, 'w')
            f.write(transformed)
            f.close()
            print(f"Saving data to '{new_filename}'")
            print(f"Data saved in file '{new_filename}'.")
        except Exception as e:
            print(f"Error saving to '{new_filename}': {e}")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
