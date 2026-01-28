"""
Task 1: The "Manual" Spreadsheet Create a DataFrame representing 5 employees at Vidya Corporation.Columns: Name, Department, Salary, and Years_of_Experience.The Challenge: Display only the Name and Salary columns and Calculate the average salary of all employees using the .mean() method.
"""
# importing pandas 
import pandas as pd
import numpy as np
data={
    'Name':["Arush","Ansh","Chhavi","Ekam","Varun"],
    'Department':["Software Development","HR","Product Management","Marketing and Support","IT"],
    'Salary':[45000,50000,70000,80000,90000],
    'Years_of_Experience':[1,2,3,4,5]              
}
df=pd.DataFrame(data)
# displaying name and salary column
print(df[["Name","Salary"]])
# Calculating the average salary 
average_sal=df["Salary"].mean()
print(average_sal)

"""
Task 2: Filtering the Workforce (Conditional Selection)Using the same DataFrame from Task 1, write a script to find:All employees with more than 3 years of experience.All employees who work in the "Software Development" department.The Challenge: Increase the salary of everyone in "Software Development" by 10% in the DataFrame.
"""
# finding employees with more than 3 years of experience
employees=df[df["Years_of_Experience"]>3]
print(employees)
# employees with software development department
emp_dep=df[df["Department"]=="Software Development"]
print(emp_dep)
# converting salary datatype to float
df["Salary"] = df["Salary"].astype(np.float64)
# increasing the salary
df.loc[df["Department"]=="Software Development","Salary"]*=1.10
print(df)


"""
Task 3:Create a CSV file (or a dictionary) where some values are missing (use None or np.nan).The Challenge: 1. Use .isnull().sum() to find out which columns have missing data. 2. Fill the missing Salary values with the Median salary of the company. 3. Drop any rows where the Name is missing entirely.
"""

# importing the data
df=pd.read_csv("employee_data.csv")
print(df)
# displaying counts of NaNs per column
print(df.isnull().sum())
# filling the missing value of salary with median
df["Salary"]=df["Salary"].fillna(df["Salary"].median())
print(df)
# dropping the rows where name is missing 
df.dropna(subset=["Name"],inplace=True)
print(df)

"""
Task 4: Real-World SEO Report Analysis
Task: Imagine a CSV with 100 rows of website data: URL, Clicks, Impressions, and CTR (Click-Through Rate).
Challenge:
Use .describe() to get a statistical summary (mean, max, min) of the clicks and impressions.
Sort the DataFrame by Clicks in descending order to find the top-performing page.
Create a new column called Engagement_Score which is Clicks + (Impressions * 0.1).
"""

# importing data from csv file
df=pd.read_csv("website_data.csv")
# statistical summary
print(df.describe())
print(df)
# converting clicks column to int
df["Clicks"] = df["Clicks"].astype(int)
# sorting in descending order 
df.sort_values("Clicks", ascending=False)
# Creating a new column 
df["Engagement_Score"]=df["Clicks"]+(df["Impressions"]*0.1)
print(df)

