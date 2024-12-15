import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox



class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Database Example")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("testdb.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
        self.conn.commit()

        # Create GUI elements
        self.top_image = tk.PhotoImage(file="image/topbar.png")
        self.top_image_label = tk.Label(root, image=self.top_image,)
        self.top_image_label.pack()
        self.top_image_label.place(x=0,y=0)        

        self.task_image = tk.PhotoImage(file="image/task.png")
        self.task_image_label = tk.Label(root, image=self.task_image, bg="#32405b")
        self.task_image_label.pack()
        self.task_image_label.place(x=30,y=25)

        heading = Label(root, text="All Task", font="arial 20 bold", fg="white", bg="#32405b")
        heading.place(x=130, y=20)


        frame = Frame(root, width=400, height=50, bg="white")
        frame.place(x=0, y=70)

        task = StringVar()
        self.task_entry = Entry(frame, width=18, font="arial 20", bd=0, textvariable=task)
        self.task_entry.place(x=10, y=7)
        self.task_entry.focus()

        button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=self.add_task)
        button.place(x=300, y=0)

        # Listbox
        framel = Frame(root, bd=3, width=400, height=400, bg="#32405b")
        framel.pack(pady=(160, 0))

        self.listbox = Listbox(
            framel,
            font=('arial', 12),
            width=40,
            height=16,
            bg="#32405b",
            fg="white",
            cursor="hand2",
            selectbackground="#5a95ff"
        )
        self.listbox.pack(side=LEFT, fill=BOTH, padx=2)

        scrollbar = Scrollbar(framel)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.load_tasks()

        self.Delete_icon = PhotoImage(file="image/delete.png")
        Button(root, image=self.Delete_icon, bd=0, command=self.delete_task).pack(side=BOTTOM, pady=13)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            self.conn.commit()
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please input a task.")

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        for row in tasks:
            self.listbox.insert(tk.END, row[1])

    def delete_task(self):
        selected_task = self.listbox.get(tk.ACTIVE)
        if selected_task:
            self.cursor.execute("DELETE FROM tasks WHERE task=?", (selected_task,))
            self.conn.commit()
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TO_DO_LIST")
    root.geometry("400x650+400+100")
    root.resizable(False, False)
    app = DatabaseApp(root)
    root.mainloop()