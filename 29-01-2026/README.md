# Pandas and Matplotlib Practice Tasks

This file contains tasks related to **data analysis using Pandas** and **data visualization using Matplotlib**.  
It covers creating and manipulating DataFrames, handling missing data, calculating statistics, and plotting scatter, line, and bar charts with annotations and labels.

---

## Tasks Overview

### **Task 1: Ad Spend vs Revenue (Scatter Plot)**
- Generate 20 random Ad_Spend values and corresponding Revenue values (Revenue increases with Spend).  
- Create a **scatter plot**.  
- Annotate the "Best Day" (highest revenue).  
- Add a **legend** and grid.  

---

### **Task 2: Client Project Audit (Data Cleaning)**
- Create a DataFrame from the `project_data` dictionary.  
- Remove rows with missing `Client_Name`.  
- Fill missing `Budget` values with the **average budget**.  
- Filter projects with `Budget > 20000`.  

---

### **Task 3: Monthly Ad Spend Analysis (Bar Chart)**
- Aggregate total spend per platform (`Google`, `FB Ads`, `Instagram`).  
- Create a **bar chart**.  
- Use **different colors** for each bar.  
- Add a **Y-axis grid**.  
- Title chart: `"Ad Spend Distribution by Platform"`.  

---

### **Task 4: SEO Stats Analysis (Line Plot + CTR)**
- Create a DataFrame from `seo_stats`.  
- Calculate **CTR (Click-Through Rate)**: `(Clicks / Impressions) * 100`.  
- Sort data by `Date`.  
- Plot **Clicks over time** with markers.  
- Annotate the day with the **highest clicks**.  
- Add grid and labels.  

---

## How to Run

1. Make sure required libraries are installed:
    ```bash
       pip install pandas numpy matplotlib random
2. Run the file:
    ```bash
       python tasks.py
