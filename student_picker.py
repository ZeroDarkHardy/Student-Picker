import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# Load student data from CSV
file_path = "students.csv"
student_data = pd.read_csv(file_path, header=None, names=["last_name", "first_name"])
remaining_students = student_data.copy()
answered_students = []  # List to keep track of answered students

# Function to select a random student
def select_student():
    if not remaining_students.empty:
        selected = remaining_students.sample().iloc[0]
        student_name.set(f"{selected['first_name']} {selected['last_name']}")
        current_student.set(selected.name)  # Store the index for tracking
        select_button.config(state=tk.DISABLED)  # Disable select button
    else:
        # Restart the queue when all students have answered
        restart_queue()

# Function to mark the student as answered
def mark_answered():
    index = current_student.get()
    if index is not None and not pd.isna(index):
        global remaining_students
        selected = remaining_students.loc[index]
        answered_students.append(f"{selected['first_name']} {selected['last_name']}")
        remaining_students = remaining_students.drop(index)
        student_name.set("")
        update_answered_list()  # Update the display of answered students
        update_queue_counter()  # Update the queue counter
        select_button.config(state=tk.NORMAL)  # Enable select button

# Function to put the student back in the queue
def requeue():
    student_name.set("")
    select_button.config(state=tk.NORMAL)  # Enable select button

# Function to restart the queue
def restart_queue():
    global remaining_students, answered_students
    remaining_students = student_data.copy()
    answered_students = []
    update_answered_list()
    update_queue_counter()  # Update the queue counter
    messagebox.showinfo("Queue Restarted", "All students have answered. The queue has been restarted.")

# Function to update the answered students list
def update_answered_list():
    answered_list.delete(0, tk.END)  # Clear the listbox
    for student in answered_students:
        answered_list.insert(tk.END, student)

# Function to update the queue counter
def update_queue_counter():
    queue_counter.set(f"Students Remaining: {len(remaining_students)}")

# Function to quit the app
def quit_app():
    app.destroy()

# Initialize the Tkinter app
app = tk.Tk()
app.title("Student Picker")
app.geometry("600x600")  # Default window size set taller
app.configure(bg="#282c34")
app.overrideredirect(True)  # Remove the title bar

# Tkinter Variables
student_name = tk.StringVar()
current_student = tk.IntVar(value=None)
queue_counter = tk.StringVar(value=f"Students Remaining: {len(remaining_students)}")

# Custom title bar
title_bar = tk.Frame(app, bg="#1e222a", relief="raised", bd=0)
title_bar.pack(fill=tk.X)

title_label = tk.Label(title_bar, text="Student Picker", font=("Helvetica", 12, "bold"), bg="#1e222a", fg="#61dafb")
title_label.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(title_bar, text="x", font=("Helvetica", 12, "bold"), bg="#dc3545", fg="white", command=quit_app, relief="flat", bd=0, activebackground="#c82333", activeforeground="white")
close_button.pack(side=tk.RIGHT, padx=5)

# Dragging functionality
def start_drag(event):
    app.x = event.x
    app.y = event.y

def drag_window(event):
    x = app.winfo_pointerx() - app.x
    y = app.winfo_pointery() - app.y
    app.geometry(f"600x600+{x}+{y}")

title_bar.bind("<Button-1>", start_drag)
title_bar.bind("<B1-Motion>", drag_window)

# UI Elements
frame = tk.Frame(app, bg="#282c34", padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

header_label = tk.Label(frame, text="Student Picker", font=("Helvetica", 18, "bold"), fg="#61dafb", bg="#282c34")
header_label.pack(pady=10)

selected_label = tk.Label(frame, text="Selected Student:", font=("Helvetica", 14), fg="#abb2bf", bg="#282c34")
selected_label.pack()

name_label = tk.Label(frame, textvariable=student_name, font=("Helvetica", 16), fg="#98c379", bg="#282c34")
name_label.pack(pady=10)

# Fancy button style
fancy_button_style = {
    "font": ("Helvetica", 12, "bold"),
    "relief": "groove",
    "bd": 3
}

# Select button
select_button = tk.Button(frame, text="Select Student", command=select_student, bg="#61dafb", fg="#282c34", activebackground="#98c379", activeforeground="#1e222a", **fancy_button_style)
select_button.pack(pady=5)

# Answered and Requeue buttons in a horizontal frame
button_frame = tk.Frame(frame, bg="#282c34")
button_frame.pack(pady=5)

mark_button = tk.Button(button_frame, text="Mark Answered", command=mark_answered, bg="#28a745", fg="white", activebackground="#218838", activeforeground="white", **fancy_button_style)
mark_button.pack(side=tk.LEFT, padx=10)

requeue_button = tk.Button(button_frame, text="Requeue Student", command=requeue, bg="#dc3545", fg="white", activebackground="#c82333", activeforeground="white", **fancy_button_style)
requeue_button.pack(side=tk.LEFT, padx=10)

answered_label = tk.Label(frame, text="Answered Students:", font=("Helvetica", 14), fg="#abb2bf", bg="#282c34")
answered_label.pack(pady=10)

# Scrollable listbox for answered students
listbox_frame = tk.Frame(frame, bg="#282c34")
listbox_frame.pack(fill=tk.BOTH, expand=True, pady=5)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, bg="#282c34")
answered_list = tk.Listbox(listbox_frame, height=10, font=("Helvetica", 12), fg="#e06c75", bg="#1e222a", yscrollcommand=scrollbar.set, relief="flat")
scrollbar.config(command=answered_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
answered_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Queue counter display
queue_counter_frame = tk.Frame(frame, bg="#282c34")
queue_counter_frame.pack(fill=tk.X, pady=10)
queue_counter_label = tk.Label(queue_counter_frame, textvariable=queue_counter, font=("Helvetica", 12), fg="#61dafb", bg="#282c34")
queue_counter_label.pack(side=tk.LEFT, padx=10)

# Footer with creator credit
footer_label = tk.Label(frame, text="Created by Matt Hardy", font=("Helvetica", 8), fg="#abb2bf", bg="#282c34", anchor="e")
footer_label.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)

# Run the app
app.mainloop()
