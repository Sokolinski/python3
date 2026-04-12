import math


def get_player_pos() -> tuple[float, float, float]:
    """Get 3D coordinates from user input until valid."""
    while True:
        try:
            msg = "Enter new coordinates as floats in format 'x,y,z': "
            coord_str = input(msg)
            coords = coord_str.split(",")
            if len(coords) != 3:
                print("Invalid syntax")
                continue
            x = float(coords[0].strip())
            y = float(coords[1].strip())
            z = float(coords[2].strip())
            return (x, y, z)
        except ValueError as e:
            error_str = str(e)
            if "could not convert" in error_str:
                parts = error_str.split("'")
                if len(parts) >= 2:
                    invalid_val = parts[1]
                    print(f"Error on parameter '{invalid_val}': {e}")
                else:
                    print("Invalid syntax")
            else:
                print("Invalid syntax")


def calculate_distance(
    pos1: tuple[float, float, float], pos2: tuple[float, float, float]
) -> float:
    """Calculate 3D Euclidean distance between two points."""
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    center = (0.0, 0.0, 0.0)
    dist_to_center = calculate_distance(pos1, center)
    print(f"Distance to center: {dist_to_center:.4f}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
