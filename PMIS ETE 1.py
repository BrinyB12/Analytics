from tkinter import *
from tkinter import ttk,messagebox
import pymysql

def add_employee():
    emp_id = txt_id.get()
    emp_name = txt_name.get()
    emp_designation = txt_designation.get()
    emp_salary = txt_salary.get()

    # Establish a connection to the database
    connection = pymysql.connect(host='localhost', user='root', password='brinybosco', database='ems')

    # Create a cursor object
    cursor = connection.cursor()

    # Prepare the SQL query
    sql = "INSERT INTO employees (emp_id, emp_name, emp_designation, emp_salary) VALUES (%s, %s, %s, %s)"
    values = (emp_id, emp_name, emp_designation, emp_salary)

    try:
        # Execute the query
        cursor.execute(sql, values)

        # Commit the changes to the database
        connection.commit()

        messagebox.showinfo("Success", "Employee added successfully")

        # Clear the input fields
        txt_id.delete(0, tk.END)
        txt_name.delete(0, tk.END)
        txt_designation.delete(0, tk.END)
        txt_salary.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Error in adding employee: {str(e)}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


def fetch_employees():
    # Establish a connection to the database
    connection = pymysql.connect(host='localhost', user='root', password='brinybosco', database='ems')

    # Create a cursor object
    cursor = connection.cursor()

    # Prepare the SQL query
    sql = "SELECT * FROM employees"

    try:
        # Execute the query
        cursor.execute(sql)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Clear the existing data in the listbox
        listbox.delete(0, tk.END)

        # Process the rows
        for row in rows:
            emp_id = row[0]
            emp_name = row[1]
            emp_designation = row[2]
            emp_salary = row[3]
            listbox.insert(tk.END, f"ID: {emp_id}, Name: {emp_name}, Designation: {emp_designation}, Salary: {emp_salary}")

    except Exception as e:
        messagebox.showerror("Error", f"Error in fetching employees: {str(e)}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Employee Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # ======================== VARIABLES =======================
        self.emp_id = StringVar()
        self.emp_name = StringVar()
        self.emp_designation = StringVar()
        self.emp_salary = StringVar()
        self.emp_phone = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ======================== MANAGE FRAME =======================
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        manage_frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(manage_frame, text="Manage Employees", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_id = Label(manage_frame, text="Employee ID", bg="crimson", fg="white",
                       font=("times new roman", 20, "bold"))
        lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_id = Entry(manage_frame, textvariable=self.emp_id, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frame, text="Name", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(manage_frame, textvariable=self.emp_name, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_designation = Label(manage_frame, text="Designation", bg="crimson", fg="white",
                                font=("times new roman", 20, "bold"))
        lbl_designation.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_designation = Entry(manage_frame, textvariable=self.emp_designation, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_designation.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_salary = Label(manage_frame, text="Salary", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_salary.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_salary = Entry(manage_frame, textvariable=self.emp_salary, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_salary.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        lbl_phone = Label(manage_frame, text="Phone", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_phone.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_phone = Entry(manage_frame, textvariable=self.emp_phone, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_phone.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # ======================== BUTTON FRAME =======================
        button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
        button_frame.place(x=10, y=500, width=430)

        add_btn = Button(button_frame, text="Add", width=10, command=self.add_employee).grid(row=0, column=0, padx=10, pady=10)
        update_btn = Button(button_frame, text="Update", width=10, command=self.update_employee).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(button_frame, text="Delete", width=10, command=self.delete_employee).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(button_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # ======================== DETAIL FRAME =======================
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=820, height=580)

        lbl_search = Label(detail_frame, text="Search By", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by,
                                    font=("times new roman", 13), state='readonly', width=10)
        combo_search['values'] = ("emp_id", "emp_name", "emp_designation", "emp_salary")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(detail_frame, textvariable=self.search_txt, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(detail_frame, text="Search", width=10, command=self.search_employee).grid(row=0, column=3, padx=10, pady=10)
        show_all_btn = Button(detail_frame, text="Show All", width=10, command=self.fetch_employees).grid(row=0, column=4, padx=10, pady=10)

        # ======================== TABLE FRAME =======================
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=800, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(table_frame, columns=("emp_id", "emp_name", "emp_designation", "emp_salary", "emp_phone"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("emp_id", text="Employee ID")
        self.employee_table.heading("emp_name", text="Name")
        self.employee_table.heading("emp_designation", text="Designation")
        self.employee_table.heading("emp_salary", text="Salary")
        self.employee_table.heading("emp_phone", text="Phone")

        self.employee_table['show'] = 'headings'

        self.employee_table.column("emp_id", width=100)
        self.employee_table.column("emp_name", width=200)
        self.employee_table.column("emp_designation", width=200)
        self.employee_table.column("emp_salary", width=100)
        self.employee_table.column("emp_phone", width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_employee)

        self.fetch_employees()

    def add_employee(self):
        emp_id = self.emp_id.get()
        emp_name = self.emp_name.get()
        emp_designation = self.emp_designation.get()
        emp_salary = self.emp_salary.get()
        emp_phone = self.emp_phone.get()

        if emp_id == "" or emp_name == "" or emp_designation == "" or emp_salary == "" or emp_phone == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="brinybosco", database="ems")
                cur = conn.cursor()
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
                            (emp_id, emp_name, emp_designation, emp_salary, emp_phone))
                conn.commit()
                self.fetch_employees()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Employee added successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error in adding employee: {str(e)}")

    def update_employee(self):
        emp_id = self.emp_id.get()
        emp_name = self.emp_name.get()
        emp_designation = self.emp_designation.get()
        emp_salary = self.emp_salary.get()
        emp_phone = self.emp_phone.get()

        if emp_id == "" or emp_name == "" or emp_designation == "" or emp_salary == "" or emp_phone == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="brinybosco", database="ems")
                cur = conn.cursor()
                cur.execute("UPDATE employees SET emp_name=%s, emp_designation=%s, emp_salary=%s, emp_phone=%s WHERE emp_id=%s",
                            (emp_name, emp_designation, emp_salary, emp_phone, emp_id))
                conn.commit()
                self.fetch_employees()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Employee updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error in updating employee: {str(e)}")

    def delete_employee(self):
        emp_id = self.emp_id.get()

        if emp_id == "":
            messagebox.showerror("Error", "Employee ID is required!")
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="brinybosco", database="ems")
                cur = conn.cursor()
                cur.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
                conn.commit()
                self.fetch_
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Employee deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error in deleting employee: {str(e)}")

    def clear(self):
        self.emp_id.set("")
        self.emp_name.set("")
        self.emp_designation.set("")
        self.emp_salary.set("")
        self.emp_phone.set("")

    def get_employee(self, event):
        row = self.employee_table.focus()
        contents = self.employee_table.item(row)
        row_data = contents['values']
        self.emp_id.set(row_data[0])
        self.emp_name.set(row_data[1])
        self.emp_designation.set(row_data[2])
        self.emp_salary.set(row_data[3])
        self.emp_phone.set(row_data[4])

    def fetch_employees(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", password="brinybosco", database="ems")
            cur = conn.cursor()
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            if len(rows) > 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert('', END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error in fetching employees: {str(e)}")

    def search_employee(self):
        search_by = self.search_by.get()
        search_txt = self.search_txt.get()
        try:
            conn = pymysql.connect(host="localhost", user="root", password="brinybosco", database="ems")
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM employees WHERE {search_by} LIKE '%{search_txt}%'")
            rows = cur.fetchall()
            if len(rows) > 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert('', END, values=row)
            else:
                messagebox.showinfo("No Records", "No matching records found!")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error in searching employee: {str(e)}")


root = Tk()
obj = EmployeeManagementSystem(root)
root.mainloop()
