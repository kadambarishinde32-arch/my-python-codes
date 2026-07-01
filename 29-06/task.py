import sqlite3

# Connect to Database
con = sqlite3.connect("stud.db")
cur = con.cursor()

# Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    subject1 INTEGER,
    subject2 INTEGER,
    subject3 INTEGER
)
""")

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Update Marks to Zero")
    print("3. Read All Students")
    print("4. Search Student")
    print("5. Delete Records")
    print("6. View Result")
    print("7. Reports")
    print("8. Download Report Card")
    print("9. Email Report Card")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        # ---------------- ADD STUDENT ----------------
        case 1:
            sid = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")

            s1 = int(input("Enter Subject 1 Marks: "))
            s2 = int(input("Enter Subject 2 Marks: "))
            s3 = int(input("Enter Subject 3 Marks: "))

            cur.execute(
                "INSERT INTO student VALUES(?,?,?,?,?,?)",
                (sid, name, email, s1, s2, s3)
            )

            con.commit()
            print("\nStudent Added Successfully!")

        # ---------------- UPDATE ----------------
        case 2:

            sid = int(input("Enter Student ID: "))

            cur.execute(
                """
                UPDATE student
                SET subject1=0,
                    subject2=0,
                    subject3=0
                WHERE id=?
                """,
                (sid,)
            )

            con.commit()

            if cur.rowcount > 0:
                print("\nAll subject marks updated to 0.")
            else:
                print("\nStudent ID not found.")

        # ---------------- PLACEHOLDERS ----------------

        case 3:

            cur.execute("SELECT * FROM student")

            records = cur.fetchall()

            if len(records) == 0:
                print("\nNo Records Found!")

            else:

                 print("\n------------------------------------------------------------------------------------------------")
                 print("ID\tName\t\tEmail\t\t\tS1\tS2\tS3\tTotal\tPercentage")
                 print("------------------------------------------------------------------------------------------------")

            for row in records:

             total = row[3] + row[4] + row[5]
            percentage = total / 3

            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{total}\t{percentage:.2f}")
            

        case 4:
            

            print("\nSearch By")
            print("1. ID")
            print("2. Name")
            print("3. Total Marks")

            ch = int(input("Enter Choice: "))

            match ch:

                case 1:

                    sid = int(input("Enter Student ID: "))

                    cur.execute("SELECT * FROM student WHERE id=?", (sid,))

                    row = cur.fetchone()

                    if row:

                        total = row[3] + row[4] + row[5]
                        percentage = total / 3

                        print("\nStudent Found")
                        print("----------------------------")
                        print("ID :", row[0])
                        print("Name :", row[1])
                        print("Email :", row[2])
                        print("Subject1 :", row[3])
                        print("Subject2 :", row[4])
                        print("Subject3 :", row[5])
                        print("Total :", total)
                        print("Percentage :", round(percentage,2))

                    else:
                        print("Student Not Found.")

                case 2:

                    name = input("Enter Student Name: ")

                    cur.execute("SELECT * FROM student WHERE name LIKE ?",('%'+name+'%',))

                    rows = cur.fetchall()

                    if rows:

                        for row in rows:

                            total = row[3] + row[4] + row[5]

                            print("--------------------------------")
                            print("ID :", row[0])
                            print("Name :", row[1])
                            print("Email :", row[2])
                            print("Total :", total)

                    else:
                        print("Student Not Found.")

                case 3:

                    marks = int(input("Enter Total Marks: "))

                    cur.execute("SELECT * FROM student")

                    rows = cur.fetchall()

                    found = False

                    for row in rows:

                        total = row[3] + row[4] + row[5]

                        if total == marks:

                            percentage = total / 3

                            print("--------------------------------")
                            print("ID :", row[0])
                            print("Name :", row[1])
                            print("Email :", row[2])
                            print("Total :", total)
                            print("Percentage :", round(percentage,2))

                            found = True

                    if not found:
                        print("No Student Found.")

                case _:
                    print("Invalid Choice")

        case 5:

            print("\nDelete Menu")
            print("1. Delete By ID")
            print("2. Delete All Records")

            ch = int(input("Enter Choice: "))

            match ch:

                case 1:

                    sid = int(input("Enter Student ID: "))

                    cur.execute("DELETE FROM student WHERE id=?", (sid,))

                    con.commit()

                    if cur.rowcount > 0:
                        print("Student Deleted Successfully.")
                    else:
                        print("Student ID Not Found.")

                case 2:

                    confirm = input("Are you sure? (yes/no): ")

                    if confirm.lower() == "yes":

                        cur.execute("DELETE FROM student")

                        con.commit()

                        print("All Records Deleted Successfully.")

                    else:
                        print("Operation Cancelled.")

                case _:
                    print("Invalid Choice.")
            

        case 6:

            sid = int(input("Enter Student ID: "))

            cur.execute("SELECT * FROM student WHERE id=?", (sid,))

            row = cur.fetchone()

            if row:

                total = row[3] + row[4] + row[5]
                percentage = total / 3

                print("\n========== RESULT ==========")
                print("Student ID :", row[0])
                print("Name       :", row[1])
                print("Email      :", row[2])
                print("Subject 1  :", row[3])
                print("Subject 2  :", row[4])
                print("Subject 3  :", row[5])
                print("Total      :", total)
                print("Percentage :", round(percentage,2), "%")

                if percentage >= 35:
                    print("Result     : PASS")
                else:
                    print("Result     : FAIL")

            else:
                print("Student Not Found.")

        case 7:

            print("\nREPORT MENU")
            print("1. Pass Students")
            print("2. Fail Students")

            ch = int(input("Enter Choice: "))

            cur.execute("SELECT * FROM student")

            rows = cur.fetchall()

            found = False

            match ch:

                case 1:

                    print("\n========== PASS STUDENTS ==========")

                    for row in rows:

                        total = row[3] + row[4] + row[5]
                        percentage = total / 3

                        if percentage >= 35:

                            print("-----------------------------------")
                            print("ID :", row[0])
                            print("Name :", row[1])
                            print("Total :", total)
                            print("Percentage :", round(percentage,2))

                            found = True

                    if not found:
                        print("No Pass Students Found.")

                case 2:

                    print("\n========== FAIL STUDENTS ==========")

                    for row in rows:

                        total = row[3] + row[4] + row[5]
                        percentage = total / 3

                        if percentage < 35:

                            print("-----------------------------------")
                            print("ID :", row[0])
                            print("Name :", row[1])
                            print("Total :", total)
                            print("Percentage :", round(percentage,2))

                            found = True

                    if not found:
                        print("No Fail Students Found.")

                case _:
                    print("Invalid Choice.")

      

        case 8:
            print("\nThank You!")
            break

        case _:
            print("\nInvalid Choice!")

con.close()