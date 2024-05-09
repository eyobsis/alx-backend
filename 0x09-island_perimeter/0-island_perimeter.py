#!/usr/bin/python3

"""
Island Perimeter Calculator

This module calculates the perimeter of an island in a grid.

"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid: A 2D array of integers representing the grid.
            0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.

    """
    island_edges = 0
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                # Check top boundary
                if row_idx == 0 or grid[row_idx - 1][col_idx] == 0:
                    island_edges += 1
                # Check bottom boundary
                if row_idx == len(grid) - 1 or grid[row_idx + 1][col_idx] == 0:
                    island_edges += 1
                # Check left boundary
                if col_idx == 0 or grid[row_idx][col_idx - 1] == 0:
                    island_edges += 1
                # Check right boundary
                if col_idx == len(row) - 1 or grid[row_idx][col_idx + 1] == 0:
                    island_edges += 1
    return island_edges


if __name__ == "__main__":
    pass
