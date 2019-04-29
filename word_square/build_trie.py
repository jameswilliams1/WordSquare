#!/usr/bin/env python3
"""
Creates a Marisa Trie from a plaintext list of words and saves to word_lists
with the same filename (.marisa extension).
"""

import marisa_trie
from os.path import basename


default_word_list_path = "...word_lists/enable1.txt"
user_word_list_path = ""


def build_trie(word_list_path):
    """
    Returns a filled Marisa Trie object from a word list file.
    @param word_list_path Path to a word list file, one per line
    @return A Trie object containing all words
    """
    with open(word_list_path) as words:
        word_list = [word.strip() for word in words]  # Removes trailing \n
    return marisa_trie.Trie(word_list)


if __name__ == "__main__":
    word_list_path = input("Enter path to plaintext wordlist (one per line):")
    word_list_trie = build_trie(word_list_path)
    # Gets filename without extension
    file_name = basename(word_list_path).split('.')[0]
    word_list_trie.save('../word_lists/%s.marisa' % file_name)
