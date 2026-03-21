import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("C:\\Users\\Admin\\Downloads\\TASK 5.xlsx",sheet_name="Dataset")

df["Revenue"]=df["Enrollments"]*df["Price"]

#Total Revenue
print("\nTotalRevenue\n",df["Revenue"].sum())

#Revenue by Course
print("\nRevenue by course\n",df.groupby("Course")["Revenue"].sum().sort_values(ascending=False))

#Revenue by Instructor
print("\nRevenue by Instructor\n",df.groupby("Instructor")["Revenue"].sum().sort_values(ascending=False))

#Revenue by Category
print("\nRevenue by Category\n",df.groupby("Category")["Revenue"].sum().sort_values(ascending=False))

#Visualization
df.groupby("Course")["Revenue"].sum().plot(kind="bar")
plt.title("Revenue by Course")
plt.show()

df.groupby("Category")["Revenue"].sum().plot(kind="pie")
plt.title("Revenue by Category")
plt.show()
