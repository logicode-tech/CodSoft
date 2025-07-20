import tkinter as tk

def btn_click(char):
    entry_var.set(entry_var.get() + char)

def clear_input():
    entry_var.set("")

def evaluate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def key_handler(event):
    key = event.char
    if key in "0123456789+-*/.":
     btn_click(key)
    elif event.keysym == 'Return':
        evaluate()
    elif event.keysym == 'BackSpace':
        entry_var.set(entry_var.get()[:-1])

# Hover effect functions
def on_enter(event):
    event.widget['bg'] = hover_bg

def on_leave(event):
    event.widget['bg'] = normal_bg

# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.resizable(False, False)
root.configure(bg="#386f89")

# Colors
hover_bg = "#337393"
normal_bg = "#FAF2F2"

# Heading
tk.Label(root, text="Calculator", font=("Arial", 20, "bold")).pack(pady=10)

# Main Frame with grid layout
main_frame = tk.Frame(root)
main_frame.pack()

# Entry Field (3-column wide)
entry_var = tk.StringVar()
entry = tk.Entry(main_frame, textvariable=entry_var, font=("Arial", 20), bd=8, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button definitions
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

# Create buttons using grid layout
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        if char == '=':
            btn = tk.Button(main_frame, text=char, font=("Arial", 18), bg=normal_bg, command=evaluate)
            btn.grid(row=r, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        elif char == 'C':
            btn = tk.Button(main_frame, text=char, font=("Arial", 18), bg=normal_bg, command=clear_input)
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
        else:
            btn = tk.Button(main_frame, text=char, font=("Arial", 18), bg=normal_bg, command=lambda x=char: btn_click(x))
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        # Add hover effects
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

# Configure uniform row/column weights
for i in range(5):
    main_frame.rowconfigure(i, weight=1)
for j in range(4):
    main_frame.columnconfigure(j, weight=1)

# Keyboard bindings
root.bind("<Key>", key_handler)

# Start the app
root.mainloop()
