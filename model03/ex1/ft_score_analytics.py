import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argv = sys.argv
    if len(argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    try:
        scores = [int(arg) for arg in argv[1:]]
    except ValueError:
        print("Invalid input: all arguments must be integers")
        return

    print(f"Scores processed: {argv[1:]}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
