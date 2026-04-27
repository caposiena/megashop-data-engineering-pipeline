import dask.dataframe as dd

file_path = "data_local/json/*.jsonl"

df = dd.read_json(file_path, lines=True)

print(df.head())