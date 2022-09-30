#!/usr/bin/env python3
"""test_cell_line.py in faker_biology/tests.

Created on Sun Feb 13 10:27:03 2022
@author: jnirschl
"""

import unittest

from faker import Faker

from faker_biology.cell_biology.cell_line_provider import CellLineProvider

fake = Faker()
fake.add_provider(CellLineProvider)
re_provider = CellLineProvider(None)


class TestCellLineProvider(unittest.TestCase):
    """Test CellLineProvider class."""

    def test_random_cell_line(self):
        """Test return of random cell line."""
        for _ in range(5):
            fake.cell_line()

    def test_random_human_cell_line(self):
        """Test that cell line returns a valid cell line filtered by species."""
        for _ in range(5):
            fake.cell_line(species="Homo sapiens")

    def test_random_non_human_cell_line(self):
        """Test that cell line returns a valid cell line filtered by species."""
        for _ in range(5):
            fake.cell_line(species="Nonhuman")

    def test_invalid_cell_line(self):
        """Test that ValueError is raised for invalid cell line."""
        invalid_species = [
            "Delphinus delphis",
            "Panaspis breviceps",
            "Tyrannosaurus rex",
        ]
        for elem in invalid_species:
            self.assertRaises(ValueError, fake.cell_line, species=elem)
