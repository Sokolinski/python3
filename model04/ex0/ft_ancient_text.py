def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        storage_vault = open("ancient_fragment.txt", "r")
    except (FileNotFoundError, PermissionError) as e:
        print(f"{e}")
        return

    print("Connection established...")
    print("RECOVERED DATA:")
    try:
        recovered_data = storage_vault.read()
        print(recovered_data)
    except FileNotFoundError as e:
        print(f"{e}")
    finally:
        storage_vault.close()

    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
