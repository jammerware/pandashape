from .GenericTransformer import GenericTransformer
from pandashape.enums.Scaling import Scaling


class MassScaler(GenericTransformer):
    def __init__(self, scaling=Scaling.MinMax, skewness_breakpoint=None):
        self.scaling = scaling
        self.skewness_breakpoint = skewness_breakpoint

    def transform(self, df):
        # this feels unnecessarily ugly
        for column in df.iteritems():
            print("column", column[0])
            if (self.skewness_breakpoint is not None):
                print("skewness breakpoint", self.skewness_breakpoint)
                skewness = column[1].skew()
                if (self.skewness_breakpoint is not None and skewness < self.skewness_breakpoint):
                    print("skewness too low for", column[0])
                    pass

        return df
