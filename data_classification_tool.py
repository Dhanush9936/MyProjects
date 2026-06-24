import pandas as pd

df = pd.read_csv("students.csv")

df = df.dropna()

def grade(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Poor"

df["Grade"] = df["Marks"].apply(grade)

print(df.head())

print("\nGrade Distribution:")
print(df["Grade"].value_counts())

df.to_csv("labeled_students.csv", index=False)
