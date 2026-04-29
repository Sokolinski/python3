"""Command-line entry point for the A-Maze-ing project.

This CLI provides both batch and interactive modes for maze generation
and visualization using either ASCII or MiniLibX graphical display.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

# Ensure the local `src` package directory is importable when running this
# script from the repository root.
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from a_maze_ing.config_parser import ConfigError, parse_config
from a_maze_ing.generator import MazeGenerationError, MazeGenerator
from a_maze_ing.display import (
    MazeDisplayMLX,
    create_mlx_display,
    COLOR_PRESETS,
    MLX_AVAILABLE,
)




def generate_maze(config_path: str) -> tuple[MazeGenerator, Any]:
    """Generate a maze from config file."""
    config = parse_config(config_path)
    generator = MazeGenerator(
        width=config["WIDTH"],
        height=config["HEIGHT"],
        entry=config["ENTRY"],
        exit_=config["EXIT"],
        seed=config.get("SEED"),
        perfect=config["PERFECT"],
    )
    return generator, config


def display_ascii(maze: Any, show_path: bool = True, use_colors: bool = False) -> None:
    """Display maze as ASCII art."""
    print(maze.render_ascii(show_path=show_path, use_ansi_colors=use_colors))


def display_mlx(maze: Any, wall_color: str = "white", show_path: bool = True) -> None:
    """Display maze using MiniLibX."""
    if not MLX_AVAILABLE:
        print("Error: MiniLibX is not installed", file=sys.stderr)
        print("Install with: pip install minilibx", file=sys.stderr)
        return

    display = create_mlx_display(
        maze=maze,
        cell_size=20,
        wall_color=wall_color,
        show_path=show_path,
    )
    display.run()


def interactive_menu(config_path: str) -> None:
    """Interactive menu for maze visualization and manipulation."""
    generator, config = generate_maze(config_path)
    maze = generator.generate()

    show_path = True
    wall_color = "white"
    use_colors = False  # ANSI colors for ASCII mode

    # Display initial maze
    print("\nGenerated maze:")
    display_ascii(maze, show_path=show_path, use_colors=use_colors)

    while True:
        print("\n" + "=" * 50)
        print("       A-MAZE-ING INTERACTIVE MENU")
        print("=" * 50)
        print(f"  1. Re-generate a new maze and display it")
        print(f"  2. Show/Hide solution path (currently: {'SHOWN' if show_path else 'HIDDEN'})")
        print(f"  3. Change wall color (currently: {wall_color})")
        print("  0. Exit")
        print("-" * 50)

        choice = input("Select option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            # Re-generate a new maze and display it
            import random
            new_seed = random.randint(0, 999999)
            generator = MazeGenerator(
                width=config["WIDTH"],
                height=config["HEIGHT"],
                entry=config["ENTRY"],
                exit_=config["EXIT"],
                seed=new_seed,
                perfect=config["PERFECT"],
            )
            maze = generator.generate()
            print(f"New maze generated with seed: {new_seed}")
            display_ascii(maze, show_path=show_path, use_colors=use_colors)

        elif choice == "2":
            # Show/Hide solution path
            show_path = not show_path
            print(f"Solution path is now: {'SHOWN' if show_path else 'HIDDEN'}")
            display_ascii(maze, show_path=show_path, use_colors=use_colors)

        elif choice == "3":
            # Change wall color
            print(f"\nAvailable colors: {', '.join(COLOR_PRESETS.keys())}")
            color = input("Enter wall color name: ").strip().lower()
            if color in COLOR_PRESETS:
                wall_color = color
                print(f"Wall color set to: {wall_color}")
            else:
                print(f"Unknown color: {color}")

        else:
            print("Invalid option. Try again.")


def main(argv: list[str] | None = None) -> int:
    """Run the maze generator CLI."""

    arguments = sys.argv[1:] if argv is None else argv

    # Check for interactive mode flag
    if "-i" in arguments or "--interactive" in arguments:
        arguments = [a for a in arguments if a not in ("-i", "--interactive")]
        config_file = arguments[0] if arguments else "config.txt"
        interactive_menu(config_file)
        return 0

    # Batch mode (original behavior)
    if len(arguments) != 1:
        print("Usage: python3 a_maze_ing.py config.txt", file=sys.stderr)
        print("       python3 a_maze_ing.py -i config.txt  (interactive mode)", file=sys.stderr)
        return 1

    try:
        config = parse_config(arguments[0])
        generator = MazeGenerator(
            width=config["WIDTH"],
            height=config["HEIGHT"],
            entry=config["ENTRY"],
            exit_=config["EXIT"],
            seed=config.get("SEED"),
            perfect=config["PERFECT"],
        )
        maze = generator.generate()
        output_path = Path(config["OUTPUT_FILE"])
        output_path.write_text(maze.to_output_text(), encoding="utf-8")

        if maze.pattern_warning is not None:
            print(f"Warning: {maze.pattern_warning}", file=sys.stderr)

        print(maze.render_ascii())
        return 0
    except (ConfigError, MazeGenerationError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())


if __name__ == "__main__":
    raise SystemExit(main())
