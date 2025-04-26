import sqlite3 as sql
from random import randint, choice

db = sql.connect("question.db")
cursor = db.cursor()

# for storing question and related data
def create_table():
    createTable = """
    CREATE TABLE IF NOT EXISTS quiz
    (
    qid VARCHAR(10) PRIMARY KEY,
    question VARCHAR(255),
    option1 VARCHAR(50),
    option2 VARCHAR(50),
    option3 VARCHAR(50),
    option4 VARCHAR(50),
    help VARCHAR(50)
    );
    """
    cursor.execute(createTable)

# for storing user data
def create_user_table():
    user_table = """
    CREATE TABLE IF NOT EXISTS userCredential
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID VARCHAR(20) UNIQUE,
    userName VARCHAR(50),
    userAge VARCHAR(10),
    userMail VARCHAR(100),
    userNumber VARCHAR(20),
    userPassword VARCHAR(50)
    );
    """
    cursor.execute(user_table)

# inserting question data in the database
def insert_data():
    file = open("question.Filetxt.txt", "r")
    filedata = file.readlines()
    for string in filedata:
        data = string.strip("\n").split(",")
        insert = """
                INSERT INTO quiz
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """
        cursor.execute(insert, (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    db.commit()
    file.close()
    print("Insert DATA Successfully!")

# inserting user data in the userCredential table
def insert_user(uid, uname, uage, umail, unumber, upass):
    insert = """INSERT INTO userCredential (userID, userName, userAge, userMail, userNumber, userPassword)
VALUES (?, ?, ?, ?, ?, ?)"""
    cursor.execute(insert, (uid, uname, uage, umail, unumber, upass))
    db.commit()
    print("Sign up successfully!")
    print(f"Your user id  : {uid}")
    print(f"your password : {upass}")


# fetching question and related data from the database
def select_data():
    select_qid = """
    SELECT qid FROM quiz
    """
    cursor.execute(select_qid)
    qid = cursor.fetchall()
    qid_list = []
    for i in range(10):
        random_qid = randint(0, len(qid)-1)
        get_qid = (qid[random_qid])[0]
        qid_list.append(get_qid)

    questions = f"""
    SELECT *
    FROM quiz
    WHERE qid IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(questions, qid_list)
    question_list = cursor.fetchall()

    return question_list

# fetching user_id and user_password from database
def getting_userid_pass():
    select = """
    SELECT userID, userPassword
    FROM userCredential
    """
    cursor.execute(select)
    uid_pass_list = cursor.fetchall()
    return uid_pass_list

# fetching user_email and user_password from database
def getting_useremail_pass():
    select = """
    SELECT userMail, userPassword
    FROM userCredential
    """
    cursor.execute(select)
    uemai_pass_list = cursor.fetchall()
    return uemai_pass_list

def delete_data():
    delete = """
    DELETE FROM quiz
    """
    cursor.execute(delete)
    db.commit()

create_table()
create_user_table()

# =================================================================================================================
# =================================================================================================================

winning_exclamations = [
    "I crushed it!",
    "Unstoppable!",
    "Too easy!",
    "Mission accomplished!",
    "I'm on fire!",
    "Winner winner, chicken dinner!",
    "That’s how it’s done!",
    "Flawless victory!",
    "No one can stop me!",
    "Level cleared like a boss!",
    "Victory dance time!"
]
lost_exclamations = [
    "Oh no!",
    "So close!",
    "Better luck next time!",
    "I’ll get it next time!",
    "That one hurt!",
    "Epic fail!",
    "Oof!",
    "I can't believe I missed that!",
    "Not my day...",
    "Defeat tastes bitter!",
    "That was rough!",
]


def display_question():
    count  = 0
    question_fetched = select_data()
    lst = ['a ', 'b ', 'c ', 'd ']
    for i in range(10):
        # showing question to user
        print(f"{i + 1}.", end=" ")
        print(question_fetched[i][1])
        # showing options to user
        for label, option in zip(lst, question_fetched[i][2:]):
            print(label, option)
        # taking answer as input from the user
        answer = input("Enter answer")
        answer = answer.strip(" ").lower()
        # checking the correctness of the entered answer
        if answer == question_fetched[i][6].lower():
            count += 1
            print(f"{choice(winning_exclamations)}")
        else:
            count -= 1
            print(f"{choice(lost_exclamations)}")
        print()


def game_menu():
    string = """
    -------------------------
    \t\tMAIN MENU
    -------------------------
    1. Play
    2. Show Game Statistic
    3. Insert Question
    4. Delete Question
    5. Exit
    ===========*^*==========
    """.center(20)
    print(string)

# ====================================================================================================================
# USER AUTHENTICATION
# ====================================================================================================================
def user_auth_menu():
    string = """
    ------------------------
    \t\tUSER FORM
    ------------------------
    1. Log in
    2. Sign up
    3. Exit
    """.center(20)
    print(string)

# Login Menu and choice input of user
def login_menu() -> int:
    string = """
    ------------------------
    Login Options 
    ------------------------
    1. Login using User ID
    2. Login using Email Address
    """.center(20)
    print(string)
    print("------------------------")

    user_choice = int(input("Enter operation from above : "))
    while (user_choice != 1) and (user_choice != 2):
        print("Invalid! choice")
        user_choice = int(input("Enter operation from above : "))
    return user_choice

# main login logic
def login():
    # To show login screen
    uchoice = login_menu()
    # Login by User ID
    if uchoice == 1:
        print()
        # it is a list of tuple that consist userID and userPassword
        user_id_pass = getting_userid_pass()
        print("Login using User ID")
        print("------------------------")
        user_id = input("Enter your user id : ")
        user_pass = input("Enter your password : ")
        if (user_id, user_pass) in user_id_pass:
            print("User Verified!")
            return 1
        else:
            print("User ID or User Password is wrong!")
            return -1
    # Login by User Mail
    else:
        user_email_pass = getting_useremail_pass()
        print("Login using User Email")
        print("------------------------")
        user_email = input("Enter your email")
        user_pass = input("Enter your password")
        if (user_email, user_pass) in user_email_pass:
            print("User Verified!")
            return 1
        else:
            print("User Email or User Password is wrong!")
            return -1


# taking input for the sign-up
def sign_up_input():
    user_name = input("Enter your name : ")
    user_age = input("Enter your age : ")
    user_mail = input("Enter Your mail : ")
    user_number = input("Enter your phone number : ")
    password = input("create a password : ")
    confirm_password = input("Re-enter password : ")
    while password != confirm_password:
        print("Password doesn't match!")
        password = input("create a password : ")
        confirm_password = input("Re-enter password : ")
    return user_name, user_age, user_mail, user_number, password

# it will unpack user ids from the list  of tuple and add it's to a list
def unpack_ids(ids):
    ids_list = []
    if len(ids) > 0:
        for tuple_id in ids:
            ids_list.append(tuple_id[0])
        return ids_list
    return -1

# function to create unique user id
def create_unique_user_id(username):
    users_id = """
    SELECT id
    FROM userCredential
    """
    cursor.execute(users_id)
    ids = cursor.fetchall()
    if unpack_ids(ids) != -1:
        id_list = unpack_ids(ids)
        last_id = id_list[len(id_list) - 1]
        new_last_id = str(last_id + 1)
        new_user_id = username + new_last_id
        return new_user_id
    else:
        return -1

# ======================================================================================================================
# ======================================================================================================================

def main_game_loop():
    flag = True
    while flag:
        game_menu()
        user_choice = int(input("Enter operation choice here : "))
        if user_choice == 1:
            display_question()
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        elif user_choice == 5:
            flag = False
        else:
            pass


def main_window_loop():
    main_flag = True
    while main_flag:
        user_auth_menu()
        credential_choice = int(input("Enter above operation : "))
        if credential_choice == 1:
            # show login method
            return_value = login()
            if return_value == 1:
                main_game_loop()
            else:
                main_flag = False
        elif credential_choice == 2:
            # for creating new user
            uname, uage, umail, unumber, upass = sign_up_input()
            # creating new user id
            if create_unique_user_id(uname) != -1:
                new_u_id = create_unique_user_id(uname)
                # insert new user in database
                insert_user(uid=new_u_id, uname=uname, uage=uage, umail=umail, unumber=unumber, upass=upass)
            else:
                print("Unable to create unique user id!")
        elif credential_choice == 3:
            main_flag = False
        else:
            print("Invalid! choice")


main_window_loop()

cursor.close()
db.close()