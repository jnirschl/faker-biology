#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.mol_biol import RestrictionEnzyme


fake = Faker()
fake.add_provider(RestrictionEnzyme)
re_provider = RestrictionEnzyme(None)


class ReTest(unittest.TestCase):
    def test_random_re(self):
        res = [fake.unique.restriction_enzyme() for _ in range(100)]
        self.assertEqual(100, len(res))
        self.assertTrue(all(isinstance(re, str) for re in res))

    def test_random_redata(self):
        res = [fake.restriction_enzyme_data() for _ in range(100)]
        self.assertTrue(all(isinstance(re, dict) for re in res))

    def test_min_size(self):
        res = [fake.restriction_enzyme(8) for _ in range(20)]
        self.assertTrue(all(isinstance(re, str) for re in res))

    def test_blunt(self):
        res = [fake.unique.blunt() for _ in range(50)]
        self.assertTrue(all(isinstance(re, str) for re in res))
