"""MLX-based graphical display for maze visualization.

This module provides a graphical interface using the MiniLibX library
to render mazes with walls, entry, exit, solution path, and pattern cells.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Optional

# Try to import MLX - fall back to ASCII-only if not available
MLX_AVAILABLE = False
MLX = None

try:
    from mlx import MLX
    MLX_AVAILABLE = True
except ImportError:
    try:
        from minilibx import MLX
        MLX_AVAILABLE = True
    except ImportError:
        MLX_AVAILABLE = False

from .generator import MazeData

# Default colors (RGB hex values)
DEFAULT_WALL_COLOR = 0xFFFFFF  # White
DEFAULT_PATH_COLOR = 0x00FF00  # Green
DEFAULT_ENTRY_COLOR = 0x00FFFF  # Cyan
DEFAULT_EXIT_COLOR = 0xFF00FF  # Magenta
DEFAULT_PATTERN_COLOR = 0xFF0000  # Red
DEFAULT_BG_COLOR = 0x000000  # Black

# Color presets for wall customization
COLOR_PRESETS = {
    "white": 0xFFFFFF,
    "red": 0xFF4444,
    "green": 0x44FF44,
    "blue": 0x4444FF,
    "yellow": 0xFFFF44,
    "cyan": 0x44FFFF,
    "magenta": 0xFF44FF,
    "orange": 0xFFAA44,
    "purple": 0xAA44FF,
    "pink": 0xFF88AA,
}


class MazeDisplayMLX:
    """Graphical maze display using MiniLibX."""

    def __init__(
        self,
        maze: MazeData,
        cell_size: int = 20,
        wall_color: int = DEFAULT_WALL_COLOR,
        path_color: int = DEFAULT_PATH_COLOR,
        entry_color: int = DEFAULT_ENTRY_COLOR,
        exit_color: int = DEFAULT_EXIT_COLOR,
        pattern_color: int = DEFAULT_PATTERN_COLOR,
        show_path: bool = True,
        show_pattern: bool = True,
    ) -> None:
        if not MLX_AVAILABLE:
            raise RuntimeError("MiniLibX is not available")

        self.maze = maze
        self.cell_size = cell_size
        self.wall_color = wall_color
        self.path_color = path_color
        self.entry_color = entry_color
        self.exit_color = exit_color
        self.pattern_color = pattern_color
        self.show_path = show_path
        self.show_pattern = show_pattern

        # Calculate window size
        self.width = (maze.width * 2 + 1) * cell_size
        self.height = (maze.height * 2 + 1) * cell_size

        # MLX instance
        self.mlx = MLX()
        self.window = self.mlx.new_window(
            self.width,
            self.height,
            "A-Maze-ing",
        )

    def _get_color(self, color_int: int) -> tuple[int, int, int]:
        """Convert integer color to RGB tuple."""
        r = (color_int >> 16) & 0xFF
        g = (color_int >> 8) & 0xFF
        b = color_int & 0xFF
        return (r, g, b)

    def _draw_walls(self) -> None:
        """Draw maze walls based on wall data."""
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                screen_x = x * 2 + 1
                screen_y = y * 2 + 1
                walls = self.maze.walls[y][x]

                # North wall
                if walls & 1 == 0:
                    self.mlx.fill_rect(
                        self.window,
                        screen_x * self.cell_size,
                        (screen_y - 1) * self.cell_size,
                        self.cell_size,
                        self.cell_size // 4,
                        self._get_color(self.wall_color),
                    )
                # South wall
                if walls & 4 == 0:
                    self.mlx.fill_rect(
                        self.window,
                        screen_x * self.cell_size,
                        (screen_y + 1) * self.cell_size,
                        self.cell_size,
                        self.cell_size // 4,
                        self._get_color(self.wall_color),
                    )
                # East wall
                if walls & 2 == 0:
                    self.mlx.fill_rect(
                        self.window,
                        (screen_x + 1) * self.cell_size,
                        screen_y * self.cell_size,
                        self.cell_size // 4,
                        self.cell_size,
                        self._get_color(self.wall_color),
                    )
                # West wall
                if walls & 8 == 0:
                    self.mlx.fill_rect(
                        self.window,
                        (screen_x - 1) * self.cell_size,
                        screen_y * self.cell_size,
                        self.cell_size // 4,
                        self.cell_size,
                        self._get_color(self.wall_color),
                    )

    def _draw_path(self) -> None:
        """Draw the solution path."""
        if not self.show_path:
            return
        path_cells = set(self.maze.solution)
        for x, y in path_cells:
            screen_x = x * 2 + 1
            screen_y = y * 2 + 1
            self.mlx.fill_rect(
                self.window,
                screen_x * self.cell_size + self.cell_size // 4,
                screen_y * self.cell_size + self.cell_size // 4,
                self.cell_size // 2,
                self.cell_size // 2,
                self._get_color(self.path_color),
            )

    def _draw_pattern(self) -> None:
        """Draw the 42 pattern cells."""
        if not self.show_pattern:
            return
        for x, y in self.maze.pattern_cells:
            screen_x = x * 2 + 1
            screen_y = y * 2 + 1
            self.mlx.fill_rect(
                self.window,
                screen_x * self.cell_size,
                screen_y * self.cell_size,
                self.cell_size,
                self.cell_size,
                self._get_color(self.pattern_color),
            )

    def _draw_entry_exit(self) -> None:
        """Draw entry and exit points."""
        # Entry
        entry_x, entry_y = self.maze.entry
        screen_x = entry_x * 2 + 1
        screen_y = entry_y * 2 + 1
        self.mlx.fill_rect(
            self.window,
            screen_x * self.cell_size,
            screen_y * self.cell_size,
            self.cell_size,
            self.cell_size,
            self._get_color(self.entry_color),
        )
        # Exit
        exit_x, exit_y = self.maze.exit_
        screen_x = exit_x * 2 + 1
        screen_y = exit_y * 2 + 1
        self.mlx.fill_rect(
            self.window,
            screen_x * self.cell_size,
            screen_y * self.cell_size,
            self.cell_size,
            self.cell_size,
            self._get_color(self.exit_color),
        )

    def render(self) -> None:
        """Render the entire maze."""
        # Clear background
        self.mlx.fill_rect(
            self.window,
            0,
            0,
            self.width,
            self.height,
            self._get_color(DEFAULT_BG_COLOR),
        )
        self._draw_walls()
        if self.show_path:
            self._draw_path()
        if self.show_pattern:
            self._draw_pattern()
        self._draw_entry_exit()

    def set_wall_color(self, color: int) -> None:
        """Change wall color."""
        self.wall_color = color

    def set_path_visibility(self, visible: bool) -> None:
        """Show or hide the solution path."""
        self.show_path = visible

    def set_pattern_visibility(self, visible: bool) -> None:
        """Show or hide the 42 pattern."""
        self.show_pattern = visible

    def run(self) -> None:
        """Main display loop."""
        self.render()
        self.mlx.loop(self.window)


def create_mlx_display(
    maze: MazeData,
    cell_size: int = 20,
    wall_color: str | int = "white",
    show_path: bool = True,
    show_pattern: bool = True,
) -> MazeDisplayMLX:
    """Factory function to create an MLX display."""
    if isinstance(wall_color, str):
        wall_color = COLOR_PRESETS.get(wall_color.lower(), DEFAULT_WALL_COLOR)

    return MazeDisplayMLX(
        maze=maze,
        cell_size=cell_size,
        wall_color=wall_color,
        show_path=show_path,
        show_pattern=show_pattern,
    )


__all__ = [
    "MazeDisplayMLX",
    "create_mlx_display",
    "COLOR_PRESETS",
    "MLX_AVAILABLE",
]