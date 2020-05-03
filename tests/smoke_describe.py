import pandas as pd
from pandashape import PandaShaper
df = pd.read_csv('./tests/assets/dataset.csv')

shaper = PandaShaper(df)
shaper.describe()
