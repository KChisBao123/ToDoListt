import tkinter
from tkinter import *

# Tạo cửa sổ chính
window = Tk()
window.title("TO_DO_LIST")
window.geometry("400x650+400+100")
window.resizable(False, False)

task_list = []


def addTask():
    """Thêm task mới vào danh sách và file."""
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    """Xóa task được chọn khỏi danh sách và file."""
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)


def openTaskfile():
    """Mở file tasklist.txt và tải danh sách task."""
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        # Tạo file nếu chưa tồn tại
        with open("tasklist.txt", "w") as taskfile:
            pass


# Icon
Image_icon = PhotoImage(file="image/task.png")
window.iconphoto(False, Image_icon)

# Top bar
TopImage = PhotoImage(file="image/topbar.png")
Label(window, image=TopImage).pack()

dockImage = PhotoImage(file="image/dock.png")
Label(window, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="image/task.png")
Label(window, image=noteImage, bg="#32405b").place(x=30, y=25)

heading = Label(window, text="All Task", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Main frame
frame = Frame(window, width=400, height=50, bg="white")
frame.place(x=0, y=70)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0, textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# Listbox
framel = Frame(window, bd=3, width=400, height=400, bg="#32405b")
framel.pack(pady=(160, 0))

listbox = Listbox(
    framel,
    font=('arial', 12),
    width=40,
    height=16,
    bg="#32405b",
    fg="white",
    cursor="hand2",
    selectbackground="#5a95ff"
)
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(framel)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Mở file và tải danh sách task
openTaskfile()

# Delete button
Delete_icon = PhotoImage(file="image/delete.png")
Button(window, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

window.mainloop()
