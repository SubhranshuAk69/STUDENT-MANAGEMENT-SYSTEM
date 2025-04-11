import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import tkinter.font as tkFont

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")
        
        self.conn = sqlite3.connect("students.db")
        self.cur = self.conn.cursor()
        self.setup_db()
        
        self.setup_gui()
        
    def setup_db(self):
        """Initialize database tables"""
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Students(
                StudentID VARCHAR(10) PRIMARY KEY,
                FirstName VARCHAR(255) NOT NULL,
                LastName VARCHAR(255) NOT NULL,
                Age INT CHECK (Age BETWEEN 18 AND 22),
                Gender VARCHAR(6),
                Email VARCHAR(255) UNIQUE,
                PrimaryAddress VARCHAR(255),
                Course VARCHAR(255),
                EnrollmentDate DATE
            )
        """)
        
        self.cur.execute("SELECT COUNT(*) FROM Students")
        if self.cur.fetchone()[0] == 0:
            students_data = [
               ('A00S1', 'Ethan', 'Carter', 20, 'MALE', 'ethan.carter@example.com', '123 Maple St', 'Computer Science', '2022-08-20'),
               ('A00S2', 'Liam', 'Anderson', 19, 'MALE', 'liam.anderson@example.com', '456 Oak Ave', 'Mechanical Engineering', '2022-08-20'),
               ('A00S3', 'Noah', 'Mitchell', 21, 'MALE', 'noah.mitchell@example.com', '789 Pine Rd', 'Civil Engineering', '2022-08-21'),
               ('A00S4', 'Oliver', 'Hughes', 22, 'MALE', 'oliver.hughes@example.com', '234 Elm St', 'Electrical Engineering', '2022-08-20'),
               ('A00S5', 'William', 'Bennett', 20, 'MALE', 'william.bennett@example.com', '567 Cedar Blvd', 'Biotechnology', '2022-08-29'),
               ('A00S6', 'James', 'Harrison', 19, 'MALE', 'james.harrison@example.com', '890 Walnut Ln', 'Artificial Intelligence', '2022-08-23'),
               ('A00S7', 'Benjamin', 'Scott', 18, 'MALE', 'benjamin.scott@example.com', '123 Birch Rd', 'Data Science', '2022-08-29'),
               ('A00S8', 'Henry', 'Cooper', 21, 'MALE', 'henry.cooper@example.com', '456 Ash St', 'Business Administration', '2022-08-31'),
               ('A00S9', 'Alexander', 'Morgan', 22, 'MALE', 'alexander.morgan@example.com', '789 Willow Ave', 'Law', '2022-08-25'),
               ('A00S10', 'Daniel', 'Parker', 20, 'MALE', 'daniel.parker@example.com', '234 Cherry Ln', 'Architecture', '2022-08-26'),
               ('A00S11', 'Samuel', 'Brooks', 18, 'MALE', 'samuel.brooks@example.com', '567 Redwood St', 'Economics', '2022-08-26'),
               ('A00S12', 'Joseph', 'Gray', 19, 'MALE', 'joseph.gray@example.com', '890 Fir Rd', 'Mathematics', '2022-08-26'),
               ('A00S13', 'Lucas', 'Richardson', 21, 'MALE', 'lucas.richardson@example.com', '123 Oakwood Blvd', 'Physics', '2022-08-24'),
               ('A00S14', 'David', 'Foster', 20, 'MALE', 'david.foster@example.com', '456 Spruce Ave', 'Medical Sciences', '2022-08-22'),
               ('A00S15', 'Nathaniel', 'Adams', 22, 'MALE', 'nathaniel.adams@example.com', '789 Sycamore Rd', 'Cybersecurity', '2022-08-21'),
               ('A00S16', 'Olivia', 'Sanders', 18, 'FEMALE', 'olivia.sanders@example.com', '234 Aspen Ln', 'Nursing', '2022-08-21'),
               ('A00S17', 'Emma', 'Collins', 19, 'FEMALE', 'emma.collins@example.com', '567 Hickory St', 'Environmental Science', '2022-08-28'),
               ('A00S18', 'Ava', 'Thompson', 21, 'FEMALE', 'ava.thompson@example.com', '890 Poplar Ave', 'Astronomy', '2022-08-28'),
               ('A00S19', 'Sophia', 'Bennett', 22, 'FEMALE', 'sophia.bennett@example.com', '123 Magnolia St', 'Political Science', '2022-08-27'),
               ('A00S20', 'Isabella', 'Wright', 20, 'FEMALE', 'isabella.wright@example.com', '456 Dogwood Ln', 'Fashion Design', '2022-08-21'),
               ('A00S21', 'Mia', 'Roberts', 19, 'FEMALE', 'mia.roberts@example.com', '789 Cottonwood Rd', 'Psychology', '2022-08-20'),
               ('A00S22', 'Amelia', 'Carter', 22, 'FEMALE', 'amelia.carter@example.com', '234 Palm St', 'Journalism', '2022-08-20'),
               ('A00S23', 'Charlotte', 'Evans', 18, 'FEMALE', 'charlotte.evans@example.com', '567 Pinecone Ave', 'Sociology', '2022-08-29'),
               ('A00S24', 'Harper', 'Lewis', 19, 'FEMALE', 'harper.lewis@example.com', '890 Hazel Rd', 'Philosophy', '2022-08-31'),
               ('A00S25', 'Evelyn', 'Turner', 21, 'FEMALE', 'evelyn.turner@example.com', '123 Elmwood Blvd', 'Fine Arts', '2022-08-31'),
               ('A00S26', 'Abigail', 'Clark', 20, 'FEMALE', 'abigail.clark@example.com', '456 Mulberry St', 'History', '2022-08-30'),
               ('A00S27', 'Ella', 'Richardson', 18, 'FEMALE', 'ella.richardson@example.com', '789 Mahogany Ave', 'Statistics', '2022-08-24'),
               ('A00S28', 'Scarlett', 'King', 19, 'FEMALE', 'scarlett.king@example.com', '234 Beech Ln', 'International Relations', '2022-08-25'),
               ('A00S29', 'Grace', 'Miller', 21, 'FEMALE', 'grace.miller@example.com', '567 Alder Rd', 'Genetics', '2022-08-30'),
               ('A00S30', 'Zoey', 'Phillips', 22, 'FEMALE', 'zoey.phillips@example.com', '890 Bamboo St', 'Marine Biology', '2022-08-31'),
               ('A00S31', 'Ryan', 'Smith', 20, 'MALE', 'ryan.smith@example.com', '101 Birch St', 'Computer Science', '2022-08-21'),
               ('A00S32', 'Jack', 'Johnson', 19, 'MALE', 'jack.johnson@example.com', '202 Pine Rd', 'Mechanical Engineering', '2022-08-22'),
               ('A00S33', 'Ethan', 'Williams', 21, 'MALE', 'ethan.williams@example.com', '303 Cedar Ave', 'Civil Engineering', '2022-08-23'),
               ('A00S34', 'Mason', 'Brown', 22, 'MALE', 'mason.brown@example.com', '404 Elm St', 'Electrical Engineering', '2022-08-24'),
               ('A00S35', 'Logan', 'Davis', 20, 'MALE', 'logan.davis@example.com', '505 Oak Blvd', 'Biotechnology', '2022-08-25'),
               ('A00S36', 'Jacob', 'Moore', 19, 'MALE', 'jacob.moore@example.com', '606 Walnut Ln', 'Artificial Intelligence', '2022-08-26'),
               ('A00S37', 'Carter', 'Taylor', 18, 'MALE', 'carter.taylor@example.com', '707 Birch Rd', 'Data Science', '2022-08-27'),
               ('A00S38', 'Luke', 'Anderson', 21, 'MALE', 'luke.anderson@example.com', '808 Ash St', 'Business Administration', '2022-08-28'),
               ('A00S39', 'Isaac', 'White', 22, 'MALE', 'isaac.white@example.com', '909 Willow Ave', 'Law', '2022-08-29'),
               ('A00S40', 'Sebastian', 'Clark', 20, 'MALE', 'sebastian.clark@example.com', '110 Cherry Ln', 'Architecture', '2022-08-30'),
               ('A00S41', 'Madison', 'Harris', 18, 'FEMALE', 'madison.harris@example.com', '121 Redwood St', 'Economics', '2022-09-01'),
               ('A00S42', 'Scarlett', 'Martin', 19, 'FEMALE', 'scarlett.martin@example.com', '232 Fir Rd', 'Mathematics', '2022-09-02'),
               ('A00S43', 'Victoria', 'Thompson', 21, 'FEMALE', 'victoria.thompson@example.com', '343 Oakwood Blvd', 'Physics', '2022-09-03'),
               ('A00S44', 'Grace', 'Walker', 20, 'FEMALE', 'grace.walker@example.com', '454 Spruce Ave', 'Medical Sciences', '2022-09-04'),
               ('A00S45', 'Lily', 'Hall', 22, 'FEMALE', 'lily.hall@example.com', '565 Sycamore Rd', 'Cybersecurity', '2022-09-05')

            ]
            self.cur.executemany("""
                INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, students_data)
            self.conn.commit()
    
    def setup_gui(self):
        """Set up the GUI components"""
        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabelFrame', background='#f0f0f0', foreground='#333333', font=('Segoe UI', 10))
        self.style.configure('TButton', font=('Segoe UI', 9), padding=5)
        self.style.map('TButton',
            foreground=[('active', 'black'), ('!active', 'black')],
            background=[('active', '#d9d9d9'), ('!active', '#e6e6e6')]
        )
        
        # Custom font
        self.custom_font = tkFont.Font(family='Segoe UI', size=9)
        
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.pack(fill=BOTH, expand=True)
        
        # Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="Student Information", padding="10 5 10 10")
        input_frame.pack(fill=X, pady=(0, 10))
        
        # Form Fields
        fields = [
            ("Student ID", "student_id_var"),
            ("First Name", "first_name_var"),
            ("Last Name", "last_name_var"),
            ("Age", "age_var"),
            ("Gender", "gender_var"),
            ("Email", "email_var"),
            ("Address", "address_var"),
            ("Course", "course_var"),
            ("Enrollment Date", "enrollment_date_var")
        ]
        
        self.vars = {}
        for i, (label_text, var_name) in enumerate(fields):
            setattr(self, var_name, StringVar())
            self.vars[var_name] = getattr(self, var_name)
            
            ttk.Label(input_frame, text=label_text, font=self.custom_font).grid(
                row=i//3, column=(i%3)*2, sticky=W, padx=5, pady=2)
            ttk.Entry(input_frame, textvariable=getattr(self, var_name), width=22, font=self.custom_font).grid(
                row=i//3, column=(i%3)*2+1, sticky=W, padx=5, pady=2)
        
        # Button Frame
        button_frame = ttk.Frame(main_frame, padding="0 5 0 5")
        button_frame.pack(fill=X, pady=(0, 10))
        
        ttk.Button(button_frame, text="Add", command=self.add_student).pack(side=LEFT, padx=3)
        ttk.Button(button_frame, text="Update", command=self.update_student).pack(side=LEFT, padx=3)
        ttk.Button(button_frame, text="Delete", command=self.delete_student).pack(side=LEFT, padx=3)
        ttk.Button(button_frame, text="Search", command=self.search_students).pack(side=LEFT, padx=3)
        ttk.Button(button_frame, text="Clear", command=self.clear_fields).pack(side=LEFT, padx=3)
        
        # Treeview Frame
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=BOTH, expand=True)
        
        # Treeview with Scrollbars
        self.tree = ttk.Treeview(
            tree_frame, 
            columns=("ID", "First Name", "Last Name", "Age", "Gender", "Email", "Course"), 
            show="headings",
            style="Custom.Treeview"
        )
        
        # Configure treeview style
        self.style.configure("Custom.Treeview", 
            font=self.custom_font,
            rowheight=25,
            background="#ffffff",
            fieldbackground="#ffffff",
            foreground="#333333"
        )
        self.style.configure("Custom.Treeview.Heading", 
            font=('Segoe UI', 9, 'bold'),
            background="#e6e6e6",
            relief=FLAT
        )
        self.style.map("Custom.Treeview",
            background=[('selected', '#0078d7')],
            foreground=[('selected', 'white')]
        )
        
        # Define headings
        self.tree.heading("ID", text="Student ID")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Course", text="Course")
        
        # Set column widths
        self.tree.column("ID", width=80)
        self.tree.column("First Name", width=100)
        self.tree.column("Last Name", width=100)
        self.tree.column("Age", width=50)
        self.tree.column("Gender", width=80)
        self.tree.column("Email", width=150)
        self.tree.column("Course", width=150)
        
        # Add scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=self.tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        # Grid layout
        self.tree.grid(row=0, column=0, sticky=NSEW)
        y_scroll.grid(row=0, column=1, sticky=NS)
        x_scroll.grid(row=1, column=0, sticky=EW)
        
        # Configure grid weights
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Bind treeview selection
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
        # Load initial data
        self.load_students()
    
    def load_students(self):
        """Load all students into the treeview"""
        self.tree.delete(*self.tree.get_children())
        try:
            self.cur.execute("SELECT StudentID, FirstName, LastName, Age, Gender, Email, Course FROM Students")
            rows = self.cur.fetchall()
            for row in rows:
                self.tree.insert("", END, values=row)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error loading students: {e}")
    
    def add_student(self):
        """Add a new student to the database"""
        try:
            # Validate inputs
            if not all([self.student_id_var.get(), self.first_name_var.get(), self.last_name_var.get()]):
                messagebox.showwarning("Validation Error", "Student ID, First Name and Last Name are required")
                return
            
            # Insert new student
            self.cur.execute("""
                INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.student_id_var.get(),
                self.first_name_var.get(),
                self.last_name_var.get(),
                int(self.age_var.get()) if self.age_var.get() else None,
                self.gender_var.get(),
                self.email_var.get(),
                self.address_var.get(),
                self.course_var.get(),
                self.enrollment_date_var.get() or datetime.now().strftime("%Y-%m-%d")
            ))
            self.conn.commit()
            messagebox.showinfo("Success", "Student added successfully")
            self.load_students()
            self.clear_fields()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("Database Error", f"Error adding student: {e}")
        except ValueError:
            messagebox.showerror("Validation Error", "Age must be a number")
    
    def update_student(self):
        """Update selected student"""
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a student to update")
            return
        
        try:
            student_id = self.tree.item(selected)['values'][0]
            self.cur.execute("""
                UPDATE Students SET
                    FirstName = ?,
                    LastName = ?,
                    Age = ?,
                    Gender = ?,
                    Email = ?,
                    PrimaryAddress = ?,
                    Course = ?,
                    EnrollmentDate = ?
                WHERE StudentID = ?
            """, (
                self.first_name_var.get(),
                self.last_name_var.get(),
                int(self.age_var.get()) if self.age_var.get() else None,
                self.gender_var.get(),
                self.email_var.get(),
                self.address_var.get(),
                self.course_var.get(),
                self.enrollment_date_var.get(),
                student_id
            ))
            self.conn.commit()
            messagebox.showinfo("Success", "Student updated successfully")
            self.load_students()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating student: {e}")
        except ValueError:
            messagebox.showerror("Validation Error", "Age must be a number")
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a student to delete")
            return
        
        student_id = self.tree.item(selected)['values'][0]
        if messagebox.askyesno("Confirm", f"Delete student {student_id}?"):
            try:
                self.cur.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Student deleted successfully")
                self.load_students()
                self.clear_fields()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error deleting student: {e}")
    
    def search_students(self):
        """Search students by name or ID"""
        search_term = f"%{self.student_id_var.get()}%"
        self.tree.delete(*self.tree.get_children())
        try:
            self.cur.execute("""
                SELECT StudentID, FirstName, LastName, Age, Gender, Email, Course 
                FROM Students 
                WHERE StudentID LIKE ? OR FirstName LIKE ? OR LastName LIKE ?
            """, (search_term, search_term, search_term))
            rows = self.cur.fetchall()
            for row in rows:
                self.tree.insert("", END, values=row)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error searching students: {e}")
    
    def on_tree_select(self, event):
        """Load selected student into form fields"""
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected)['values']
            self.student_id_var.set(values[0])
            self.first_name_var.set(values[1])
            self.last_name_var.set(values[2])
            self.age_var.set(values[3])
            self.gender_var.set(values[4])
            self.email_var.set(values[5])
            self.course_var.set(values[6])
    
    def clear_fields(self):
        """Clear all form fields"""
        for var in self.vars.values():
            var.set("")
    
    def __del__(self):
        """Clean up database connection"""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
