import pandas as pd

# Read CSV file
df = pd.read_csv("data/sample_uidai.csv")
print("UIDAI Data")
print(df)

# Find suspicious/fake Aadhaar records
print("\nSuspicious Records:")
print(df[df["Age"] > 100])
