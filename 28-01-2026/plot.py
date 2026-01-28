# Task 1: Service Comparison (Bar Chart)The Task: Create a dictionary of 4 services and their respective "Project Counts" for the month.The Challenge: Create a Bar Chart showing which service had the most projects. Use a different color for each bar. 3. Add a Grid to the background, but only for the Y-axis, to make the values easier to read.
import matplotlib.pyplot as plt

services={
    "Cyber Security":30,
    "App Development":25,
    "SEO":20,
    "UI/UX Design":15 
}
plt.bar(
    services.keys(),
    services.values()
)
plt.grid(axis="y")
plt.show()

# Task 2: The "Traffic Growth" Line PlotThe Task: Create two lists (or NumPy arrays): days (1 to 7) and visitors (representing daily website hits).The Challenge: Plot a line graph showing the traffic over the week.Add a Title ("Weekly Website Traffic"), X-label ("Day"), and Y-label ("Number of Visitors"). Change the line color to green, make it dashed, and add markers (dots) at each data point.

l1=[1,2,3,4,5,6,7]
l2=[20,30,40,50,25,15,35]
plt.plot(l1,l2,color="green",marker="o",linestyle="--")
plt.title("Weekly Website Traffic")
plt.xlabel("Day")
plt.ylabel("Number of Visitors")
plt.show()