import csv

data = [ 
    ['Name', 'Salary', 'Designation', 'Department', 'Location'],
    ['Alice', 70000, 'Software Engineer', 'IT', 'New York'],
    ['Bob', 85000, 'Data Scientist', 'Data Science', 'San Francisco'],
    ['Charlie', 60000, 'HR Manager', 'Human Resources', 'Chicago'],
    ['David', 75000, 'Product Manager', 'Product', 'Austin'],
    ['Eve', 90000, 'Marketing Specialist', 'Marketing', 'Los Angeles'],
    ['Frank', 65000, 'Systems Analyst', 'IT', 'Seattle'],
    ['Grace', 72000, 'UX Designer', 'Design', 'Boston'],
    ['Hank', 80000, 'DevOps Engineer', 'IT', 'Denver'],
    ['Ivy', 68000, 'Content Writer', 'Content', 'New York'],
    ['Jack', 95000, 'Chief Technology Officer', 'IT', 'San Francisco']
]
with open('module_4/my.csv', 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)
    print('CSV file created')

with open('module_4/my.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)
