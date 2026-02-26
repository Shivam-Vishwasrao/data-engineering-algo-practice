records = [
    {"name": "Aman", "salary": 80000},
    {"name": "Riya", "salary": 90000},
    {"name": "Kabir", "salary": 60000}
]

def highestSalary(records):
    
    max_emp = records[0]
    for emp in records:
        if emp["salary"] > max_emp['salary']:
            max_emp = emp
        
    return max_emp

print(highestSalary(records))