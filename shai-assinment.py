#Q1: Basic Data Exploration
# Number of rows and columns
number of rows, number of columns = df.shape
print(f"Number of rows: {num_rows}, Number of columns: {num_cols}")

# The data type of each column
datatype = df.dtypes
print("\nData type of each column:\n", data_types)

# Check for missing values
missing_values ​​= df.isnull().sum()
print("\nEach column has missing values:\n", missing_values)

#####################################################

#Q2: Descriptive Statistics
# Basic salary statistics (TotalPay column)
Payroll statistics = df['TotalPay'].describe()
print("\nBasic salary statistics:\n", Salary_Statistics)

#####################################################

# Range of rights
Salary range = df['TotalPay'].max() - df['TotalPay'].min()
print("\nSalary range: "salary_range)

#####################################################

# Standard deviation of rights
salary_std = df['TotalPay'].std()
print("\nSalary standard deviation:",salary_std)

#####################################################

#Q3:  Data Cleaning
# Handle missing values ​​by filling the column mean with NaN
df['Benefits'].fillna(df['Benefits'].mean(), inplace=True)

#####################################################

#Q4: Basic Data Visualization
Import matplotlib.pyplot as plt
# Histogram of salary distribution
plt.hist(df['TotalPay'], bins=20, color='blue', edgecolor='black')
plt.title("rights distribution")
plt.xlabel("TotalPay")
plt.ylabel("frequency")
plt.show()

# Pie chart showing the percentage of employees in different departments (using the "JobTitle" column)
department count = df['job title'].value_counts()
plt.pie(DepartmentCount, label=DepartmentCount.Index, autopct='%1.1f%%', startangle=90)
plt.title ("Percentage of employees in different departments")
plt.show()

#####################################################

#Q5: Grouped Analysis
# Group by "year" and calculate the average salary for each year
Mean annual salary = df.groupby('year')['total salary'].mean()
print("\nAverage salary by year:\n", average_salary_by_year)

#####################################################

#Q6: Simple Correlation Analysis
# Check the connection between "TotalPay" and "BasePay".
Correlation = df['TotalPay'].corr(df['BasePay'])
print("\nCorrelation between TotalPay and BasePay:", correlation)

# Sparse design
plt.scatter(df['BasePay'], df['TotalPay'])
plt.title('Scatterplot: TotalPay vs. BasePay')
plt.xlabel("BasePay")
plt.ylabel('TotalPay')
plt.show()

#####################################################

#Q8: Summary of Insights
"""
This includes summarizing key insights and observations from the analysis.
You can create a summary based on the results obtained from the above tasks.
You can easily run the provided code snippet in your notebook and adjust it as needed based on the specific details of your dataset.
"""
