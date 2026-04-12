import random


def gen_player_achievements() -> set[str]:
    """Generate random achievements for a player."""
    all_achievements = {
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Unstoppable",
        "Hidden Path Finder",
    }
    num_achievements = random.randint(4, 10)
    return set(random.sample(list(all_achievements), num_achievements))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements: dict[str, set[str]] = {}

    for player in players:
        player_achievements[player] = gen_player_achievements()
        print(f"Player {player}: {player_achievements[player]}")

    all_achievements = set()
    for achievements in player_achievements.values():
        all_achievements = all_achievements.union(achievements)
    print(f"\nAll distinct achievements: {all_achievements}")

    common = player_achievements["Alice"]
    for achievements in list(player_achievements.values())[1:]:
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")

    for player in players:
        only_player = player_achievements[player]
        for other_player in players:
            if other_player != player:
                msg = player_achievements[other_player]
                only_player = only_player.difference(msg)
        print(f"Only {player} has: {only_player}")

    for player in players:
        missing = all_achievements.difference(player_achievements[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
