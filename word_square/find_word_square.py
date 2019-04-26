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

        def build_square():
            '''Used internally to add sucessive words to the word_square.'''

            for i in range(1, r):
                print(list(word_square[i]))
                # prefix_present = all(elem in list(current_string) for elem in list(word_square[i]))
                # if not prefix_present: # If required letters to form square not in remaining string
                #     return

                print(letters_available)
                for letter in word_square[i]:
                    letters_available[letter] -= 1
                    if letters_available[letter] < 0:
                        return

                next_word = self.find_words(
                    current_string, r, prefix=word_square[i])
                try:
                    word_square[i] = ''.join(next(next_word))
                except StopIteration:
                    return
                for j in range(i, r - 1):  # Add the next word vertically
                    word_square[j + 1] += word_square[i][j + 1]
                # Remove letters in first_word from string
                for used_letter in word_square[i]:
                    current_string.replace(used_letter, '', 1)
            return word_square

        if not r**2 == len(string):
            return
        pool = list(string)
        # Sort pool by lowest frequency
        count = Counter(pool)
        pool = sorted(pool, key=lambda x: count[x])
        least_occuring = pool.pop(0)
        pool.append(least_occuring)  # Put least occuring letter to back
        last_used_letter = ''
        for first_letter in pool:
            if first_letter == last_used_letter:
                continue
            last_used_letter = first_letter
            new_string = string.replace(first_letter, '', 1)
            first_word_gen = self.find_words(
                new_string, r, prefix=first_letter)
            while True:
                try:
                    print('----------------------')
                    current_string = new_string
                    first_word = next(first_word_gen)
                    current_string_list = list(current_string)
                    # Remove letters in first_word from string
                    for used_letter in first_word[1:]:
                        current_string_list.remove(used_letter)
                    letters_available = Counter(current_string_list)

                    word_square = [''.join(first_word)]
                    try:
                        # Add first_word vertically
                        for letter in word_square[0][1:]:
                            word_square.append(letter)
                            current_string_list.remove(letter)
                    except ValueError:
                        continue
                    current_string = ''.join(current_string_list)
                    print(first_word, current_string)
                    output = build_square()
                    if output:
                        return output
                except StopIteration:
                    break


if __name__ == '__main__':
    word_list = WordList('../word_lists/enable1.marisa')
    gen = word_list.find_word('aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy', 9, prefix='')
    for i in gen:
        print(i)
