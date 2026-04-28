import dask.dataframe as dd

file_path = "data_local/json/*.jsonl"

df = dd.read_json(file_path, lines=True)
# Nota: nel dataset generato non è presente la colonna "payment_type".
# Per questo motivo il raggruppamento viene effettuato su "region_id".
media_per_regione = df.groupby("region_id")["amount"].mean()

risultato = media_per_regione.compute()

print("Media importi per regione:")
print(risultato)