import tkinter as tk


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True,
        }
        self.visited = False
        self.cell_size = 50
        self.in_solution = False
        self.parent = None

    def draw_current_cell(self, canvas: tk.Canvas,
                          color: str = 'lightgrey') -> None:
        canvas.create_rectangle(
            20 + self.x * self.cell_size,
            20 + self.y * self.cell_size,
            20 + (self.x + 1) * self.cell_size,
            20 + (self.y + 1) * self.cell_size,
            fill=color,
            outline=''
        )

    def get_wall_coordinates(self, grid_x, grid_y, position):
        padding = 20
        x = padding + (grid_x * self.cell_size)
        y = padding + (grid_y * self.cell_size)

        if position == 'top':
            return (x, y, x + self.cell_size, y)
        elif position == 'bottom':
            return (x, y + self.cell_size,
                    x + self.cell_size, y + self.cell_size)
        elif position == 'left':
            return (x, y, x, y + self.cell_size)
        elif position == 'right':
            return (x + self.cell_size, y,
                    x + self.cell_size, y + self.cell_size)

    def draw_walls(self, canvas: tk.Canvas):
        for key in self.walls.keys():
            if self.walls[key]:
                coordinates = self.get_wall_coordinates(self.x, self.y, key)
                canvas.create_line(*coordinates, width=3)
            
        if self.walls['top']:
            coordinates = self.get_wall_coordinates(self.x, self.y, 'top')
            canvas.create_line(*coordinates, width=3)
        if self.walls['right']:
            coordinates = self.get_wall_coordinates(self.x, self.y, 'right')
            canvas.create_line(*coordinates, width=3)
        if self.walls['bottom']:
            coordinates = self.get_wall_coordinates(self.x, self.y, 'bottom')
            canvas.create_line(*coordinates, width=3)
        if self.walls['left']:
            coordinates = self.get_wall_coordinates(self.x, self.y, 'left')
            canvas.create_line(*coordinates, width=3)
