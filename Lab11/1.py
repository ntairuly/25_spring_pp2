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

cur.execute("DROP TABLE IF EXISTS PhoneBookErrors;")
cur.execute("""
    CREATE TABLE PhoneBookErrors(
        error TEXT NOT NULL
    )
""")
conn.commit()

cur.execute("""
CREATE OR REPLACE PROCEDURE insert_many_users_proc(
    names_arr TEXT[],
    phones_arr TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    v_error TEXT;
BEGIN
    TRUNCATE TABLE PhoneBookErrors;
    IF array_length(names_arr, 1) IS NULL 
       OR array_length(phones_arr, 1) IS NULL 
       OR array_length(names_arr, 1) <> array_length(phones_arr, 1) THEN
       RAISE EXCEPTION 'Names and Phones arrays must have the same number of elements';
    END IF;
    FOR i IN 1..array_length(names_arr, 1) LOOP
       IF NOT (phones_arr[i] ~ '^\+?[0-9]+$') THEN
          v_error := 'Name: ' || names_arr[i] || ', Phone: ' || phones_arr[i];
          INSERT INTO PhoneBookErrors(error) VALUES (v_error);
       ELSE
          INSERT INTO PhoneBook(Name, Phone) VALUES (names_arr[i], phones_arr[i]);
       END IF;
    END LOOP;
END;
$$;
""")
conn.commit()

cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE Name = p_name) THEN
        UPDATE PhoneBook SET Phone = p_phone WHERE Name = p_name;
    ELSE
        INSERT INTO PhoneBook(Name, Phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
""")
conn.commit()

cur.execute("""
CREATE OR REPLACE PROCEDURE delete_from_phonebook_proc(
    p_deletion_type TEXT,
    p_value TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_deletion_type = 'N' THEN
        DELETE FROM PhoneBook WHERE Name = p_value;
    ELSIF p_deletion_type = 'P' THEN
        DELETE FROM PhoneBook WHERE Phone = p_value;
    ELSE
        RAISE EXCEPTION 'Invalid deletion type. Use "N" for Name or "P" for Phone.';
    END IF;
END;
$$;
""")
conn.commit()

def query_paginated_data(cur, table_name, limit=10, offset=0):
    allowed_tables = ["PhoneBook", "PhoneBookErrors"]
    if table_name not in allowed_tables:
        raise ValueError("Invalid table name. Please choose a valid table.")
    query = f"SELECT * FROM {table_name} ORDER BY 1 LIMIT %s OFFSET %s;"
    cur.execute(query, (limit, offset))
    return cur.fetchall()

def pattern(cur, column, position, data):
    print("Sort by column:")
    print("N: Name")
    print("P: Phone")
    print("Any other key: Unsorted data")
    sort_input = input("Your choice: ")
    sort_clause = ""
    if sort_input == "N" or sort_input == "P":
        sort_col = "Name" if sort_input == "N" else "Phone"
        print("Choose sort order:")
        print("A: Ascending")
        print("D: Descending")
        print("Any other key: Unsorted data")
        order_input = input("Your choice: ")
        if order_input == "A":
            sort_clause = f" ORDER BY {sort_col} ASC"
        elif order_input == "D":
            sort_clause = f" ORDER BY {sort_col} DESC"
    print("Show columns:")
    print("N: Name")
    print("P: Phone")
    print("Any other key: Both Name and Phone")
    show_input = input("Your choice: ")
    if show_input == "N":
        show_clause = "Name"
    elif show_input == "P":
        show_clause = "Phone"
    else:
        show_clause = "*"
    if position == "B":
        search_pattern = f"{data}%"
    elif position == "E":
        search_pattern = f"%{data}"
    else:
        search_pattern = f"%{data}%"
    column_clause = f"WHERE {column} LIKE %s" if column != "*" else ""
    cur.execute(f"SELECT {show_clause} FROM PhoneBook {column_clause}{sort_clause};", (search_pattern,))
    rows = cur.fetchall()
    if rows:
        if show_clause == "*":
            print("Name      Phone")
            print("-" * 25)
            for row in rows:
                print(" | ".join(row))
        else:
            print(show_clause)
            print("-" * 25)
            for row in rows:
                print(row[0])
    else:
        print("The data with such pattern doesn't exist.")

while True:
    print("")
    print("Do you want to:")
    print("I: Input")
    print("U: Update")
    print("R: Read")
    print("D: Delete")
    print("P: Pagination Query")
    print("Q: Quit")
    command = input("Command: ")
    if command == "Q":
        break
    elif command == "I":
        print("Get information by:")
        print("F: File(csv)")
        print("T: Terminal")
        choice = input("Your choice: ")
        if choice == "T":
            print("Do you want to input:")
            print("O: Only one data")
            print("M: More than one data")
            choice = input("Your choice: ")
            if choice == "O":
                name = input("Name: ")
                phone = input("Phone: ")
                cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
                conn.commit()
            elif choice == "M":
                try:
                    num = int(input("How many records do you want to insert? "))
                except ValueError:
                    print("Invalid number. Operation aborted.")
                    continue
                names_list = []
                phones_list = []
                for i in range(num):
                    n = input(f"Enter name for record {i+1}: ")
                    p = input(f"Enter phone for record {i+1}: ")
                    names_list.append(n)
                    phones_list.append(p)
                cur.execute("CALL insert_many_users_proc(%s, %s);", (names_list, phones_list))
                conn.commit()
                cur.execute("SELECT error FROM PhoneBookErrors;")
                errors = cur.fetchall()
                if errors:
                    print("The following entries have incorrect phone numbers:")
                    for err in errors:
                        print(err[0])
                else:
                    print("All records were inserted successfully!")
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
        choice = input("Your choice: ")
        if choice == "N":
            old_name = input("Current Name: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s);", (old_name,))
            exist = cur.fetchone()[0]
            if exist:
                new_name = input("New Name: ")
                cur.execute("UPDATE PhoneBook SET Name = %s WHERE Name = %s;", (new_name, old_name))
            else:
                print("This name doesn't exist.")
        elif choice == "P":
            old_phone = input("Current Phone: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Phone = %s);", (old_phone,))
            exist = cur.fetchone()[0]
            if exist:
                new_phone = input("New Phone: ")
                cur.execute("UPDATE PhoneBook SET Phone = %s WHERE Phone = %s;", (new_phone, old_phone))
            else:
                print("This phone doesn't exist.")
        conn.commit()
    elif command == "R":
        print("Search by: ")
        print("N: Name")
        print("P: Phone")
        print("Any other key: Skip")
        column = input("Your choice: ")
        if column == "N":
            column = "Name"
        elif column == "P":
            column = "Phone"
        else:
            column = "*"
        position = ""
        data = ""
        if column != "*":
            print("Search at: ")
            print("B: Begining")
            print("E: End")
            print("Any other key: All interval")
            position = input("Your choice: ")
            data = input("Enter partial data: ")
        pattern(cur, column, position, data)
    elif command == "D":
        print("Delete by:")
        print("N: Name")
        print("P: Phone")
        choice = input("Your choice: ")
        if choice == "N":
            value = input("Deleting Name: ")
            cur.execute("CALL delete_from_phonebook_proc(%s, %s);", (choice, value))
        elif choice == "P":
            value = input("Deleting Phone: ")
            cur.execute("CALL delete_from_phonebook_proc(%s, %s);", (choice, value))
        conn.commit()
    elif command == "P":
        print("Enter table name (PhoneBook or PhoneBookErrors):")
        table = input("Table: ")
        try:
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
        except ValueError:
            print("Invalid input for limit or offset.")
            continue
        try:
            results = query_paginated_data(cur, table, limit=limit, offset=offset)
            if results:
                print("Results:")
                for row in results:
                    print(row)
            else:
                print("No records found.")
        except ValueError as ve:
            print("Error:", ve)
conn.commit()
cur.close()
conn.close()