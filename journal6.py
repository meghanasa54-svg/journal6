
def employee_info(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )


result = employee_info("Rahul", 101, "HR", 25000)

print(result)
