def handle_archive_access(filename: str, routine: bool = False) -> None:
    if routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        if filename == "classified_vault.txt":
            raise PermissionError

        with open(filename, "r") as archive_file:
            archive_data = archive_file.read().strip()
            print(f"SUCCESS: Archive recovered - ``{archive_data}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly encountered")
        print("STATUS: Crisis handled, fallback protocols active")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_archive_access("lost_archive.txt")
    handle_archive_access("classified_vault.txt")
    handle_archive_access("standard_archive.txt", routine=True)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
