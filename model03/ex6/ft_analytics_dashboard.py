scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 2050}

achs = {
    "alice": [
        "first_kill",
        "level_10",
        "boss_slayer",
        "first_kill",
        "level_10",
    ],
    "bob": ["first_kill", "level_10", "boss_slayer"],
    "charlie": [
        "first_kill",
        "level_10",
        "boss_slayer",
        "first_kill",
        "level_10",
        "boss_slayer",
        "first_kill",
    ],
    "diana": ["first_kill", "level_10", "boss_slayer"],
}

p_is_act = {"alice": True, "bob": True, "charlie": True, "diana": False}

p_reg = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "west",
}

print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")
high_scores = [name for name, score in scores.items() if score > 2000]
print(f"High scorers (>2000): {high_scores}")
doubled_scores = [score * 2 for score in scores.values()]
print(f"Scores doubled: {doubled_scores}")
active_players = [name for name, active in p_is_act.items() if active]
print(f"Active players: {active_players}\n")

print("=== Dict Comprehension Examples ===")
player_scores = {name: scores[name]
                 for name, active in p_is_act.items() if active}
print(f"Player scores: {player_scores}")

score_categories = {"high": 3, "medium": 2, "low": 1}
print(f"Score categories: {score_categories}")

achievement_counts = {name: len(achs[name])
                      for name, active in p_is_act.items() if active}
print(f"Achievement counts: {achievement_counts}\n")

print("=== Set Comprehension Examples ===")
unique_players = {name for name in scores}
print(f"Unique players: {unique_players}")

unique_achievements = {ach for achievements in achs.values()
                       for ach in achievements}
print(f"Unique achievements: {unique_achievements}")

active_regions = {p_reg[name] for name, active in p_is_act.items() if active}
print(f"Active regions: {active_regions}\n")

print("=== Combined Analysis ===")
total_players = len(scores)
print(f"Total players: {total_players}")
total_unique_achievements = sum(len(set(achs[name])) for name in scores)
print(f"Total unique achievements: {total_unique_achievements}")
average_score = 2062.5
print(f"Average score: {average_score:.1f}")
top_player = max(scores, key=scores.get)
print(
    f"Top performer: {top_player} ({scores[top_player]} points, "
    f"{len(achs[top_player])} achievements)"
)
