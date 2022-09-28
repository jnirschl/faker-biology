#!/usr/bin/env python3
"""cell_line_provider.py in faker_biology/cell_biology.

author: jnirschl
NCI 60 cell line data publicly available from:
https://en.wikipedia.org/wiki/NCI-60
"""

from pathlib import Path

import pandas as pd
from faker.providers import BaseProvider


# TODO re-format class as BioProvider with ability to filter by tumor classification and species
# TODO add non-human cell lines to separate csv file
class CellLineProvider(BaseProvider):
    """
    Provider of fake cell line data.
    """

    def __init__(self, generator):
        super().__init__(generator)

    def cell_line(self) -> str:
        """
        A random cell line used in cell biology research
        Returns
        -------
        str
        """
        data_filepath = Path(__file__).parent.joinpath("nci_60.csv")
        if data_filepath.exists():
            df = pd.read_csv(data_filepath)
            return self.random_element(df["Cell line"].to_list())
        else:
            raise FileNotFoundError(
                f"Could not find cell line data file at {data_filepath}"
            )
