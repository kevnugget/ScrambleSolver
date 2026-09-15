def in_bounds(row, column):
    """Return True if (row, column) is inside the 4x4 grid."""
    return 0 <= row < 4 and 0 <= column < 4


def neighbors(row, column):
    """Return the coordinates of all cells adjacent to (row, column), including diagonals."""
    adjacent = []
    for row_step in (-1, 0, 1):
        for column_step in (-1, 0, 1):
            if row_step == 0 and column_step == 0:
                continue
            next_row = row + row_step
            next_column = column + column_step
            if in_bounds(next_row, next_column):
                adjacent.append((next_row, next_column))
    return adjacent


def search_from(grid, row, column, visited, path, dictionary, found):
    """Recursively extend path from (row, column), recording any dictionary words found."""
    visited.add((row, column))
    path += grid[row][column]

    if len(path) >= 3 and path in dictionary:
        found.add(path)

    for next_row, next_column in neighbors(row, column):
        if (next_row, next_column) not in visited:
            search_from(grid, next_row, next_column, visited, path, dictionary, found)

    visited.remove((row, column))
