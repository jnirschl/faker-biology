#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest

from faker import Faker

from faker_biology.cell_biology.cell_line_provider import CellLineProvider

fake = Faker()
fake.add_provider(CellLineProvider)
re_provider = CellLineProvider(None)


class TestCellLineProvider(unittest.TestCase):
    def test_random_cell_line(self):
        for i in range(10):
            fake.cell_line()
