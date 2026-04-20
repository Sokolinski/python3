import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return

    lines = content.splitlines()
    transformed = '\n'.join(line + '#' for line in lines) + '\n'
    print("Transform data:")
    print("---")
    print(transformed, end='')
    print("---")

    print("Enter new file name (or empty): ", end='')
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()
    if new_filename:
        try:
            f = open(new_filename, 'w')
            f.write(transformed)
            f.close()
            print(f"Saving data to '{new_filename}'")
            print(f"Data saved in file '{new_filename}'.")
        except Exception as e:
            print(f"[STDERR] Error opening file '{new_filename}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
