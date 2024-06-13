def island_perimeter(grid):
    """
    This function calculates the perimeter of the island in the given grid.

    Args:
    grid (list): A 2D list of integers 
    where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """

    if not grid:
        return 0

    perimeter = 0

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check the top cell
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the right cell
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                # Check the bottom cell
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the left cell
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

    return perimeter
