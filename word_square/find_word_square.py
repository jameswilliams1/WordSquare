import marisa_trie
import sys


class WordList():
    '''A class that represents a list of words as a trie and provides useful string searching methods.'''

    def __init__(self, word_list_filepath):
        self.word_list = marisa_trie.Trie()
        self.word_list.load(word_list_filepath)

    def find_word(self, n: int, string: str, prefix: str = '') -> str:
        '''A generator that finds one word at a time of length n from a string starting with prefix (prefix is optional).
        @param n: The desired length of each word
        @param string: The string to find words from
        @param prefix: A prefix each word should start with, all words possible are output if not setUp
        @return Successive words that are possible matching the input criteria'''
        prefix_length = len(prefix)
        if prefix_length > n: # Not a possible word
            return
        elif  prefix_length == n: # Yield when word is of required length and is valid
            if self.word_list.get(prefix):
                yield prefix
        else:
            try: # Skip branches where prefix has no children
                next(self.word_list.iterkeys(prefix))
            except StopIteration:
                return
            checked_letters = set()
            for i in range(len(string)):
                if string[i] in checked_letters: # Avoids checking the same letter combinations again
                    continue
                else: # Add a letter when prefix (word) is too short
                    checked_letters.add(string[i])
                remain = string[0:i] + string[i + 1:]
                next_word = prefix + string[i]
                yield from self.find_word(n, remain, next_word)

    def find_word_square(self, n: int, string: str, word_square: list = [], cycle_count: int = 0, prefix: str = '') -> list:
        '''Finds a valid word square of length n from string of n^2 characters.'''

        if len(word_square) == n:
            yield word_square
        else:
            word_generator = self.find_word(n, string, prefix)
            while True:
                try:
                    word = next(word_generator)
                    next_word_square = word_square.copy()
                    next_word_square.append(word)
                    if cycle_count == n - 1:
                        yield from self.find_word_square(n, string, next_word_square)
                        return
                    next_prefix = []
                    next_string = list(string)
                    for i in range(cycle_count + 1): # Find next words required prefix from all previous words
                        next_prefix.append(next_word_square[i][cycle_count + 1])
                    for used_letter in word[cycle_count:]: # Remove other letters used in last word (prefix was already removed)
                        next_string.remove(used_letter)
                    try:
                        for letter in next_prefix: # Remove letters needed to make the next prefix
                            next_string.remove(letter)
                    except ValueError: # Prefix can't be made from remaining letters
                        continue
                    yield from self.find_word_square(n, ''.join(next_string), next_word_square, cycle_count + 1, ''.join(next_prefix))
                except StopIteration:
                    return





if __name__ == '__main__':
    word_list = WordList('../word_lists/enable1.marisa')
    gen = word_list.find_word_square(5, 'eeeeddoonnnsssrv')
    for el in gen:
        print(el)
