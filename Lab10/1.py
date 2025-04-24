import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    host="localhost",
    password="Baton2018",
    port=5432
)
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS PhoneBook;")
cur.execute("""
    CREATE TABLE PhoneBook(
        Name VARCHAR(255) NOT NULL,
        Phone VARCHAR(255) NOT NULL 
    )
""")
conn.commit()


while True:
    print("")
    print("Do you want to:")
    print("I: Input")
    print("U: Update")
    print("R: Read")
    print("D: Delete")
    print("Q: Quit")
    command=input("Command: ")
    if command == "Q":
        break
    elif command == "I":
        print("Get information by:")
        print("F: File(csv)")
        print("T: Terminal")
        choice = input("Your choice: ")
        if choice == "T":
            name=input("Name:")
            phone=input("Phone:")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s AND Phone = %s);", (name, phone))
            exist = cur.fetchone()[0]
            if exist:
                print("It already exists.")
            else:
                cur.execute("INSERT INTO PhoneBook(Name, Phone) VALUES(%s,%s)",(name,phone))
        elif choice == "F":
            with open(input("Path: "), 'r') as file:
                cur.copy_expert("""
                COPY PhoneBook(Name, Phone)
                FROM STDIN WITH CSV HEADER DELIMITER ','
                """, file)
                conn.commit()
    elif command == "U":
        print("Do you want to update:")
        print("N: Name")
        print("P: Phone")
        choice = input()
        if choice == "N":
            old_name = input("Current Name: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s);", (old_name,))
            exist = cur.fetchone()[0]
            if exist:
                new_name = input("New Name: ")
                cur.execute("UPDATE PhoneBook SET Name = %s WHERE Name = %s;", (new_name, old_name))
            else:
                print("This name doesnt exist.")
        elif choice == "P":
            old_phone = input("Current Phone: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Phone = %s);", (old_phone,))
            exist = cur.fetchone()[0]
            if exist:
                new_phone = input("New Phone: ")
                cur.execute("UPDATE PhoneBook SET Phone = %s WHERE Phone = %s;", (new_phone, old_phone))
            else:
                print("This phone doesnt exist.")
    elif command == "R":
        print("Sort by column:")
        print("N: Name")
        print("P: Phone")
        print("ELSE: Unsorted data")
        choice = input("Your choice: ")
        show = "*"
        sort = "" 
        if choice == "N" or choice == "P":
            col = "Name" if choice == "N" else "Phone"
            print("Choose sort order:")
            print("A: Ascending")
            print("D: Descending")
            print("ELSE: Unchanged")
            choice = input("Your choice: ")
            if choice == "A":
                sort = f"ORDER BY {col} ASC"
            elif choice == "D":
                sort = f"ORDER BY {col} DESC"
            print("Show:")
            print("N: Name")
            print("P: Phone")
            print("ELSE: Both name and phone")
            choice = input("Your choice: ")
            if choice == "N":
                show = "Name"
            elif choice == "P":
                show = "Phone"
            choice = ""

        cur.execute(f"SELECT {show} FROM PhoneBook {sort};")
        rows = cur.fetchall()
        if show == "*":
            show = "Name      Phone"
        if rows:
            print(show)
            print("-" * len(show)*3)
            for row in rows:
                print(" | ".join(row))
        else:
            print("")
            print("No records found.")
    elif command == "D":
        print("Delete by:")
        print("N: Name")
        print("P: Phone")
        choice = input("Your choice: ")
        if choice == "N":
            del_name = input("Deleting Name: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s);", (del_name,))
            exist = cur.fetchone()[0]
            if exist:
                cur.execute("DELETE FROM PhoneBook WHERE Name = %s;", (del_name,))
            else:
                print("This name doesnt exist.")
        elif choice == "P":
            del_phone = input("Deleting Phone: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Phone = %s);", (del_phone,))
            exist = cur.fetchone()[0]
            if exist:
                cur.execute("DELETE FROM PhoneBook WHERE Phone = %s;", (del_phone,))
            else:
                print("This phone doesnt exist.")
            
cur.close()
conn.close()