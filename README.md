# A-Maze-ing
## Description

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-black)](https://flake8.pycqa.org/)
[![Mypy](https://img.shields.io/badge/type%20checked-mypy-blue)](http://mypy-lang.org/)

A Python maze generator that implements **three different algorithms** (DFS, Prim, Hunt‑and‑Kill) with an **interactive Tkinter visualizer**. Watch the maze being built step by step, show/hide the shortest path, and export the result to a standard hex‑based file format.

![Maze generation demo](https://via.placeholder.com/800x400?text=Screenshot+of+maze+visualization)  
*(Add a real screenshot or GIF here)*

## ✨ Features

- 🧠 **Three generation algorithms** – DFS (winding corridors), Prim (balanced randomness), Hunt‑and‑Kill (unique mix)
- 🎨 **Live animation** – watch the maze being carved in real time (optional)
- 🔁 **Perfect or imperfect** – choose `PERFECT=True` for a tree‑like maze (unique path) or `False` for loops
- 🧩 **Embedded “42” pattern** – the maze contains the digits “42” made of solid cells
- 🖥️ **Tkinter visualizer** – interactive window with:
  - regenerate new maze
  - toggle shortest path (E → X)
  - cycle through wall colours
  - adjust animation speed
- 📁 **File export** – writes a standard `.txt` maze using hexadecimal wall encoding (one hex digit per cell)

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or later
- Tkinter (usually included with Python on Windows / macOS / most Linux distros)

### Installation

```bash
git clone https://github.com/yourusername/a-maze-ing.git
cd a-maze-ing
```

No extra dependencies – uses only the standard library + Tkinter.

### Run

```bash
python a_maze_ing.py config.txt
```

A default `config.txt` is provided. You can edit it to change maze size, entry/exit, algorithm, etc.

## ⚙️ Configuration

Plain text file with `KEY=VALUE` entries. Example:

```ini
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=19,19
OUTPUT_FILE=maze.txt
ALGORITHM=prim
PERFECT=True
ANIMATION=True
SEED=42
CELL_SIZE=50
PADDING=20
```

| Key           | Values                                 | Description                          |
|---------------|----------------------------------------|--------------------------------------|
| `WIDTH`       | integer                                | Number of cells horizontally         |
| `HEIGHT`      | integer                                | Number of cells vertically           |
| `ENTRY`       | `x,y`                                  | Starting cell coordinates            |
| `EXIT`        | `x,y`                                  | Target cell coordinates              |
| `OUTPUT_FILE` | filename                               | Where to save the maze               |
| `ALGORITHM`   | `dfs` / `prim` / `hak`                 | Algorithm to use                     |
| `PERFECT`     | `True` / `False`                       | If `True`, no loops (spanning tree)   |
| `ANIMATION`   | `True` / `False`                       | Animate generation step by step      |
| `SEED`        | integer (optional)                     | Deterministic randomness             |
| `CELL_SIZE`   | pixels                                 | Size of each cell in the visualizer  |
| `PADDING`     | pixels                                 | Margin around the maze window        |

## 🧠 Algorithms & Why

| Algorithm       | Characteristics                                                                 | Why chosen                               |
|----------------|---------------------------------------------------------------------------------|------------------------------------------|
| **DFS** (recursive backtracker) | Long, winding corridors; tends to create a single long path.                   | Simple, classic, produces “snake‑like” mazes. |
| **Prim**       | Uniform randomness, many short branches, looks more “natural”.                 | Produces mazes with balanced corridor lengths. |
| **Hunt‑and‑Kill** | Random walk until stuck, then “hunt” for an unvisited cell.                   | Unique behaviour – mixes exploration and scanning. |

All three can generate **perfect mazes** (spanning trees) when `PERFECT=True`. The implementation is fully deterministic when a `SEED` is provided.

## 🧩 Reusable Module

The core logic (`Maze` class and algorithm classes) lives in `mazegen/` and can be installed and reused independently of the Tkinter visualizer.

```python
from mazegen import Maze

maze = Maze(width=40, height=30, algorithm="prim", perfect=True, seed=123)
maze.generate()

# Access internal grid (list of lists of Cells)
grid = maze.grid

# Export to the required file format
maze.export_to_file("my_maze.txt", entry=(0,0), exit=(39,29))
```

## 🖼️ Visual Controls

When running with `ANIMATION=True`, the Tkinter window provides:

- **`r`** – regenerate a new maze (same settings)
- **`p`** – show/hide the shortest path
- **`c`** – cycle through wall colour themes
- **`+` / `-`** – increase/decrease animation delay
- **`q`** – quit

## 🛠️ Development

Lint and type‑check with:

```bash
flake8 .
mypy . --strict
```

---

<p align="center">
  Made with 🐍 by <a href="https://github.com/alaktaou">alaktaou</a> & <a href="https://github.com/mlaktaou">mlaktaou</a>
</p>
