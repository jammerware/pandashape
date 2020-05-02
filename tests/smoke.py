import os
import pandas as pd
from pandashape import PandaShaper

print('CWD', os.getcwd())
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

shaper = PandaShaper(df_adults)
shaper.report(['1', '2', '3'])
