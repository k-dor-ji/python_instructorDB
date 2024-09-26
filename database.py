import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

class UniIndex:
    def __init__(self):
        # Initialize the main window
        self.main_window = tk.Tk()
        self.main_window.title("University Information System")
        self.main_window.geometry('1920x1080')
        self.main_window.configure(bg='#f0f0f0')

        # Create the database and tables
        self.create_database()

        # Radio button setup
        self.radio_frame = tk.Frame(self.main_window, bg='#f0f0f0')
        self.radio_var = tk.IntVar(value=0)

        options = [
            ("Get Instructor Info", 1, self.show_instructor_info),
            ("Get Department Info", 2, self.show_department_info),
            ("Add Instructor Info", 3, self.show_add_instructor),
            ("Add Department Info", 4, self.show_add_department),
            ("Clear", 5, self.clear_info),
            ("Quit", 6, self.quit_function)
        ]

        for text, value, command in options:
            rb = tk.Radiobutton(self.radio_frame, text=text, variable=self.radio_var, value=value, command=command, bg='#f0f0f0')
            rb.pack(side='left', padx=5)

        self.radio_frame.pack(pady=10)

        self.option_frame = tk.Frame(self.main_window, bg='#f0f0f0')
        self.results_frame = tk.Frame(self.main_window, bg='#f0f0f0')

        self.main_window.mainloop()

    def create_database(self):
        self.conn = sqlite3.connect('university.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS instructor (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS department (
                name TEXT PRIMARY KEY,
                building TEXT NOT NULL,
                budget INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def show_instructor_info(self):
        self.clear_info()
        self.create_instructor_info_widgets()
        self.option_frame.pack()

    def show_department_info(self):
        self.clear_info()
        self.create_department_info_widgets()
        self.option_frame.pack()

    def show_add_instructor(self):
        self.clear_info()
        self.create_add_instructor_widgets()
        self.option_frame.pack()

    def show_add_department(self):
        self.clear_info()
        self.create_add_department_widgets()
        self.option_frame.pack()

    def create_instructor_info_widgets(self):
        self.instructor_id_label = tk.Label(self.option_frame, text='Enter Instructor ID:', bg='#f0f0f0')
        self.instructor_id_entry = tk.Entry(self.option_frame)
        self.instructor_id_entry.bind('<Return>', self.get_instructor_info)
        self.instructor_id_label.pack(pady=5)
        self.instructor_id_entry.pack(pady=5)

        self.submit_btn = tk.Button(self.option_frame, text='Submit', command=self.get_instructor_info, bg='#4CAF50', fg='white')
        self.submit_btn.pack(pady=5)

    def create_department_info_widgets(self):
        self.department_name_label = tk.Label(self.option_frame, text='Enter Department Name:', bg='#f0f0f0')
        self.department_name_entry = tk.Entry(self.option_frame)
        self.department_name_entry.bind('<Return>', self.get_department_info)
        self.department_name_label.pack(pady=5)
        self.department_name_entry.pack(pady=5)

        self.submit_btn = tk.Button(self.option_frame, text='Submit', command=self.get_department_info, bg='#4CAF50', fg='white')
        self.submit_btn.pack(pady=5)

    def create_add_instructor_widgets(self):
        self.new_id_label = tk.Label(self.option_frame, text='Enter Instructor ID:', bg='#f0f0f0')
        self.new_name_label = tk.Label(self.option_frame, text='Enter Instructor Name:', bg='#f0f0f0')
        self.new_dept_label = tk.Label(self.option_frame, text='Enter Department:', bg='#f0f0f0')

        self.new_id_entry = tk.Entry(self.option_frame)
        self.new_name_entry = tk.Entry(self.option_frame)
        self.new_dept_entry = tk.Entry(self.option_frame)

        self.new_id_label.pack(pady=5)
        self.new_id_entry.pack(pady=5)
        self.new_name_label.pack(pady=5)
        self.new_name_entry.pack(pady=5)
        self.new_dept_label.pack(pady=5)
        self.new_dept_entry.pack(pady=5)

        self.add_instructor_btn = tk.Button(self.option_frame, text='Add Instructor', command=self.add_instructor_info, bg='#4CAF50', fg='white')
        self.add_instructor_btn.pack(pady=5)

    def create_add_department_widgets(self):
        self.new_dept_name_label = tk.Label(self.option_frame, text='Enter Department Name:', bg='#f0f0f0')
        self.new_building_label = tk.Label(self.option_frame, text='Enter Building:', bg='#f0f0f0')
        self.new_budget_label = tk.Label(self.option_frame, text='Enter Budget:', bg='#f0f0f0')

        self.new_dept_name_entry = tk.Entry(self.option_frame)
        self.new_building_entry = tk.Entry(self.option_frame)
        self.new_budget_entry = tk.Entry(self.option_frame)

        self.new_dept_name_label.pack(pady=5)
        self.new_dept_name_entry.pack(pady=5)
        self.new_building_label.pack(pady=5)
        self.new_building_entry.pack(pady=5)
        self.new_budget_label.pack(pady=5)
        self.new_budget_entry.pack(pady=5)

        self.add_department_btn = tk.Button(self.option_frame, text='Add Department', command=self.add_department_info, bg='#4CAF50', fg='white')
        self.add_department_btn.pack(pady=5)

    def clear_info(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.option_frame.pack_forget()

        for widget in self.option_frame.winfo_children():
            widget.pack_forget()

        self.results_frame.pack_forget()

    def get_instructor_info(self, event=None):
        instructor_id = self.instructor_id_entry.get()
        found = False
        try:
            self.cursor.execute("SELECT name, department FROM instructor WHERE id = ?", (instructor_id,))
            result = self.cursor.fetchone()
            if result:
                self.display_instructor_info(result[0], result[1])
                found = True
            if not found:
                messagebox.showerror("Error", "No instructor found with that ID.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_instructor_info(self, name, dept):
        self.clear_info()
        tk.Label(self.results_frame, text=f'Name: {name}', bg='#f0f0f0').pack()
        tk.Label(self.results_frame, text=f'Department: {dept}', bg='#f0f0f0').pack()
        self.results_frame.pack(pady=10)

    def get_department_info(self, event=None):
        department_name = self.department_name_entry.get()
        found = False
        try:
            self.cursor.execute("SELECT building, budget FROM department WHERE name = ?", (department_name,))
            result = self.cursor.fetchone()
            if result:
                self.display_department_info(result[0], result[1])
                found = True
            if not found:
                messagebox.showerror("Error", "No department found with that name.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_department_info(self, building, budget):
        self.clear_info()
        tk.Label(self.results_frame, text=f'Building: {building}', bg='#f0f0f0').pack()
        tk.Label(self.results_frame, text=f'Budget: {budget}', bg='#f0f0f0').pack()
        self.results_frame.pack(pady=10)

    def add_instructor_info(self):
        instructor_id = self.new_id_entry.get().strip()
        instructor_name = self.new_name_entry.get().strip()
        department = self.new_dept_entry.get().strip()

        # Validation checks
        if not instructor_id.isdigit() or len(instructor_id) != 4:
            messagebox.showwarning("Input Error", "Instructor ID must be exactly 4 digits.")
            return

        # Check if the name contains only letters and spaces
        if not re.match("^[A-Za-z\s]+$", instructor_name):
            messagebox.showwarning("Input Error", "Instructor name must contain only letters and spaces.")
            return

        if not department.isalpha():
            messagebox.showwarning("Input Error", "Department must contain only letters.")
            return

        try:
            self.cursor.execute("SELECT * FROM instructor WHERE id = ?", (instructor_id,))
            if self.cursor.fetchone():
                messagebox.showwarning("Input Error", "Instructor ID already exists.")
                return

            self.cursor.execute("INSERT INTO instructor (id, name, department) VALUES (?, ?, ?)",
                                (instructor_id, instructor_name, department))
            self.conn.commit()
            messagebox.showinfo("Success", "Instructor added successfully.")
            self.clear_info()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_department_info(self):
        dept_name = self.new_dept_name_entry.get().strip()
        building = self.new_building_entry.get().strip()
        budget = self.new_budget_entry.get().strip()

        # Validation checks
        if not dept_name.isalpha():
            messagebox.showwarning("Input Error", "Department name must contain only letters.")
            return
        if not budget.isdigit():
            messagebox.showwarning("Input Error", "Budget must contain only numbers.")
            return

        try:
            self.cursor.execute("SELECT * FROM department WHERE name = ?", (dept_name,))
            if self.cursor.fetchone():
                messagebox.showwarning("Input Error", "Department name already exists.")
                return

            self.cursor.execute("INSERT INTO department (name, building, budget) VALUES (?, ?, ?)",
                                (dept_name, building, int(budget)))
            self.conn.commit()
            messagebox.showinfo("Success", "Department added successfully.")
            self.clear_info()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def quit_function(self):
        self.conn.close()  # Close the database connection
        self.main_window.destroy()

def main():
    UniIndex()

if __name__ == '__main__':
    main()
