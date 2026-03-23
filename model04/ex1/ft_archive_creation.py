def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")

    archive_file = open("new_discovery.txt", "w")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")

    entry_1 = "[ENTRY 001] New quantum algorithm discovered"
    entry_2 = "[ENTRY 002] Efficiency increased by 347%"
    entry_3 = "[ENTRY 003] Archived by Data Archivist trainee"

    archive_file.write(entry_1 + "\n")
    archive_file.write(entry_2 + "\n")
    archive_file.write(entry_3 + "\n")
    archive_file.close()

    print(entry_1)
    print(entry_2)
    print(entry_3)
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
