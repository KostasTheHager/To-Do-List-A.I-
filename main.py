import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List with Reminders")
        self.tasks = []

        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.priority_var = tk.StringVar(value="Low")
        self.priority_dropdown = tk.OptionMenu(master, self.priority_var, "Low", "Medium", "High")
        self.priority_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.filter_label = tk.Label(master, text="Filter By:")
        self.filter_label.grid(row=0, column=3, padx=5, pady=5)

        self.filter_options = tk.StringVar(value="All")
        self.filter_dropdown = tk.OptionMenu(master, self.filter_options, "All", "Completed", "Incomplete", command=self.filter_tasks)
        self.filter_dropdown.grid(row=0, column=4, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=2, padx=5, pady=5)

        self.reminder_button = tk.Button(master, text="Set Reminder", command=self.set_reminder)
        self.reminder_button.grid(row=2, column=3, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        if task:
            self.tasks.append((len(self.tasks) + 1, task, False, priority))
            self.task_listbox.insert(tk.END, f"{task} ({priority})")  # Display task with priority
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_id = self.tasks[selected_index][0]
            old_task = self.tasks[selected_index][1]
            old_priority = self.tasks[selected_index][3]
            new_task = simpledialog.askstring("Edit Task", "Enter new task:")
            new_priority = simpledialog.askstring("Edit Priority", "Enter new priority (Low, Medium, High):")
            if new_task:
                self.tasks[selected_index] = (task_id, new_task, self.tasks[selected_index][2], new_priority)
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"{new_task} ({new_priority})")  # Display edited task with priority
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_as_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_id = self.tasks[selected_index][0]
            self.tasks[selected_index] = (task_id, self.tasks[selected_index][1], True, self.tasks[selected_index][3])
            self.task_listbox.itemconfig(selected_index, {'bg': 'light green'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def set_reminder(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index][1]
            messagebox.showinfo("Reminder Set", f"Reminder for task '{task}' set successfully!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to set a reminder.")

    def filter_tasks(self, *args):
        selected_filter = self.filter_options.get()
        self.task_listbox.delete(0, tk.END)
        if selected_filter == "Completed":
            filtered_tasks = [f"{task[1]} ({task[3]})" for task in self.tasks if task[2]]
        elif selected_filter == "Incomplete":
            filtered_tasks = [f"{task[1]} ({task[3]})" for task in self.tasks if not task[2]]
        else:
            filtered_tasks = [f"{task[1]} ({task[3]})" for task in self.tasks]
        for task in filtered_tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()