import os
import pandas as pd
import tabula

# List all PDFs in the 'data' folder
pdfs = [f"../data/" + f for f in os.listdir("../data") if f.endswith(".pdf")]

all_tables = []

for pdf in pdfs:
    print(f"Reading {pdf} ...")
    tables = tabula.read_pdf(pdf, pages='all', multiple_tables=True)
    all_tables.extend(tables)

# Combine all tables into one CSV
combined = pd.concat([t for t in all_tables if not t.empty], ignore_index=True)
combined.to_csv("../data/uidai_data.csv", index=False)

print("CSV created successfully in data folder!")
