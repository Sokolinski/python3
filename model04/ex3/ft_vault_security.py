def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as classified_vault:
            classified_data = classified_vault.read()
            print(classified_data)
    except FileNotFoundError:
        print("ERROR: classified_data.txt not found.")
        return
    except PermissionError:
        print("ERROR: Cannot access classified_data.txt.")
        return

    print("SECURE PRESERVATION:")
    new_security_protocol = "[CLASSIFIED] New security protocols archived"
    try:
        with open("security_protocols.txt", "w") as security_vault:
            security_vault.write(new_security_protocol + "\n")
    except PermissionError:
        print("ERROR: Cannot write to security_protocols.txt.")
        return

    print(new_security_protocol)
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
