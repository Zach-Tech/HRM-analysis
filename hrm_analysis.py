import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

plt.style.use('bmh')
df = pd.read_csv('hrm.csv')

# ---------------------------------------------Gender------------------------------------------------------------

# # Count the occurrences of each unique value in 'EmpSatisfaction'
# emp_sex_counts = df['Sex'].value_counts()


# # (Optional) Sort the counts by index if 'EmpSatisfaction' is numeric
# emp_sex_counts = emp_sex_counts.sort_index()


# # Create a pie chart
# plt.figure(figsize=(8, 8))  # Optional: adjust the size of the plot

# # Plot the pie chart using pandas' plot method
# emp_sex_counts.plot(
#     kind='pie',
#     autopct='%1.1f%%',        # Display percentages with one decimal
#     startangle=140,           # Rotate the start of the pie chart
#     labels=emp_sex_counts.index,  # Use sex levels as labels
#     pctdistance=0.85,         # Position of the percentage labels
#     colors=plt.cm.Paired.colors  # Optional: set a color palette
# )

# # Add a circle at the center to make it a donut chart (optional)
# centre_circle = plt.Circle((0,0),0.70,fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)

# # Set the title
# plt.title('Employee Gender', fontsize=18)

# # Ensure the pie chart is a circle
# plt.axis('equal')  

# # Remove the y-label (optional)
# plt.ylabel('')

# # Show the plot
# plt.show()

# ------------------------------------------------------Race------------------------------------------------------------

# race_counts = df['RaceDesc'].value_counts()


# # Set the plot style (optional)
# plt.style.use('bmh')

# # Create the bar chart
# plt.figure(figsize=(10, 6))  # Optional: Set the size of the plot

# # Plot the bar chart
# race_counts.plot(
#     kind='bar',
#     color='skyblue',
#     edgecolor='black'
# )

# # Add title and labels
# plt.title('Distribution of Race Description', fontsize=18)
# plt.xlabel('Race Description', fontsize=14)
# plt.ylabel('Number of Employees', fontsize=14)

# # Rotate the x labels if needed (optional)
# plt.xticks(rotation=45, ha='right', fontsize=12)

# # Show the plot
# plt.tight_layout()  # Adjust layout to fit everything
# plt.show()

# -----------------------------------------------Performance-------------------------------------------------------

# performance_counts = df['PerformanceScore'].value_counts()

# # Set the plot style (optional)
# plt.style.use('bmh')

# # Create the bar chart
# plt.figure(figsize=(10, 6))  # Optional: Set the size of the plot

# # Plot the bar chart
# performance_counts.plot(
#     kind='bar',
#     color='coral',
#     edgecolor='black'
# )

# # Add title and labels
# plt.title('Distribution of Performance Scores', fontsize=18)
# plt.xlabel('Performance Score', fontsize=14)
# plt.ylabel('Number of Employees', fontsize=14)

# # Rotate the x labels if needed (optional)
# plt.xticks(rotation=0, fontsize=12)

# # Show the plot
# plt.tight_layout()  # Adjust layout to fit everything
# plt.show()


# ------------------------------------------------------Date of Birth-------------------------------

# # Calculate the current age based on DOB
# df['DOB'] = pd.to_datetime(df['DOB'])
# df['Age'] = df['DOB'].apply(lambda x: datetime.now().year - x.year)

# # Define age ranges
# bins = [20, 30, 40, 50, 60, 70]
# labels = ['20-29', '30-39', '40-49', '50-59', '60-69']
# df['AgeRange'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# # Plot a bar chart of age ranges
# age_range_counts = df['AgeRange'].value_counts().sort_index()

# plt.bar(age_range_counts.index, age_range_counts.values)
# plt.xlabel('Age Range', fontsize=14)
# plt.ylabel('Number of Employees', fontsize=14)
# plt.title('Age Distribution of Employees', fontsize=16)
# plt.show()



# -----------------------------------------------Employment Status-----------------------------------
# # Count the occurrences of each employment status
# employment_status_counts = df['EmploymentStatus'].value_counts()

# # Plot a pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(employment_status_counts, labels=employment_status_counts.index, autopct='%1.1f%%', startangle=140)
# plt.title('Employment Status Distribution')
# plt.show()

# ----------------------------------------------Employee Engagement-------------------

# Check the first few rows to understand the data
print(df.head())

# Scatter plot of EngagementSurvey
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['EngagementSurvey'], alpha=0.5, color='blue')
plt.xlabel('Index', fontsize=14)
plt.ylabel('Engagement Survey Score', fontsize=14)
plt.title('Scatter Plot of Engagement Survey Scores', fontsize=16)
plt.grid(True)
plt.show()