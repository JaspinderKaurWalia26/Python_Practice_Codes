"""
Task: Generate 20 random values for Ad_Spend and 20 corresponding values for Revenue (ensure Revenue generally increases as Spend increases).
The Challenge:
Create a Scatter Plot to show the relationship.
Add a Legend to the chart.
Annotate the "Best Day" (the point with the highest revenue) by pointing an arrow to it using plt.annotate().
"""
import matplotlib.pyplot as plt
import random

#Generating random values
ad_spend=[random.randint(100,1000) for _ in range(20)]
revenue=[spend+random.randint(50,300) for spend in ad_spend]
# Creating Scatter Plot
plt.scatter(ad_spend,revenue,label="Ad Spend vs Revenue")
max_revenue=max(revenue)
best_index=revenue.index(max_revenue)
# annotating the graph
plt.annotate("Best Day",xy=(ad_spend[best_index],revenue[best_index]),xytext=(ad_spend[best_index]+50,revenue[best_index]+50),arrowprops=dict(arrowstyle="->"))
plt.xlabel("Ad_Spend")
plt.ylabel("Revenue")
plt.title("Ad_Spend vs Revenue")
plt.legend()
plt.grid(True)
plt.savefig("ScatterPlot")
plt.show()

"""
TASK 1: THE CLIENT PROJECT AUDIT
Create a DataFrame from the 'project_data' dictionary below.
Find and remove any rows where the 'Client_Name' is missing.
For projects where the 'Budget' is missing, fill it with the AVERAGE budget of the remaining projects.
Filter the list to show only projects with a budget greater than 20,000.

project_data = {
    'Project_ID': [101, 102, 103, 104, 105],
    'Client_Name': ['TechSol', None, 'CloudNine', 'GreenWay', 'Solaris'],
    'Budget': [25000, 15000, None, 30000, 12000],
    'Service': ['Web Dev', 'App Dev', 'SEO', 'Web Dev', 'Graphic Design']
}
"""
import pandas as pd
import numpy as np

project_data = {
    'Project_ID': [101, 102, 103, 104, 105],
    'Client_Name': ['TechSol', None, 'CloudNine', 'GreenWay', 'Solaris'],
    'Budget': [25000, 15000, None, 30000, 12000],
    'Service': ['Web Dev', 'App Dev', 'SEO', 'Web Dev', 'Graphic Design']
}
df=pd.DataFrame(project_data)
print(df)
# removing missing client name
df.dropna(subset=["Client_Name"],inplace=True)
# filling the missing budget value with the average budget 
df["Budget"]=df["Budget"].fillna(df["Budget"].mean())
# filtering the budget 
project_budget=df[df["Budget"]>20000]
print(project_budget)


"""
TASK 2: MONTHLY AD-SPEND ANALYSIS
Create a DataFrame from 'ad_data'.
Group the data by 'Platform' and calculate the TOTAL spend for each.
Create a Bar Chart showing the total spend per platform.
Use a different color for each bar.
Add a grid (Y-axis only).
Title the chart "Ad Spend Distribution by Platform".

ad_data = {
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb'],
    'Platform': ['Google', 'FB Ads', 'Instagram', 'Google', 'FB Ads', 'Instagram'],
    'Spend': [5000, 4000, 2500, 5500, 3800, 2900]
}


"""
ad_data = {
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb'],
    'Platform': ['Google', 'FB Ads', 'Instagram', 'Google', 'FB Ads', 'Instagram'],
    'Spend': [5000, 4000, 2500, 5500, 3800, 2900]
}
df=pd.DataFrame(ad_data)
total_spend=df.groupby('Platform')['Spend'].sum()
print(total_spend)
import matplotlib.pyplot as plt
total_spend.plot(kind="bar")
colors=["Red","Green","Blue"]
plt.title("Ad Spend Distribution by Platform")
plt.xlabel("Platform")
plt.ylabel("Spend")
plt.grid(axis="y")
plt.show()


"""
Create a DataFrame from 'seo_stats'.
Create a new column called 'CTR' (Click-Through Rate).
Formula: CTR = (Clicks / Impressions) * 100
Sort the data by 'Date' to ensure the trend is correct.
Plot a Line Chart of 'Clicks' over time.
Add markers (dots) at each data point.
Bonus Challenge: Use plt.annotate to point an arrow at the day with the highest clicks.

seo_stats = {
    'Date': ['2026-01-05', '2026-01-01', '2026-01-03', '2026-01-02', '2026-01-04'],
    'Clicks': [120, 85, 150, 90, 110],
    'Impressions': [2000, 1500, 2500, 1600, 1900]
}

"""

seo_stats = {
    'Date': ['2026-01-05', '2026-01-01', '2026-01-03', '2026-01-02', '2026-01-04'],
    'Clicks': [120, 85, 150, 90, 110],
    'Impressions': [2000, 1500, 2500, 1600, 1900]
}

df=pd.DataFrame(seo_stats)
print(df)
df['CTR']=(df['Clicks']/df['Impressions'])*100
print(df)
df['Date']=pd.to_datetime(df['Date'])
df=df.sort_values('Date')
print(df)
plt.figure(figsize=(8,5))
plt.plot([df.Date],[df.Clicks],marker="o")
plt.xticks(df['Date'])
max_row=df.loc[df['Clicks'].idxmax()]
plt.annotate(
    "Highest Clicks",
    xy=(max_row['Date'],max_row['Clicks']),
    xytext=(max_row['Date'],max_row['Clicks']+10),
    arrowprops=dict(arrowstyle="->")
)
plt.xlabel('Date')
plt.ylabel('Clicks')
plt.grid(True)
plt.show()
