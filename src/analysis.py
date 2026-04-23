import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
data = pd.read_csv("../data/student_data.csv")

print("Dataset:\n", data)

# -------------------------------
# Basic Statistics (Measurements)
# -------------------------------
print("\n--- Basic Statistics ---")
print("Average Marks:", data['Marks'].mean())
print("Max Marks:", data['Marks'].max())
print("Min Marks:", data['Marks'].min())
print("Standard Deviation:", data['Marks'].std())

# -------------------------------
# Correlation (Important Metric)
# -------------------------------
correlation = data['Attendance'].corr(data['Marks'])
print("\nCorrelation (Attendance vs Marks):", correlation)

# -------------------------------
# Categorization
# -------------------------------
def categorize(marks):
    if marks >= 75:
        return "High"
    elif marks >= 50:
        return "Average"
    else:
        return "Low"

data['Performance'] = data['Marks'].apply(categorize)

print("\n--- Performance Categories ---")
print(data[['StudentID', 'Marks', 'Performance']])

# -------------------------------
# Weak Students
# -------------------------------
weak = data[data['Marks'] < 50]
print("\nWeak Students:\n", weak)

# -------------------------------
# Graph 1: Scatter Plot
# -------------------------------
plt.scatter(data['Attendance'], data['Marks'])
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.savefig("../results/attendance_vs_marks.png")
plt.show()

# -------------------------------
# Graph 2: Line Plot
# -------------------------------
plt.plot(data['StudyHours'], data['Marks'])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.savefig("../results/studyhours_vs_marks.png")
plt.show()

# -------------------------------
# Graph 3: Bar Chart
# -------------------------------
performance_counts = data['Performance'].value_counts()

performance_counts.plot(kind='bar')
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.title("Student Performance Distribution")
plt.savefig("../results/performance_distribution.png")
plt.show()

# -------------------------------
# Additional Metrics
# -------------------------------
print("\n--- Additional Metrics ---")
print("Total Students:", len(data))
print("High Performers:", len(data[data['Performance'] == 'High']))
print("Average Performers:", len(data[data['Performance'] == 'Average']))
print("Low Performers:", len(data[data['Performance'] == 'Low']))