from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Generate random game events."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "move", "grab", "release", "sleep", "eat", "climb",
               "swim", "use"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    """Consume events from a list randomly until empty."""
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()
    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    event_gen = gen_event()
    event_list = [next(event_gen) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
    main()
