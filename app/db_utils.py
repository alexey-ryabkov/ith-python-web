def execute_sql_file(cursor, file_path):
    with open(file_path, "r") as file:
        sql_commands = file.read().split(";")
        for command in sql_commands:
            if command.strip():
                cursor.execute(command)
