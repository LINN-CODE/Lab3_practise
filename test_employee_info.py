import employee_info as test

def test_average_salary():
    result = test.calculate_average_salary()
    assert(result == 60166.67)