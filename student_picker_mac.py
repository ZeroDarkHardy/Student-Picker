import tkinter as tk
from tkinter import ttk, messagebox
import csv
import random
import sys
import os

# Determine the base directory for bundled or standalone mode
if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
    base_dir = sys._MEIPASS  # Points to the temp directory created by PyInstaller
else:  # Running as a standalone script
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Points to the script's directory

# Path to the CSV file
file_path = os.path.join(base_dir, "Resources", "students.csv")

# Debugging the file path
if not os.path.isfile(file_path):
    print(f"Error: CSV file not found at {file_path}")

# Load student data from CSV
student_data = []
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        student_data.append({"last_name": row[0], "first_name": row[1]})

remaining_students = student_data.copy()
answered_with_messages = []  # To store student + message pairs

# Coding-themed uplifting messages list
uplifting_messages = [
    "debugged that question flawlessly!",
    "wrote a perfect algorithm!",
    "handled the logic like a pro!",
    "compiled the perfect answer!",
    "was on point with that solution!",
    "crushed that code challenge!",
    "refactored the question brilliantly!",
    "delivered a bug-free answer!",
    "optimized the solution like a genius!",
    "nailed the syntax and logic!",
    "showed true programming skills!",
    "thought like a seasoned developer!",
    "handled the edge cases like a champ!",
    "built an elegant solution!"
]

# Function to select a random student
def select_student():
    if remaining_students:
        selected = random.choice(remaining_students)
        student_name.set(f"{selected['first_name']} {selected['last_name']}")
        current_student.set(selected)
        select_button.state(["disabled"])  # Disable select button
    else:
        restart_queue()

# Function to mark the student as answered
def mark_answered():
    selected = current_student.get()
    if selected:
        for student in remaining_students:
            if student == eval(selected):
                remaining_students.remove(student)
                message = random.choice(uplifting_messages)
                answered_with_messages.append({"student": student, "message": message})
                break
        student_name.set("")
        update_answered_list()
        update_queue_counter()
        select_button.state(["!disabled"])  # Enable select button

# Function to requeue the student
def requeue():
    student_name.set("")
    select_button.state(["!disabled"])

# Function to restart the queue
def restart_queue():
    global remaining_students, answered_with_messages
    remaining_students = student_data.copy()
    answered_with_messages = []
    update_answered_list()
    update_queue_counter()
    messagebox.showinfo("Queue Restarted", "All students have answered. The queue has been restarted.")

# Function to update the answered students list
def update_answered_list():
    answered_list.delete(0, tk.END)
    for entry in answered_with_messages:
        student = entry["student"]
        message = entry["message"]
        answered_list.insert(tk.END, f"{student['first_name']} {student['last_name']} {message}")
    answered_list.yview_moveto(1)

# Function to update the queue counter
def update_queue_counter():
    queue_counter.set(f"Students Remaining: {len(remaining_students)}")

# Function to quit the app
def quit_app():
    app.destroy()

# Initialize the Tkinter app
app = tk.Tk()
app.title("Student Picker")

app_width = 700  # Slightly wider for better readability
app_height = 700
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width // 2) - (app_width // 2)
y_coordinate = (screen_height // 2) - (app_height // 2)
app.geometry(f"{app_width}x{app_height}+{x_coordinate}+{y_coordinate}")
app.configure(bg="#282c34")

student_name = tk.StringVar()
current_student = tk.StringVar(value=None)
queue_counter = tk.StringVar(value=f"Students Remaining: {len(remaining_students)}")

# Define ttk button styles
style = ttk.Style()
style.theme_use("clam")  # Use a cross-platform theme
style.configure(
    "Custom.TButton",
    font=("Helvetica", 14, "bold"),  # Increased font size
    foreground="white",
    background="#0078d4",
    padding=8
)
style.map(
    "Custom.TButton",
    background=[("active", "#005a9e"), ("disabled", "#cccccc")],
    foreground=[("disabled", "#666666")]
)

# UI Layout
frame = tk.Frame(app, bg="#282c34", padx=15, pady=15)
frame.pack(fill=tk.BOTH, expand=True)

header_label = tk.Label(frame, text="Student Picker", font=("Helvetica", 22, "bold"), fg="#61dafb", bg="#282c34")
header_label.pack(pady=15)

selected_label = tk.Label(frame, text="Selected Student:", font=("Helvetica", 16), fg="#abb2bf", bg="#282c34")
selected_label.pack()

name_label = tk.Label(frame, textvariable=student_name, font=("Helvetica", 20), fg="#98c379", bg="#282c34")
name_label.pack(pady=15)

# Buttons
select_button = ttk.Button(frame, text="Select Student", command=select_student, style="Custom.TButton")
select_button.pack(pady=10)

button_frame = tk.Frame(frame, bg="#282c34")
button_frame.pack(pady=10)

mark_button = ttk.Button(button_frame, text="Mark Answered", command=mark_answered, style="Custom.TButton")
mark_button.pack(side=tk.LEFT, padx=15)

requeue_button = ttk.Button(button_frame, text="Requeue Student", command=requeue, style="Custom.TButton")
requeue_button.pack(side=tk.LEFT, padx=15)

# Answered students display
answered_label = tk.Label(frame, text="Answered Students:", font=("Helvetica", 16), fg="#abb2bf", bg="#282c34")
answered_label.pack(pady=10)

listbox_frame = tk.Frame(frame, bg="#282c34")
listbox_frame.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
answered_list = tk.Listbox(
    listbox_frame,
    height=12,
    font=("Helvetica", 14),  # Increased font size
    fg="#e06c75",
    bg="#1e222a",
    yscrollcommand=scrollbar.set,
    relief="flat"
)
scrollbar.config(command=answered_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
answered_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

queue_counter_frame = tk.Frame(frame, bg="#282c34")
queue_counter_frame.pack(fill=tk.X, pady=10)
queue_counter_label = tk.Label(queue_counter_frame, textvariable=queue_counter, font=("Helvetica", 14), fg="#61dafb", bg="#282c34")
queue_counter_label.pack(side=tk.LEFT, padx=15)

footer_label = tk.Label(frame, text="Created by Matt Hardy", font=("Helvetica", 12), fg="#abb2bf", bg="#282c34", anchor="e")
footer_label.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=10)

# Run the app
app.mainloop()
