"""
1. Insert new employee
2. Update email of the employee
3. Delete employee on behalf of eid
4. Search employee
5. Search according to deptno
6. Show all employees
7. Exit
"""
from webbrowser import open_new

employee_column = ['eid', 'fname', 'lname', 'email', 'phone', 'hiredate', 'jobid', 'salary', 'comm', 'mid', 'did']
employee_input = []

def operation_menu():
    print("""
    ---------------------------------------    
    \t\t\tMain Menu
    ---------------------------------------
    1. Insert New Employee
    2. Update Email of the Employee
    3. Delete Employee on Behalf of eid
    4. Search Employee
    5. Search According to deptno
    6. Show All Employee
    7. Exit
    ============= *^* ====================\n
    """)

# function to take input from the user
def input_data():
    global employee_input
    for column in employee_column:
        data = input(f"{column} : ")
        employee_input.append(data)

# Insert() -> function to insert employee data
def insert():
    file = open("emp.txt", "a")
    input_data()
    file.write(",".join(employee_input) + "\n")

    employee_input.clear()
    file.close()

def search_by_eid(eid : str) -> tuple[int, list[str]] | int:
    file = open("emp.txt", "r")
    filedata = file.readlines()
    file.close()
    for i, line in enumerate(filedata):
        emp_data = line.strip().split(",")
        if  emp_data[0] == eid:
            return i, filedata
    return -1

def search_by_deptno(deptno : str) -> int | str | None:
    did_member = []
    file = open("emp.txt", "r")
    filedata = file.readlines()
    for index, string in enumerate(filedata):
        filedata[index] = string.strip("\n").split(",")
        if filedata[index][-1] == deptno:
            did_member.append(filedata[index])
    if len(did_member) == 0:
        return -1
    else:
        return did_member

def update_by_eid(eid):
    global employee_input
    if search_by_eid(eid) != -1:
        print("Person Found!")
        print("Enter new data below")
        index, emp_data = search_by_eid(eid)
        input_data()
        emp_data[index] = ",".join(employee_input) + "\n"
        file = open("emp.txt", "w")
        file.writelines(emp_data)
        file.close()
        employee_input.clear()
        print("Data updated successfully!")
    else:
        print("Update failed: person not found in the database!")


def delete_by_eid(eid):
    if search_by_eid(eid) != -1:
        index, filedata = search_by_eid(eid)
        filedata.pop(index)
        file = open("emp.txt", "w")
        file.writelines(filedata)
        file.close()
        print("Record deleted successfully!")
    else:
        print("Invalid eid!")


def show_all():
    file = open("emp.txt", "r")
    filedata = file.readlines()
    for employee in filedata:
        data = employee.strip("\n").split(",")
        print(f"{data[0]:<4} {data[1]:<15} {data[2]:<15} {data[3]:<25} {data[4]:<20} {data[5]:<15} {data[6]:<15} {data[7]:<10} {data[8]:<7} {data[8]:<7} {data[9]:<7}")
        print("-" * 147)
    file.close()


flag = True
while flag:
    operation_menu()
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        print()
        insert()
    elif choice == 2:
        print()
        eid = input("Enter eid of the employee : ")
        update_by_eid(eid)
    elif choice == 3:
        print()
        eid = input("Enter eid to delete record : ")
        delete_by_eid(eid)
    elif choice == 4:
        print()
        eid = input("Enter eid of the employee : ")
        if search_by_eid(eid) != -1:
            index, data = search_by_eid(eid)
            emp_data = data[index].strip("\n").split(",")
            for i, values in enumerate(emp_data):
                print(f"{employee_column[i]:<12} : {values}")
        else:
            print("Employee not found!")
    elif choice == 5:
        print()
        deptno = input("Enter deptno of the employee : ")
        print()
        return_value = search_by_deptno(deptno)
        if return_value != -1:
            for values_list in return_value:
                print()
                for i in range(0, 11):
                    print(f"{" ":<10} {employee_column[i].capitalize():<12} {":":<6} {values_list[i]:<6}")

                print()
                print("=" * 55)
        else:
            print("Employee not exist!")
    elif choice == 6:
        print()
        show_all()
    elif choice == 7:
        flag = False
    else:
        print("Error! Enter a valid choice!")
