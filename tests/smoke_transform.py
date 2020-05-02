import os
import pandas as pd
from pandashape import PandaShaper, Columns
from pandashape.transformers import MassLabelEncoder

df_adults = pd.read_csv('./tests/assets/adult_data.txt', sep=",", header=None)
df_adults.columns = [
    "Age",
    "WorkClass",
    "fnlwgt",
    "Education",
    "EducationNum",
    "MaritalStatus",
    "Occupation",
    "Relationship",
    "Race",
    "Gender",
    "CapitalGain",
    "CapitalLoss",
    "HoursPerWeek",
    "NativeCountry",
    "Income"
]

# shaper = PandaShaper(df_adults)
# shaper.transform({
#     "columns": 'Education',
#     "transformers": MassLabelEncoder(label_encoding_breakpoint=5)
# })

df_dataset = pd.read_csv('./tests/assets/dataset.csv')
df_dataset.head()
