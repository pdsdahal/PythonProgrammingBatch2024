import csv
import os

current_file_absolute_path = os.getcwd()
base_path = os.path.dirname(current_file_absolute_path)
file_path = os.path.join(base_path, 'Resources', 'Student.csv')

with open(file=file_path, mode='r+', newline='') as student_file:
    # Write

    # Move the file pointer to the end of the file for appending new data
    student_file.seek(0,2)
    row = ['5', 'Ullash Dullal', 'India']
    csv_writer = csv.writer(student_file)
    csv_writer.writerow(row)

    # Read
    # Move the file pointer back to the beginning to read the updated content
    student_file.seek(0)
    csv_reader = csv.reader(student_file)

    # Skip the header
    header = next(csv_reader)
    print("Header : ", header)

    for row in csv_reader:
        student_id = row[0]
        student_name = row[1]
        student_address = row[2]
        print(student_id, student_name)