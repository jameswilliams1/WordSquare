#!/usr/bin/env python3
'''
This module defines the WordList class for creating valid English language acrostic word squares from a user entered string and word length. If ran as main, The program will prompt for user
input in the form 'n string' where n is the word length and string is the string of letters to use when generating words. A valid word square is then output if one is possible.
'''
import marisa_trie
import sys
from typing import List
__author__ = 'James Williams'


class WordList():
    '''A class that represents a list of words as a trie and provides word building methods allowing word squares to be formed.'''

    def __init__(self, word_list_filepath: str):
        '''Initialises a WordList from a pre made .marisa dictionary file.
        @param word_list_filepath Path to a .marisa file of words (these can be made using build_trie.py)'''
        self.word_list = marisa_trie.Trie()
        self.word_list.load(word_list_filepath)

    def find_word(self, n: int, string: str, prefix: str = '') -> List[str]:
        '''A generator that finds one word at a time of length n from a string starting with prefix (prefix is optional).
        @param n: The desired length of each word
        @param string: The string to find words from (letters only)
        @param prefix: A prefix each word should start with, all words possible are output if not set
        @return Successive words that are possible matching the input criteria'''
        prefix_length = len(prefix)
        if prefix_length > n:  # Not a possible word
            return
        elif prefix_length == n:  # Yield when word is of required length and is valid
            if self.word_list.get(prefix):
                yield prefix
        else:
            try:  # Skip branches where no words start with prefix
                next(self.word_list.iterkeys(prefix))
            except StopIteration:
                return
            checked_letters = set()
            for i in range(len(string)):
                # Avoids checking the same letter combinations again
                if string[i] in checked_letters:
                    continue
                else:  # Add a letter when prefix (-> output word) is too short
                    checked_letters.add(string[i])
                remain = string[0:i] + string[i + 1:]
                next_prefix = prefix + string[i]
                yield from self.find_word(n, remain, next_prefix)

    def __find_word_square(self, n: int, string: str, word_square: list = [], cycle_count: int = 0, prefix: str = '') -> List[str]:
        '''A generator that finds acrostic word squares of length n from string of at least n^2 characters using English words.
        This method is called internally by find_word_square to avoid default parameters being set.
        @param n The length of each word to make and the size of the word square
        @param string The string of letters used to make words
        @param word_square An empty list that is built up to for a word square (setting this manually may cause unexpected behaviour)
        @param cycle_count The depth of recursion; used to calculate the prefix of the next word (setting this manually may cause unexpected behaviour)
        @param prefix The prefix to be used when finding the next word such that it will lead to a word square (setting this manually may cause unexpected behaviour)'''
        word_generator = self.find_word(n, string, prefix)
        while True:
            try:
                word = next(word_generator)
                next_word_square = word_square.copy()
                next_word_square.append(word)
                if cycle_count == n - 1:
                    yield next_word_square
                    return
                try:
                    for i in range(cycle_count + 1, n): # Check each column prefix has possible words
                        vertical_prefix = [word[i] for word in word_square]
                        next(self.word_list.iterkeys(''.join(vertical_prefix)))
                except StopIteration:
                    continue
                next_string = list(string)
                next_prefix = [next_word_square[i][cycle_count + 1] for i in range(cycle_count + 1)]
                # Remove other letters used in last word (prefix was already removed)
                for used_letter in word[cycle_count:]:
                    next_string.remove(used_letter)
                try:
                    for letter in next_prefix:  # Remove letters needed to make the next prefix
                        next_string.remove(letter)
                except ValueError:  # Required prefix can't be made from remaining letters
                    continue
                yield from self.__find_word_square(n, ''.join(next_string), next_word_square, cycle_count + 1, ''.join(next_prefix))
            except StopIteration:
                return

    def find_word_square(self, n: int, string: str) -> List[str]:
        '''A generator that finds acrostic word squares of length n from string of at least n^2 characters using English words.
        @param n The length of each word to make and the size of the word square
        @param string The string of letters used to make words'''
        yield from self.__find_word_square(n, string)


if __name__ == '__main__':
    word_list = WordList('../word_lists/enable1.marisa')
    try:
        n = sys.argv[1]
        string = sys.argv[2]
        n = int(n)
        string = string.lower()
        word_square_generator = word_list.find_word_square(n, string)
        try:
            word_square = next(word_square_generator)
            for word in word_square:
                print(word)
        except StopIteration:
            print(f'No word square of length {n} could be found from {string}')
    except IndexError:
        print('No input. Input should be of the form "n string" where n is the word length and string is the letters to use to make words (at least n^2 characters).')
    except ValueError:
        print('Invalid input: n must be a positive integer.')
