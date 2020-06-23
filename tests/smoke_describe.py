import pandas as pd
from pandashape import PandaShaper
from pandashape.describers import GeneralDescriber, DistributionDescriber, DTypesDescriber, CorrelationDescriber

df = pd.read_csv('./tests/assets/dataset.csv')
df['AmountSpent_HighCorrelation'] = df['AmountSpent']
df['Salary_HighCorr'] = df['Salary']

shaper = PandaShaper(df)
shaper.describe([GeneralDescriber, DTypesDescriber, DistributionDescriber, CorrelationDescriber])
