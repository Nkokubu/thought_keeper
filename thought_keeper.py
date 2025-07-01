import tkinter as tk
from tkinter import messagebox, Menu
from datetime import datetime
import os

def get_journal_filename():
    today = datetime.today().strftime("%Y-%m-%d")
    journal_dir = "journals"
    os.makedirs(journal_dir, exist_ok=True)
    return os.path.join(journal_dir, f"{today}-journal.txt")

def save_entry():
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Entry", "Write something before saving!")
        return

    filename = get_journal_filename()
    with open(filename, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%H:%M")
        file.write(f"\n[{timestamp}]\n{text}\n")

    messagebox.showinfo("Saved", f"Your entry has been saved to:\n{filename}")
    text_area.delete("1.0", tk.END)

def exit_app():
    root.quit()

# GUI setup
root = tk.Tk()
root.title("📝 Daily Journal")
root.geometry("600x500")

# Menu bar setup
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save Entry", command=save_entry)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Title label
title_label = tk.Label(root, text="Your Daily Journal", font=("Helvetica", 16))
title_label.pack(pady=10)

# Text area
text_area = tk.Text(root, wrap="word", font=("Helvetica", 12))
text_area.pack(padx=10, pady=5, expand=True, fill="both")

# Save button
save_button = tk.Button(root, text="Save Entry", font=("Helvetica", 12), command=save_entry)
save_button.pack(pady=10)

# Start GUI
root.mainloop()
