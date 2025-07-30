import tkinter as tk
from tkinter import messagebox
import os

# ====================== Contact Storage ======================
contacts = []
FILE_NAME = "contacts.txt"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 1:
                contact = {
                    
                    "Name": data[0],
                    "Phone": data[1],
                    "Email": data[2],
                    "Address": data[3]
                }
                contacts.append(contact)

def save_contacts():
    with open(FILE_NAME, "w") as f:
        for c in contacts:
            line = "|".join([c["Name"], c["Phone"], c["Email"], c["Address"]])
            f.write(line + "\n")

# ====================== Theme Setup ======================
theme = "light"
themes = {
    "light": {
        "bg": "#f0f4f8", "fg": "#000", "entry_bg": "white", "button_fg": "white",
        "buttons": {
            "Add": "#4CAF50", "Update": "#2196F3",
            "Delete": "#f44336", "Clear": "#9E9E9E", "Search": "#1679A4"
        }
    },
    "dark": {
        "bg": "#2b2b2b", "fg": "#fff", "entry_bg": "#3c3f41", "button_fg": "white",
        "buttons": {
            "Add": "#388e3c", "Update": "#1976D2",
            "Delete": "#d32f2f", "Clear": "#757575", "Search": "#1394d5"
        }
    }
}

def toggle_theme():
    global theme
    theme = "dark" if theme == "light" else "light"
    apply_theme()

def apply_theme():
    th = themes[theme]
    root.configure(bg=th["bg"])
    title_label.config(bg=th["bg"], fg=th["fg"])
    frame.config(bg=th["bg"])
    btn_frame.config(bg=th["bg"])
    search_frame.config(bg=th["bg"])
    list_frame.config(bg=th["bg"])
    contact_listbox.config(bg=th["entry_bg"], fg=th["fg"])

    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=th["bg"], fg=th["fg"])
        elif isinstance(widget, tk.Entry):
            widget.config(bg=th["entry_bg"], fg=th["fg"])

    for text, button in button_widgets.items():
        button.config(bg=th["buttons"][text], fg=th["button_fg"])

    search_entry.config(bg=th["entry_bg"], fg=th["fg"])
    search_btn.config(bg=th["buttons"]["Search"], fg=th["button_fg"])
    toggle_btn.config(bg=th["entry_bg"], fg=th["fg"])

# ====================== Contact Functions ======================
def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    address = address_var.get().strip()
    

    if not name or not phone:
        messagebox.showwarning("Required", "Name and Phone are required.")
        return

    contact = { "Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    save_contacts()
    update_contact_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully.")

def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")
        return

    index = selected[0]
    contacts[index] = {
        
        "Name": name_var.get(),
        "Phone": phone_var.get(),
        "Email": email_var.get(),
        "Address": address_var.get()
    }
    save_contacts()
    update_contact_list()
    clear_fields()
    messagebox.showinfo("Updated", "Contact updated successfully.")

def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return

    index = selected[0]
    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
    if confirm:
        contacts.pop(index)
        save_contacts()
        update_contact_list()
        clear_fields()
        messagebox.showinfo("Deleted", "Contact deleted successfully.")

def search_contact():
    term = search_var.get().lower()
    filtered = [c for c in contacts if term in c["Name"].lower() or term in c["Phone"]]
    update_contact_list(filtered)

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")
   

def show_contact_details(event):
    selected = contact_listbox.curselection()
    if not selected:
        return
    index = selected[0]
    contact = contacts[index]
    name_var.set(contact["Name"])
    phone_var.set(contact["Phone"])
    email_var.set(contact["Email"])
    address_var.set(contact["Address"])
    

def update_contact_list(filtered=None):
    contact_listbox.delete(0, tk.END)
    display_list = filtered if filtered is not None else contacts
    for c in display_list:
        contact_listbox.insert(tk.END, f"{c['Name']} - {c['Email']} - {c['Phone']} - {c['Address']}")

# ====================== UI Setup ======================
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")

title_label = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

fields = [("Name", name_var), ("Phone", phone_var),
          ("Email", email_var), ("Address", address_var)]

for i, (label, var) in enumerate(fields):
    tk.Label(frame, text=label, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(frame, textvariable=var, width=30).grid(row=i, column=1, padx=10, pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

button_widgets = {}
button_widgets["Add"] = tk.Button(btn_frame, text="Add Contact", command=add_contact, width=15)
button_widgets["Add"].grid(row=0, column=0, padx=5)

button_widgets["Update"] = tk.Button(btn_frame, text="Update Contact", command=update_contact, width=15)
button_widgets["Update"].grid(row=0, column=1, padx=5)

button_widgets["Delete"] = tk.Button(btn_frame, text="Delete Contact", command=delete_contact, width=15)
button_widgets["Delete"].grid(row=0, column=2, padx=5)

button_widgets["Clear"] = tk.Button(btn_frame, text="Clear Fields", command=clear_fields, width=15)
button_widgets["Clear"].grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
search_entry.grid(row=0, column=0, padx=5)

search_btn = tk.Button(search_frame, text="Search", command=search_contact)
search_btn.grid(row=0, column=1, padx=5)

toggle_btn = tk.Button(search_frame, text="🌗 Toggle Theme", command=toggle_theme)
toggle_btn.grid(row=0, column=2, padx=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

tk.Label(list_frame, text="Contacts List", font=("Arial", 14, "bold")).pack()

contact_listbox = tk.Listbox(list_frame, width=50, height=10)
contact_listbox.pack()
contact_listbox.bind("<<ListboxSelect>>", show_contact_details)

# ====================== Initialize ======================
load_contacts()
update_contact_list()
apply_theme()
root.mainloop()
