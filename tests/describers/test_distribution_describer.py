import pandas as pd
from src.pandashape.describers import DistributionDescriber


class TestDistributionDescriber():
    def test_skew_skips_binary_cols(self):
        # arrange
        df_test = pd.DataFrame({
            'binary_col': [0, 1, 0, 0, 1],
        })

        # act
        describer = DistributionDescriber()
        result = describer.describe(df_test)

        # assert
        assert len(result) == 0
