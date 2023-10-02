import sqlite3

def write_to_database(file_path):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)''')
    with open(file_path, 'r') as file:
        data = file.readlines()
        cursor.executemany('INSERT INTO data (content) VALUES (?)', [(line.strip(),) for line in data])
    connection.commit()
    connection.close()

def read_from_database_and_write_to_file(output_file_path):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT content FROM data')
    data = cursor.fetchall()
    with open(output_file_path, 'w') as file:
        for row in data:
            file.write(row[0] + '\n')
    connection.close()

input_file_path = 'input_data.txt'
output_file_path = 'output_data.txt'

write_to_database(input_file_path)
read_from_database_and_write_to_file(output_file_path)
