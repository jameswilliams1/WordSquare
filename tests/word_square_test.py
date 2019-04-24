"""
Tests for word_square.py
"""
import sys
import unittest
sys.path.append('../word_square')
from find_word_square import *
import marisa_trie


class WordSquareTest(unittest.TestCase):
    def setUp(self):
        self.word_list = WordList('../word_lists/enable1.marisa')

    def test_find_words_possible_answers(self):
        word_generator = self.word_list.find_words('nabraa', 3, 'c')
        found_words = [''.join(word) for word in word_generator]
        possible_words = ['cab', 'can', 'car']
        possible_words.sort()
        found_words.sort()
        self.assertEqual(possible_words, found_words)

    def test_find_words_no_possible_answers(self):
        word_generator = self.word_list.find_words('vwj', 2, 'x')
        with self.assertRaises(StopIteration):
            next(word_generator)

    def test_find_words_r_is_1(self):
        word_generator = self.word_list.find_words('vwb', 1, 'a')
        with self.assertRaises(StopIteration):
            next(word_generator)

    def test_find_words_r_greater_than_n(self):
        word_generator = self.word_list.find_words('ds', 5, 'en')
        with self.assertRaises(StopIteration):
            next(word_generator)



if __name__ == "__main__":
    unittest.main()
