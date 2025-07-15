import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median, mode, stdev, variance


df = pd.read_csv(r"C:\Users\ncdtg\OneDrive\Desktop\major_project\marks.csv")


print("Dataset:\n", df)


marks = df['Marks']


print("\n📊 Statistical Analysis:")
print("Mean:", mean(marks))
print("Median:", median(marks))
print("Mode:", mode(marks))
print("Standard Deviation:", stdev(marks))
print("Variance:", variance(marks))


print("\n📋 Summary (Pandas describe):")
print(df['Marks'].describe())


print("\n🔢 Frequency Count:")
print(df['Marks'].value_counts())


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")


plt.subplot(1, 2, 2)
sns.boxplot(x=marks, color='lightgreen')
plt.title("Marks Distribution - Boxplot")

plt.tight_layout()
plt.show()
