import pandas as pd


class PandaShaper:
    def __init__(self, df, inplace=False):
        assert(isinstance(df, pd.DataFrame))

        # why does this cause an evaluation of the truth of df?
        # self.df = df if inplace else df.copy(df)
        self.df = df
        if inplace:
            self.df = df.copy()

    def report(self, columnDefinitions):
        print(f"Reporting on {columnDefinitions}")
        # df_adults.columns[df_adults.isna().any()]
