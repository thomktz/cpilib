import pandas as pd

from cpilib.cpi.base_classes import CPICountries
from cpilib.utils import get_eurostat_dataset


class HICP(CPICountries):
    """CPI class for the Harmonized Index of Consumer Prices (HICP)."""

    def __init__(self):
        prices = get_eurostat_dataset("prc_hicp_midx")
        prices.index = pd.to_datetime(prices.index, format="%YM%m")
        prices = prices["I15"].swaplevel(0, 1, axis=1).sort_index(axis=1).sort_index(axis=0)

        item_weights = get_eurostat_dataset("prc_hicp_inw")
        item_weights.index = pd.to_datetime(item_weights.index)
        item_weights = item_weights.swaplevel(0, 1, axis=1).sort_index(axis=1).sort_index(axis=0)

        country_weights = get_eurostat_dataset("prc_hicp_cow")
        country_weights.index = pd.to_datetime(country_weights.index)
        country_weights = country_weights["COWEA19"].sort_index(axis=0)

        super().__init__(prices, item_weights, country_weights, 2015)
