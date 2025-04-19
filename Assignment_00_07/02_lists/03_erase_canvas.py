import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20
ERASER_COLOR = "pink"
CELL_COLOR = "blue"
ERASED_COLOR = "white"

class EraserCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.cells = []  # Store references to all blue cells

        self.create_grid()
        self.eraser = None
        self.dragging = False

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_eraser)
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        """Draw a grid of blue cells"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill=CELL_COLOR, outline="black"
                )
                self.cells.append(rect)

    def start_eraser(self, event):
        """Create the eraser on click"""
        if not self.eraser:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y,
                event.x + ERASER_SIZE, event.y + ERASER_SIZE,
                fill=ERASER_COLOR, outline=""
            )
        self.move_eraser(event)

    def move_eraser(self, event):
        """Move the eraser with the mouse and erase overlapping cells"""
        if self.eraser:
            # Move the eraser to the current mouse position
            self.canvas.coords(
                self.eraser,
                event.x, event.y,
                event.x + ERASER_SIZE, event.y + ERASER_SIZE
            )
            self.erase_overlapping(event.x, event.y)

    def erase_overlapping(self, x, y):
        """Set all overlapping rectangles to white"""
        overlapping = self.canvas.find_overlapping(
            x, y,
            x + ERASER_SIZE, y + ERASER_SIZE
        )

        for item in overlapping:
            # Avoid changing the eraser color itself
            if item != self.eraser:
                self.canvas.itemconfig(item, fill=ERASED_COLOR)

def main():
    root = tk.Tk()
    app = EraserCanvasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
