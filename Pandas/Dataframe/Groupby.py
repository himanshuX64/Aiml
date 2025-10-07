import pandas as pd

data = {
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance'],
    'Salary': [60000, 70000, 50000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

# Group by Department
grouped = df.groupby('Department')

# Average salary har department me
print(grouped['Salary'].mean())
