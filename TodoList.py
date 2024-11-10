from tkinter import *
import tkinter.messagebox

# Create the main window
window = Tk()
window.title("DataFlair Python To-Do List APP")

# Function to add a new task
def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Toplevel(window)
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()

# Function to delete selected task from the list
def deletetask():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected[0])

# Function to mark task as completed
def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        temp = marked[0]
        temp_marked = listbox_task.get(marked)
        temp_marked = temp_marked + " ✔"
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)

# Frame to hold the listbox and scrollbar
frame_task = Frame(window)
frame_task.pack()

# Listbox to display tasks
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

# Scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Button to add a task
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

# Button to delete selected task
delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

# Button to mark task as completed
mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

# Run the main window
window.mainloop()