###
Resource: 
https://robertochiosa.medium.com/a-python-guide-to-compress-csv-data-into-parquet-8c797136aa38
###

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

csv_file_path = "/home/teja/Documents/Python/customers-100000.csv"
df = pd.read_csv(csv_file_path)

table = pa.Table.from_pandas(df)

parquet_file_path = "/home/teja/Documents/Python/data-100000.parquet"
pq.write_table(table, parquet_file_path)
