import employee_info as test

def test_average_salary():
    result = test.calculate_average_salary()
    assert(result == 60166.67)

def test_get_employees_by_age_range():
    result = test.get_employees_by_age_range(20,30)
    employee_data = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    assert(result == employee_data)

def test_get_employees_by_dept():
    result = test.get_employees_by_dept("Sales")
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    assert(result == employee_data) 