import os
import pandas as pd
from pandashape import PandaShaper, Columns, Scaling
from pandashape.transformers import CategoricalEncoder, MassScaler

df_dataset = pd.read_csv('./tests/assets/dataset.csv')

shaper = PandaShaper(df_dataset)
shaper.transform([
    {
        "columns": ['Gender', 'OwnHome', 'Married', 'Location', 'History'],
        "transformers": CategoricalEncoder(label_encoding_breakpoint=4)
    },
    {
        "columns": Columns.Numeric,
        "transformers": MassScaler(scaling=Scaling.Log, skewness_breakpoint=0.4)
    }
])
