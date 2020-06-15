import pandas as pd


class Describer:
    def __init__(self, df):
        self.df = df

    def describe(self):
        raise NotImplementedError()

    def get_section_header(self):
        raise NotImplementedError()