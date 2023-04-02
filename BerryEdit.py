import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path
import tkinter.font as tkFont
class BerryEdit:
    def __init__(self, master):

        self.master = master
        self.master.title("Pls End Me")
        self.master.geometry("1200x600")

        # Create a text area widget
        self.textarea = tk.Text(self.master, bg="black", fg="#ff03d1", insertbackground="white")
        self.textarea.pack(fill="both", expand=True)
        # Define the "font" tag with a default font size
        # Set the font size of the text area
        self.font = tkFont.Font(family="Arial", size=20)
        self.textarea.configure(font=self.font)
        # Bind Ctrl+S key event to save_file method
        self.master.bind("<Control-s>", self.save_file)
        self.master.bind("<Control-plus>", self.inc_size)
        self.master.bind("<Control-minus>", self.dec_size)

        # Bind Return key event to check for first line and format as cursive
        self.textarea.bind("<Return>", self.format_first_line)

        # Create a menu bar
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        # Create a File menu with Open, Save and Exit options
        file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_command(label="Open", command=self.open_file)
        self.menubar.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                self.textarea.delete("1.0", "end")
                self.textarea.insert("end", f.read())
    def inc_size(self, event=None):
        size = self.font.cget("size") + 2
        self.font.configure(size=size)
        if self.textarea.tag_ranges("cursive"):
            self.textarea.tag_config("cursive", font=("Arial", size-2, "italic"))
    def dec_size(self, event=None):
        if not self.font.cget("size") <=10: 
            size = self.font.cget("size") - 2
            self.font.configure(size=size)
            if self.textarea.tag_ranges("cursive"):
                self.textarea.tag_config("cursive", font=("Arial", size-2, "italic"))

    def save_file(self, event=None):
        desktop_path = str(Path.home() / "Desktop")
        filename = self.textarea.get("1.0", "1.end").strip() + ".txt"
        file_path = os.path.join(desktop_path, filename)
        with open(file_path, "w") as f:
            f.write(self.textarea.get("1.0", "end"))

    def format_first_line(self, event):
        first_line = self.textarea.get("1.0", "1.end-1c")
        if first_line.strip() and not self.textarea.tag_ranges("cursive"):
            self.textarea.tag_add("cursive", "1.0", "1.end")
            self.textarea.tag_config("cursive", font=("Arial", self.font.cget("size")-2, "italic"),foreground= "white")
        
        # Create a rainbow gradient effect for the text
        #rainbow_colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#8f00ff"]
        #start_index = 0
        #for i, char in enumerate(self.textarea.get("1.0", "end")):
        #    self.textarea.tag_add(f"color{i}", f"1.{i}", f"1.{i+1}")
        #    self.textarea.tag_config(f"color{i}", foreground=rainbow_colors[(i+start_index)%len(rainbow_colors)])

if __name__ == "__main__":
    root = tk.Tk()
    app = BerryEdit(root)
    root.mainloop()

