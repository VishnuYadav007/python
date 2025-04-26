from tabulate import tabulate

# insert student data into the list
def insert(empdb):
    global lst
    cl = []
    for i in lst:
        cl.append(input(f'Enter {i} '))
    empdb.append(cl)

# update student data in the database
def update(empdb, find):
    #update logic
    global lst
    for index, attribute in enumerate(lst, 0):
        empdb[find][index] = input(f'Enter {attribute} : ')

def delete(empdb, find):
    empdb.remove(empdb[find])

def show_one_student(studentIndex, empdb):
    global lst
    data = []
    for attribute in range(0, 5):
        data.append([lst[attribute].capitalize(), empdb[studentIndex][attribute]])
    print(tabulate(data, headers=['Attributes', 'Details'], tablefmt='grid'))      


def show_all_student(empdb):
    global lst
    print(tabulate(empdb, headers=lst, tablefmt='grid'))

def search(empdb, rollno) -> int:
    index = -1
    for student in empdb:
        if student[1] == rollno:
            index = empdb.index(student)
            return index
    return index

# empdb -> contains the data of the each student
empdb = []
# lst -> list contains all the essential attributes of the student
lst = ['name', 'rollno','semester', 'cgpa', 'email']

flag = True
while flag:
    menu_data = """\n\n\t\tMain Menu
    1 : Insert student details
    2 : Update student details
    3 : Delete student details
    4 : Show all students
    5 : Search students
    6 : Exit
    """
    choice = int(input(menu_data + 'Enter your choice : '))
    
    if choice == 1:
        # Insert parts
        insert(empdb)
    elif choice == 2:
        # Update parts
        stdRoll = input('Enter roll no. : ')
        find = search(empdb, stdRoll)
        if find != -1:
            update(empdb, find)
        else:
            print('Student does not exist!')
    elif choice == 3:
        # delete part here
        stdRoll = input('Enter roll no. : ')
        find = search(empdb, stdRoll)
        if find != -1:
            delete(empdb, find)
        else:
            print("Enter a valid roll no!")
    elif choice == 4:
        # showing part here
        if len(empdb) != 0:
            show_all_student(empdb)
        else:
            print('Database is empty!')
    elif choice == 5:
        # searching part here
        stdRoll = input('Enter student roll no. : ')
        find = search(empdb, stdRoll)
        if find != -1:
            print("\n============= Student Details =============")
            show_one_student(find, empdb)
        else:
            print(f"Student with roll no. {stdRoll} doesn't exist!")
    elif choice == 6:
        # for exiting from the loop
        choice = input('enter y/n : ')
        if choice == 'y' or choice == 'Y':
            flag = False
        else:
            flag = True
    else:
        print('Enter a valid choice!')