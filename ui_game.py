import tkinter as tk

# Game Data
stack = ["A", "B", "C", "D"]
positions = {t: 0 for t in stack}

# Window
root = tk.Tk()
root.title("Tiki Topple Game")

# Display Label
label = tk.Label(root, text="", font=("Arial", 14))
label.pack()

# Update Display
def update_display():
    text = "Stack (Top → Bottom): " + " ".join(stack) + "\n"
    text += "Positions:\n"
    for t in positions:
        text += f"{t}: {positions[t]}  "
    label.config(text=text)

# Move Function
def move_tokens(n):
    for i in range(n):
        positions[stack[i]] += 1
    update_display()

# Reorder Function
def reorder():
    if len(stack) >= 2:
        stack[0], stack[1] = stack[1], stack[0]
    update_display()

# Buttons
tk.Button(root, text="Move 1", command=lambda: move_tokens(1)).pack()
tk.Button(root, text="Move 2", command=lambda: move_tokens(2)).pack()
tk.Button(root, text="Move 3", command=lambda: move_tokens(3)).pack()

tk.Button(root, text="Reorder Top 2", command=reorder).pack()

# Start
update_display()
root.mainloop()