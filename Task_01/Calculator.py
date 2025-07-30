import tkinter as tk

def click(event=None):
    widget = event.widget
    text = widget.cget("text")
    animate_button(widget)
    process_input(text)

def key_press(event):
    char = event.char
    if char in "0123456789.+-*/":
        screen.set(screen.get() + char)
    elif char == "\r":
        calculate()
    elif char == "\x08":
        screen.set(screen.get()[:-1])

def process_input(char):
    if char == "=":
        calculate()
    elif char == "C":
        screen.set("")
    else:
        screen.set(screen.get() + char)

def calculate():
    try:
        result = str(eval(screen.get()))
        screen.set(result)
    except:
        screen.set("Error")

def animate_button(btn):
    original = btn["bg"]
    btn.config(bg="#EADDDD", fg="#222831")
    btn.after(100, lambda: btn.config(bg=original, fg="white"))

def on_enter(e):
    e.widget.config(bg="#69A491", fg="#222831", relief="raised", bd=2)

def on_leave(e):
    btn = e.widget
    btn_text = btn.cget("text")
    color = "#8297B3" if btn_text in {"=", "C"} else "#393E46"
    btn.config(bg=color, fg="white", relief="flat", bd=0)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")
root.configure(bg="#222831")

# Entry field
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Helvetica", 18), bd=0,
                 bg="#393E46", fg="white", insertbackground="white", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, pady=20, padx=20)

# Bind keyboard input
root.bind("<Key>", key_press)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

# Create buttons with hover and shadow
for row in buttons:
    frame = tk.Frame(root, bg="#101113")
    for btn_text in row:
        color = "#78EFF6" if btn_text in {"=", "C"} else "#393E46"
        btn = tk.Button(frame, text=btn_text, font=("arial", 16),
                        bg=color, fg="white",
                        activebackground="#3FD4C5", activeforeground="#14B97A",
                        relief="flat", padx=10, pady=10, bd=0)
        btn.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        btn.bind("<Button-1>", click)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
    frame.pack(expand=True, fill="both", padx=10)

root.mainloop()
