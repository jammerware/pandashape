import pandas as pd
from src.pandashape.internal import DescriberExecutor
from src.pandashape.describers import CategoricalDescriber


class TestDescriberExecutor():
    def test_skips_describers_with_no_messages(self):
        # arrange
        executor = DescriberExecutor()
        describer = CategoricalDescriber()
        df = pd.DataFrame(data={'column': [0, 1, 2, 3, 4]})

        # TODO: this is a pretty hacky way to assert this, but we'll get there
        describer_header = f"### {describer.get_section_header()} ###"

        # act
        messageLines = executor.describe(df, describer)

        # assert
        assert describer_header not in messageLines
