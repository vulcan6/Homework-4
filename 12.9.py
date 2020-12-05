# Erick Jimenez
# PSID 1463639
# Zylab 12.9

 # Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
    # while names and ages end with -1. Hoping I understood that right
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except Exception as ex:
        age = 0
    print('{} {}'.format(name, age))
    parts = input().split()
    name = parts[0]