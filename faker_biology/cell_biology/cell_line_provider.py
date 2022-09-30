#!/usr/bin/env python3
"""cell_line_provider.py in faker_biology/cell_biology.

@author: jnirschl
NCI 60 cell line data publicly available from:
https://en.wikipedia.org/wiki/NCI-60
"""

from pathlib import Path
from typing import Optional

import pandas as pd
from faker.providers import BaseProvider


# TODO re-format class as BioProvider with ability to
#  filter by tumor classification and species
# TODO add non-human cell lines to separate csv file
class CellLineProvider(BaseProvider):
    """Provider of fake cell line data."""

    def __init__(self, generator):
        """Initialize provider."""
        super().__init__(generator)

    def cell_line(self, species: Optional[str] = None) -> str:
        """Returns random cell line used in cell biology research.

        Args:
            species: optional species name to filter cell lines by.
        """
        valid_species = ["Homo sapiens"]  # "Mus musculus", "Rattus norvegicus"
        if species is not None and species not in valid_species:
            raise ValueError(
                "Species not available " f"{species} in list {valid_species}"
            )

        data_filepath = Path(__file__).parent.joinpath("nci_60.csv")
        if data_filepath.exists():
            df = pd.read_csv(data_filepath)
            if species:
                df = df[df["Species"] == species.capitalize()]
            else:
                df = df

            return self.random_element(df["Cell line"].to_list())
        else:
            raise FileNotFoundError(
                f"Could not find cell line data file at {data_filepath}"
            )
