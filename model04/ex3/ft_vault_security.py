import typing


def secure_archive(filename: str, action: typing.Union[int, str],
                   content: str = "") -> tuple[bool, str]:
    try:
        if action in ('r', 0, 'read'):
            with open(filename, 'r') as f:
                data = f.read()
            return True, data
        elif action in ('w', 1, 'write'):
            with open(filename, 'w') as f:
                f.write(content)
            return True, "Content successfully written to file"
        else:
            return False, "Invalid action"
    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive('/not/existing/file', 'r')
    print(result)
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive('/etc/master.passwd', 'r')
    print(result)

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive('ancient_fragment.txt', 'r')
    print(result)
    if result[0]:
        previous_content = result[1]
        print("Using 'secure_archive'"
              "to write previous content to a new file:")
        result = secure_archive('new_fragment.txt', 'w', previous_content)
        print(result)


if __name__ == "__main__":
    main()
