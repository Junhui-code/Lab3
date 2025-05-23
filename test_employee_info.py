import employee_info as employee
def test_get_by_Age_range():
    age_upper = 60
    age_lower = 30
    assert(employee.get_employees_by_age_range(age_lower, age_upper) == [ {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}, {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}])

def test_calculate_average_salary():
    assert(employee.calculate_average_salary() == 60166.6666666666664)

def test_get_employees_by_dept():
    assert(employee.get_employees_by_dept('Sales') == [{'name': 'John', 'age': 30, 'department': 'Sales','salary': 50000}, {'age': 40, 'department': 'Sales', 'name': 'Peter', 'salary': 60000}])