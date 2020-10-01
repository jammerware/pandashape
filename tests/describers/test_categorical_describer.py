import pandas as pd
from src.pandashape.describers import CategoricalDescriber


class TestCategoricalDescriber():
    def test_ignores_numeric_columns(self):
        # arrange
        df = pd.DataFrame(columns=['column'], data=[0, 1, 2, 3, 4], )
        describer = CategoricalDescriber()

        # act
        result = describer.describe(df)

        # assert
        assert len(result) == 0

    def test_reports_string_column(self):
        # arrange
        df = pd.DataFrame(data={'gender': ['gnb', 'male', 'female', 'fluid', 'transgender', 'no response']})
        describer = CategoricalDescriber()

        # act
        result = describer.describe(df)

        # assert
        assert len(result) > 0
