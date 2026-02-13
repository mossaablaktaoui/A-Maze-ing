import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

canvas.create_rectangle(
    0, 0, 100, 100,
    fill="red",
    outline="",
    width=3
)

root.mainloop()
