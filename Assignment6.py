import pandas as pd
import numpy as np

df = pd.read_excel("array.xlsx")

print("Original Dataset:")
print(df)

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Age"] = pd.to_numeric(df["Age"])
df["Marks"] = pd.to_numeric(df["Marks"])

df = df.drop_duplicates()

print("\nDataset After Preprocessing:")
print(df)

print("\nFinal Dataset Information:")
df.info()

print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())

print("\nDuplicate Records After Preprocessing:")
print(df.duplicated().sum())

df.to_excel("preprocessed_array.xlsx", index=False)

print("\nCleaned Dataset Saved Successfully!")