# Scramble Solver

Finds every valid word in a 4x4 Word Hunt / Boggle-style letter grid.

Boards can be entered manually. A screenshot-upload feature (using OCR to read the
grid automatically) is planned but not yet implemented.

## Requirements

Currently needed (core solver):

- OS: Windows 11 Pro (10.0.26200) — should also run on any OS with Python installed
- Python 3.12.3

Planned, not yet needed (web app + screenshot input):

- Flask, for the web interface
- Tesseract OCR (system install) + the `pytesseract` Python package, for reading a
  board from an uploaded screenshot

## How to run

```
git clone https://github.com/kevnugget/ScrambleSolver.git
cd ScrambleSolver
python
```

Then in the Python prompt:

```python
from solver import load_dictionary, find_words

grid = [
    ["C", "A", "T", "S"],
    ["O", "R", "E", "N"],
    ["D", "O", "G", "S"],
    ["B", "I", "R", "D"],
]

dictionary = load_dictionary("words.txt")
words = find_words(grid, dictionary)
print(sorted(words))
```

## Files

- `solver.py` — grid search logic (bounds checking, adjacency, DFS, dictionary loading)
- `words.txt` — dictionary of valid words (ENABLE word list, ~172,000 words)
