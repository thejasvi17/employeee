name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
phone = input("Enter Phone Number: ")

with open("employee.txt", "a") as file:
    file.write(f"{name}, {emp_id}, {phone}\n")

print("Employee Details Saved Successfully!")