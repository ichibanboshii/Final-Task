import sys
import re
import random

def generate_email(student_id, name):
    lastname, firstname = re.split(r'\s*,\s*', name)
    initials = '.'.join([x[0] for x in firstname.split()])
    lastname = re.sub(r'[^a-zA-Z]+', '', lastname)
    email = f'{initials}.{lastname}{random.randint(1000, 9999)}@poppleton.ac.uk'
    return email.lower()

if len(sys.argv) == 2:
    print("Error: Missing command-line argument.")
    sys.exit(1)

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    input_file = "students.txt"
    output_file = "emails.txt"
try:
    with open(input_file, "r") as f:
        lines = f.readlines()
    with open(output_file, "w") as f:
        for line in lines:
            student_id, name = line.split()[0], line.split()[1:]
            f.write(f'{student_id} {generate_email(student_id, " ".join(name))}\n')
except FileNotFoundError:
    print(f'Error: Cannot open {input_file}. Sorry about that.')
