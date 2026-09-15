def in_bounds(row, column):
    """Return True if (row, column) is inside the 4x4 grid."""
    return 0 <= row < 4 and 0 <= column < 4
