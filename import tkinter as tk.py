import tkinter as tk
import random
import time

# Constants
WIDTH = 600
HEIGHT = 400
DELAY = 100
SEG_SIZE = 20

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, background="black")
        self.canvas.pack()

        self.snake = [(100,100), (80,100), (60,100)]
        self.food = self.create_food()

        self.score = 0
        self.direction = "Right"
        self.paused = False

        self.bind("<Key>", self.on_key_press)

        self.snake_move()

    def on_key_press(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "p":
            self.toggle_pause()

    def toggle_pause(self):
        self.paused = not self.paused

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH-SEG_SIZE) // SEG_SIZE) * SEG_SIZE
            y = random.randint(0, (HEIGHT-SEG_SIZE) // SEG_SIZE) * SEG_SIZE
            food = (x, y)
            if food not in self.snake:
                return food

    def snake_move(self):
        if not self.paused:
            head = self.snake[0]
            if self.direction == "Left":
                new_head = (head[0] - SEG_SIZE, head[1])
            elif self.direction == "Right":
                new_head = (head[0] + SEG_SIZE, head[1])
            elif self.direction == "Up":
                new_head = (head[0], head[1] - SEG_SIZE)
            elif self.direction == "Down":
                new_head = (head[0], head[1] + SEG_SIZE)

            self.snake.insert(0, new_head)

            if new_head == self.food:
                self.score += 1
                self.canvas.delete("food")
                self.food = self.create_food()
            else:
                self.snake.pop()

            self.canvas.delete("snake")
            for segment in self.snake:
                self.canvas.create_rectangle(segment[0], segment[1],
                                             segment[0] + SEG_SIZE, segment[1] + SEG_SIZE,
                                             fill="green", tag="snake")
            self.canvas.create_oval(self.food[0], self.food[1],
                                    self.food[0] + SEG_SIZE, self.food[1] + SEG_SIZE,
                                    fill="red", tag="food")

            if (self.snake[0][0] < 0 or self.snake[0][0] >= WIDTH or 
                self.snake[0][1] < 0 or self.snake[0][1] >= HEIGHT or 
                self.snake[0] in self.snake[1:]):
                self.game_over()
            else:
                self.after(DELAY, self.snake_move)

    def game_over(self):
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text=f"Game Over! Score: {self.score}", fill="white")

if __name__ == "__main__":
    app = SnakeGame()
    app.title("Snake Game")
    app.mainloop()
