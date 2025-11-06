import sys

if len(sys.argv) < 2:
    print("Введите email как аргумент")
    sys.exit()

input_email = sys.argv[1]         
employees_file = "employees.tsv"  


name_found = None
with open(employees_file, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
    for line in lines[1:]: 
        parts = line.split("\t")
        if len(parts) == 3:
            name, surname, email = parts
            if email.lower() == input_email.lower():  
                name_found = name
                break

if name_found:
    letter = (
        f"Уважаемый {name_found}, добро пожаловать в нашу команду. "
        "Мы уверены, что с нами будет приятно работать. "
        "Это обязательное условие для специалистов, которых нанимает наша компания."
    )
    print(letter)
else:
    print(f"Email '{input_email}' не найден в {employees_file}")
