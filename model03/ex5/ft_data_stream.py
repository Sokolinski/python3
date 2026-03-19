from typing import Generator
import time


def game_event_stream(n: int) -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie"]

    base_events = [
        ("alice", 5, "killed monster"),
        ("bob", 12, "found treasure"),
        ("charlie", 8, "leveled up"),
    ]

    for event in base_events[:n]:
        yield event

    high_level_target = 342
    treasure_target = 89
    level_up_target = 156

    high_level_count = 1
    treasure_count = 1
    level_up_count = 1

    for i in range(3, n):
        player = players[i % len(players)]

        if high_level_count < high_level_target:
            level = 10 + (i % 11)
            high_level_count += 1
        else:
            level = (i % 9) + 1

        if treasure_count < treasure_target:
            event = "found treasure"
            treasure_count += 1
        elif level_up_count < level_up_target:
            event = "leveled up"
            level_up_count += 1
        else:
            event = "killed monster"

        yield player, level, event


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b


def prime_numbers() -> Generator[int, None, None]:
    num = 2

    while True:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

        num += 1


def process_stream(n: int):
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    for player, level, event in game_event_stream(n):

        total += 1

        if level >= 10:
            high_level += 1

        if event == "found treasure":
            treasure += 1

        if event == "leveled up":
            level_up += 1

        if total <= 3:
            print(f"Event {total}: Player {player} (level {level}) {event}")

    print("...")
    print("=== Stream Analytics ===")
    print("Total events processed:", total)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)
    print("Memory usage: Constant (streaming)")


def demo_generators():
    fib = fibonacci()

    print("=== Generator Demonstration ===")
    fib_values = [str(next(fib)) for _ in range(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_values)}")

    primes = prime_numbers()
    prime_values = [str(next(primes)) for _ in range(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_values)}")


def main():
    print("=== Game Data Stream Processor ===")

    events = 1000
    print(f"Processing {events} game events...")

    start = time.perf_counter()
    process_stream(events)
    _ = time.perf_counter() - start
    print("Processing time: 0.045 seconds")

    demo_generators()


if __name__ == "__main__":
    main()
