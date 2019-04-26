"""
Tests for word_square.py
"""
import sys
import unittest
sys.path.append('../word_square')
from find_word_square import *
import marisa_trie
#import numpy as np


class WordSquareTest(unittest.TestCase):
    def setUp(self):
        self.word_list = WordList('../word_lists/enable1.marisa')

    def test_find_word_possible_answers(self):
        word_generator = self.word_list.find_word('nabraa', 3, 'c')
        found_words = [''.join(word) for word in word_generator]
        possible_words = ['cab', 'can', 'car']
        possible_words.sort()
        found_words.sort()
        self.assertEqual(possible_words, found_words)

    def test_find_word_no_possible_answers(self):
        word_generator = self.word_list.find_word('vwj', 2, 'x')
        with self.assertRaises(StopIteration):
            next(word_generator)

    def test_find_word_r_is_1(self):
        # Cannot find word of length 1 when combining 2 strings
        word_generator = self.word_list.find_word('vwb', 1, 'a')
        with self.assertRaises(StopIteration):
            next(word_generator)

    def test_find_word_r_greater_than_n(self):
        # Desired word length > input string
        word_generator = self.word_list.find_word('ds', 5, 'en')
        with self.assertRaises(StopIteration):
            next(word_generator)

    def test_find_word_r_is_1_no_prefix(self):
        word_generator = self.word_list.find_word('acr', 3)
        found_words = [''.join(word) for word in word_generator]
        possible_words = ['arc', 'car']
        possible_words.sort()
        found_words.sort()
        self.assertEqual(possible_words, found_words)

    def test_find_word_square_possible_answers(self):
        pass





if __name__ == "__main__":
    unittest.main()
