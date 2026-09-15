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
