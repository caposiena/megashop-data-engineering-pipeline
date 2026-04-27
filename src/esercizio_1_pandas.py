import pandas as pd
import os
folder_path = "data_local/json"
total_amount = 0
for filename in os.listdir(folder_path):
    if filename.endswith(".jsonl"):
        file_path = os.path.join(folder_path, filename)

        df = pd.read_json(file_path, lines=True)

        file_total = df["amount"].sum()
        total_amount += file_total

        print(f"File letto: {filename} - Totale amount: {file_total}")
print("\nTotale complessivo delle vendite:", total_amount)