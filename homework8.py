import sqlite3
with sqlite3.connect('person.db') as connect:
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        DepartmentID INTEGER PRIMARY KEY,
        DepartmentName TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        DepartmentID INTEGER,
        FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    )
    ''')

    departments = [
        (101, 'HR'),
        (102, 'IT'),
        (103, 'Sales')
    ]
    cursor.executemany('INSERT INTO Departments (DepartmentID,'
                       ' DepartmentName) VALUES (?, ?)', departments)
    employees = [
        ('John', 'Doe', 101),
        ('Jane', 'Smith', 101),
        ('Alice', 'Johnson', 102),
        ('Bob', 'Brown', 102),
        ('Charlie', 'Davis', 103),
        ('Emily', 'Wilson', 103)
    ]
    cursor.executemany('INSERT INTO Employees (FirstName,'
                       ' LastName, DepartmentID) VALUES (?, ?, ?)', employees)
    connect.commit()
    print("Список всех сотрудников с указанием оделов:")
    cursor.execute('''
    SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
    FROM Employees
    JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
    ''')

    for row in cursor.fetchall():
        print(row)
    print("\nсписок сотрудников отдела IT:")
    cursor.execute('''
    SELECT Employees.FirstName, Employees.LastName
    FROM Employees
    JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
    WHERE Departments.DepartmentName = 'IT'
    ''')
    for row in cursor.fetchall():
        print(row)
