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

from faker_biology.cell_biology import VALID_SPECIES


# TODO re-format class as BioProvider with ability to
#  filter by tumor classification
# TODO add non-human cell lines to separate csv file
class CellLineProvider(BaseProvider):
    """Provider of fake cell line data."""

    def __init__(self, generator):
        """Initialize provider."""
        super().__init__(generator)

    def _human_cell_lines(self, df: pd.DataFrame) -> pd.DataFrame:
        """Returns dataframe of human cell lines."""
        return df[df["Species"] == "Homo sapiens"]

    def _non_human_cell_lines(self, df: pd.DataFrame) -> pd.DataFrame:
        """Returns dataframe of non-human cell lines."""
        return df[df["Species"] != "Homo sapiens"]

    def _get_species(self, df: pd.DataFrame, species: str) -> pd.DataFrame:
        """Returns dataframe of cell lines filtered by species."""
        return df[df["Species"] == species.capitalize()]

    def _load_csv_files(self) -> pd.DataFrame:
        """Load csv files from data directory."""
        data_dir = Path(__file__).parent.resolve()
        csv_file_list = list(data_dir.glob("*.csv"))

        if csv_file_list:
            for csv_file in csv_file_list:
                if not csv_file.exists():
                    raise FileNotFoundError(f"Could not find data file: {csv_file}")

        # read all csv files in csv_file_list and concatenate into one dataframe
        df = pd.concat(
            [
                pd.read_csv(f, usecols=["Cell line", "Species"], index_col=None)
                for f in csv_file_list
            ]
        )
        return df

    def _is_valid_species(self, species: str) -> bool:
        """Check if species is valid."""
        return species in VALID_SPECIES or species is None

    def cell_line(self, species: Optional[str] = None) -> str:
        """Returns random cell line used in cell biology research.

        Args:
            species: optional species name to filter cell lines by.
        """
        if not self._is_valid_species(species) and species != "Nonhuman":
            raise ValueError(f"{species} is not a valid species.")

        # load csv files
        df = self._load_csv_files()

        if species is None:
            result = df["Cell line"].to_list()
        elif species.lower() in ["homo sapiens", "human"]:
            result = self._human_cell_lines(df)["Cell line"].to_list()
        elif species == "Nonhuman":
            result = self._non_human_cell_lines(df)["Cell line"].to_list()
        else:
            result = self._get_species(df, species)["Cell line"].to_list()

        return self.random_element(result)
