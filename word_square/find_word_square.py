import marisa_trie
import sys
from collections import Counter


class WordList():
    '''A class that represents a list of words as a trie and provides useful string search methods'''

    def __init__(self, word_list_filepath):
        self.word_list = marisa_trie.Trie()
        self.word_list.load(word_list_filepath)

    def find_word(self, string: str, n: int, prefix: str = '') -> str:
        '''A generator that finds one word at a time of length n from a string starting with prefix (prefix is optional).
        @param string: The string to find words from
        @param n: The desired length of each word
        @param prefix: A prefix each word should start with, all words possible are output if not setUp
        @return Successive words that are possible matching the input criteria'''
        try:  # Skip branches where prefix has no possible items
            next(self.word_list.iterkeys(prefix))
        except StopIteration:
            return
        if len(prefix) >= n:  # Yield when word is of required length and is valid
            if self.word_list.get(prefix):
                yield prefix
        else:  # Add a letter when word is too short
            checked_letters = set()
            for i in range(len(string)):
                if string[i] in checked_letters: # Avoids checking the same letter combinations again
                    continue
                else:
                    checked_letters.add(string[i])
                remain = string[0:i] + string[i + 1:]
                next_word = prefix + string[i]
                yield from self.find_word(remain, n, next_word)


    def find_word_square(self, r, string):
        '''Finds a valid word square of length r from string. '''
        pass


if __name__ == '__main__':
    word_list = WordList('../word_lists/enable1.marisa')
    gen = word_list.find_word('aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy', 9, prefix='')
    for i in gen:
        print(i)
