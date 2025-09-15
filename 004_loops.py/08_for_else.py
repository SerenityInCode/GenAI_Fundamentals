#else loop will only execute if the loop doesn't break

staff=[('Amit',15), ('Sonia',17), ('Dev',15)]

for name,age in staff:
    if age < 18:
        print(f"{name} can manage the staff")
        break
else:
    print("Not eligible to manage the staff")    