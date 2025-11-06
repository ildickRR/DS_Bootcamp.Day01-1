import sys


if len(sys.ar-gv) < 2:
    print("Долбаеб, введи имя файла")
    sys.exit()

input_file = sys.argv[1]
output_file = "employees.tsv"

with open(input_file, "r", encoding="utf-8") as f:
    emails = f.read().splitlines()

rows = ["Name\tSurname\tE-mail"]

for email in emails:
    if not email.strip():  
        continue
    
    local_part = email.split("@")[0] 
    parts = local_part.split(".")      
    

    name = parts[0].capitalize()
    surname = parts[1].capitalize()
    
    rows.append(f"{name}\t{surname}\t{email}")


with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(rows))

print(f"✅ File '{output_file}'респект")
