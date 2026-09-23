from create_database_file import get_sql_cursor

# Create database and get cursor
cursor = get_sql_cursor()

with open("input1.txt", encoding="utf-8") as in_file:
    # Read input from input1.txt
    search_string = in_file.read()
    print(f"Searching for Student with name {search_string}")

    # Format a string for the SQL SELECT statement
    execute_str = "SELECT * FROM Student WHERE first_name = ?"

    # Run statement and print results
    results = cursor.execute(execute_str, (search_string))

# Get a list of all student details and store in a list
database_info = cursor.execute("SELECT * FROM Student;")
fetch_results = database_info.fetchall()

# Check if list length is zero - if it is zero, entries have been deleted
if len(fetch_results) == 0:
    print("We have been hacked! There are no records in the table!")
else:
    print(f"Thank you for using our system, {search_string}. Have a nice day!")