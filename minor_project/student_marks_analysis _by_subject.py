import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode


df = pd.read_csv(r"C:\Users\ncdtg\OneDrive\Desktop\major_project\student_scores.csv")


print("Dataset:\n", df)


print("\n🧹 Checking for missing values:\n", df.isnull().sum())


print("\n✅ Marks within valid range (0-100)?")
valid_marks = df.iloc[:, 1:].applymap(lambda x: 0 <= x <= 100)
print(valid_marks.all())

# Task 2: Descriptive Statistics
print("\n📊 Descriptive Statistics per Subject:")
desc_stats = df.describe().T[['mean', 'std', 'min', 'max']]
desc_stats['median'] = df.median(numeric_only=True)
desc_stats['mode'] = df.mode(numeric_only=True).iloc[0]
desc_stats['variance'] = df.var(numeric_only=True)
print(desc_stats)


subject_avg = df.mean(numeric_only=True)
print("\n🏆 Highest Scoring Subject:", subject_avg.idxmax())
print("📉 Lowest Scoring Subject:", subject_avg.idxmin())


df['Total'] = df.iloc[:, 1:].sum(axis=1)
df['Average'] = df['Total'] / 4

def categorize(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Average"
    else:
        return "Needs Improvement"

df['Performance'] = df['Average'].apply(categorize)
print("\n🧑‍🎓 Student-wise Performance:\n", df[['Student', 'Total', 'Average', 'Performance']])


print("\n🥇 Subject-wise Toppers:")
for subject in ['Maths', 'Science', 'English', 'SST']:
    topper = df[df[subject] == df[subject].max()]['Student'].values
    print(f"{subject}: {', '.join(topper)}")


plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Student', y='Total', palette='viridis')
plt.title("Total Marks per Student")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
subject_avg.plot(marker='o', linestyle='-', color='orange')
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Maths', 'Science', 'English', 'SST']])
plt.title("Boxplot of Subject Marks")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
for subject in ['Maths', 'Science', 'English', 'SST']:
    sns.histplot(df[subject], bins=5, kde=True, label=subject, alpha=0.5)
plt.legend()
plt.title("Histogram - Marks Distribution per Subject")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
