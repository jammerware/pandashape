import os
import pandas as pd
from pandashape import PandaShaper, Columns, Scaling
from pandashape.internal import ColumnResolver
from pandashape.transformers import CategoricalEncoder, MassScaler

resolver = ColumnResolver()
df = pd.read_csv('./tests/assets/dataset.csv')

result = resolver.resolve('Gender', df)
shaper = PandaShaper(df)

print(result)
