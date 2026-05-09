# A-Maze-ing
## Description

A Python maze generator that implements **three different algorithms** (DFS, Prim, Hunt‑and‑Kill) with an **interactive Tkinter visualizer**. Watch the maze being built step by step, show/hide the shortest path, and export the result to a standard hex‑based file format.

<p align="center">
  <img src="https://github.com/mossaablaktaoui/Assests/blob/main/Screenshot%20from%202026-05-08%2018-47-42.png?raw=true" width="30%" />
  <img src="https://github.com/mossaablaktaoui/Assests/blob/main/Screenshot%20from%202026-05-08%2018-48-15.png?raw=true" width="30%" />
</p>

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
make install
```

No extra dependencies – uses only the standard library + Tkinter.

### Run

```bash
make run
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

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/mossaablaktaoui/Assests/blob/main/Screenshot%20from%202026-05-08%2018-55-33.png?raw=true" width="400"/><br>
      <b>Prim</b>
    </td>
    <td align="center">
      <img src="https://github.com/mossaablaktaoui/Assests/blob/main/Screenshot%20from%202026-05-08%2018-57-14.png?raw=true" width="400"/><br>
      <b>BFS</b>
    </td>
    <td align="center">
      <img src="https://github.com/mossaablaktaoui/Assests/blob/main/Screenshot%20from%202026-05-08%2018-58-38.png?raw=true" width="400"/><br>
      <b>Hunt and Kill</b>
    </td>
  </tr>
</table>

All three can generate **perfect mazes** (spanning trees) when `PERFECT=True`. The implementation is fully deterministic when a `SEED` is provided.

## 🧩 Reusable Module

The core logic (`Maze` class and algorithm classes) lives in `mazegen/` and can be installed and reused independently of the Tkinter visualizer.

```python
from mazegen import Maze

maze = Maze(
    width=40,
    height=30,
    entry=(0, 0),
    exit_=(39, 29),
    perfect=True,
    algorithm="prim",
    animation=False,
    seed=123
)

# Generate the maze
maze.algorithm.generate()

# Access internal cells
cells = maze.cells

# Find shortest path
maze.find_shortest_path()

# Export maze to file
maze.write_to_file("my_maze.txt")
```

## 🖼️ Visual Controls

When running with `ANIMATION=True`, the Tkinter window provides:

- **`1`** – regenerate a new maze (same settings)
- **`2`** – show/hide the shortest path
- **`3`** – cycle through wall colour themes
- **`4`** – quit

## 🛠️ Development

Lint and type‑check with:

```bash
flake8 .
mypy . --strict
```

---

<p align="center">
  Made by <a href="https://github.com/mossaablaktaoui">Mossaab Laktaoui</a> & <a href="https://github.com/abdelfatah89">Abdelfatah Laktaoui</a>
</p>

<p align="right"><code>This project was completed in 16 February 2026.</code></p>
