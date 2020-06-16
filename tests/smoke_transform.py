import os
import pandas as pd
from pandashape import PandaShaper, Columns, Scaling
from pandashape.transformers import CategoricalEncoder, MassScaler

df = pd.read_csv('./tests/assets/dataset.csv')

shaper = PandaShaper(df)
df_txfd = shaper.transform([
    {
        "columns": ['Gender', 'OwnHome', 'Married', 'Location', 'History'],
        "transformers": CategoricalEncoder(label_encoding_breakpoint=4)
    },
    {
        "columns": Columns.Numeric,
        "transformers": MassScaler(scaling=Scaling.Log, skewness_breakpoint=0.4)
    }
])

print(df_txfd)
