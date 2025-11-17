import tkinter as tk

# Function to safely evaluate expressions
def safe_eval(expr):
    try:
        # Only allow safe operations (no variables or imports)
        allowed_chars = "0123456789+-*/(). "
        if all(ch in allowed_chars for ch in expr):
            return eval(expr)
        else:
            return "Error"
    except Exception:
        return "Error"

# Handle button click events
def button_click(value):
    current = expression_label["text"]

    if value == "AC":
        expression_label.config(text="")
    elif value == "⌫":
        expression_label.config(text=current[:-1])
    elif value == "=":
        result = safe_eval(current)
        if result == "Error":
            expression_label.config(text="Error")
        else:
            expression_label.config(text=f"{current}\n\n{' ' * 10}Ans = {result}")
    else:
        # Start new expression if previous result is displayed
        if "Ans =" in current or current == "Error":
            expression_label.config(text=value)
        else:
            expression_label.config(text=current + value)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("360x580")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Display Label
expression_label = tk.Label(
    root,
    text="",
    font=("Consolas", 20),
    bg="#f0f0f0",
    anchor="e",      # Right align like a real calculator
    justify="right",
    relief="sunken",
    bd=5,
    width=22,
    height=3
)
expression_label.pack(pady=10, padx=10, fill="x")

# Frame for buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

# Button layout
buttons = [
    ["AC", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "(", ")"]
]

# Create buttons dynamically
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        color = "#d4d4d2" if char not in {"AC", "⌫", "=", "+", "-", "*", "/"} else "#ffcc00"
        active_color = "#b3b3b3" if char not in {"AC", "⌫", "=", "+", "-", "*", "/"} else "#ffb84d"

        btn = tk.Button(
            button_frame,
            text=char,
            font=("Consolas", 18, "bold"),
            width=5,
            height=2,
            bg=color,
            activebackground=active_color,
            relief="raised",
            command=lambda ch=char: button_click(ch)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)


root.mainloop()