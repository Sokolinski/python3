def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter',
               'boss_slayer', 'speed_demon', 'perfectionist'}

    print(f"Player alice achievement: {alice}")
    print(f"Player bob achievement: {bob}")
    print(f"Player charlie achievement: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_uniq = alice.union(alice, bob, charlie)
    print(f"All unique achievements: {all_uniq}")
    print(f"Total unique achievements: {len(all_uniq)}")
    all_common = alice.intersection(alice, bob, charlie)
    print(f"\nCommon to all players:{all_common}")
    rare_achive = (alice.union(bob, charlie)) -\
        (alice & bob) - (alice & charlie) - (bob & charlie)
    print(f"Rare achievemen{rare_achive}")
    alice_and_bob = alice.intersection(bob)
    print(f"Alice vs Bob common:{alice_and_bob}")
    alice_uniq = alice.difference(bob)
    print(f"Alice unique{alice_uniq}")
    bob_uniq = bob.difference(alice)
    print(f"Bob unique{bob_uniq}")


if __name__ == "__main__":
    main()
