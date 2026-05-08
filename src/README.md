*This project has been created as part of the 42 curriculum alaktaou, mlaktaou.*

## Description

This project implements a maze generator with three algorithms (DFS, Prim, Hunt-and-Kill) and a Tkinter renderer for animation and visualization. It supports deterministic output with seeds, optional perfect or imperfect mazes, and exports the maze to a text file.

## Instructions

### Requirements

- Python 3.11 or later
- Tkinter (bundled with standard Python on Windows and most OS distributions)

### Run

```powershell
python a_maze_ing.py config.txt
```

### Optional

- Lint and type-check:

```powershell
flake8 .
mypy . --strict
```

## Resources

- Youtube: ALgorithms videos, and Maze Generation.
- AI: AI Assistans (DeepSeek, Gemeni, ChatGPT)

### AI usage

AI was used to:

- Review algorithm steps and suggest corrections to DFS, Prim, and Hunt-and-Kill logic.
- Propose safer rendering flow for Tkinter when closing the window during animation.
- Provide type-hinting guidance for mypy and identify None-guard issues.

AI was not used to write final output files for the maze or to generate visual assets.

## Configuration File

The configuration file is plain text with one key per line using `KEY=VALUE`. Example:

```
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=19,19
OUTPUT_FILE=maze.txt
ALGORITHM=prim
PERFECT=True
ANIMATION=False
SEED=42
CELL_SIZE=50
PADDING=20
```

### Fields

- `WIDTH`, `HEIGHT`: Maze dimensions in cells.
- `ENTRY`: Start cell as `x,y`.
- `EXIT`: Exit cell as `x,y`.
- `OUTPUT_FILE`: Output file name for the serialized maze.
- `ALGORITHM`: `dfs`, `prim`, or `hak`.
- `PERFECT`: `True` for no loops, `False` to allow loops.
- `ANIMATION`: `True` to animate generation, `False` to generate instantly.
- `SEED`: Optional integer seed for deterministic generation.
- `CELL_SIZE`: Pixel size of each cell in the renderer.
- `PADDING`: Padding around the maze in the renderer.

## Chosen Maze Algorithms

This project implements and compares three algorithms:

1. DFS (depth-first search)
2. Prim
3. Hunt-and-Kill

### Reasons for choosing them

- **DFS**: Simple to implement and produces long, winding corridors. Good baseline.
- **Prim**: Produces more uniform randomness and balanced corridor lengths.
- **Hunt-and-Kill**: Offers a different style and combines random walks with structured hunting.

## Reusable Maze Generator Module

The reusable core is the `Maze` class and algorithm classes in `algorithm.py`.

### Key usage

- Create a `Maze` with dimensions, entry/exit, and algorithm settings.
- Call `generate()` for a full maze or call step methods for animation.
- Use `MazeRenderer` to visualize generation and solution paths.

This separation allows the maze generator to be reused without the Tkinter renderer, for example in a CLI or another GUI.

## Team and Project Management

### Roles

- **alaktaou**: Core algorithms (DFS and Hunt and Kill), Maze, Mazerenderer integration and Setup package.
- **mlaktaou**: Configuration handling, Prim algorithm, Makefile and Code Enhancement.

### Planning and evolution

Initial planning started with research on maze algorithms, including tutorials and videos. A prototype was built without following the subject requirements to understand maze behavior. After that, each algorithm was studied and implemented with the project norms and requirements.

### What worked well

- Splitting algorithm logic from rendering made debugging and testing easier.
- Using type hints and mypy helped catch None cases and interface mismatches.

### What could be improved

- Add unit tests for each algorithm step.
- Provide more consistent naming across classes and files.

### Tools used

- VS Code
- Git
- Tkinter
- mypy
- flake8
