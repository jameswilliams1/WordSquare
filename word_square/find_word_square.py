import marisa_trie


class WordList():
    '''A class that represents a list of words as a trie and provides useful string search methods'''

    def __init__(self, word_list_filepath):
        self.word_list = marisa_trie.Trie()
        self.word_list.load(word_list_filepath)

    def find_words(self, string, r=None, prefix=None):
        '''A generator function that finds successive words matching input criteria.
        @param string String to generate words from
        @param r Length of each word to generate
        @param prefix The prefix that each word must start with (does not have to be a single letter)
        @return The next word matching the criteria as a list
        '''
        pool = list(string)
        n = len(pool)
        r = n if r is None else r
        r = r if prefix is None else r - len(prefix)
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        word = [prefix] + list(pool[i] for i in indices[:r])
        if self.word_list.get(str(word), default=False):
            yield word
        print(''.join(word) + ' *')
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    word = [prefix] + list(pool[i] for i in indices[:r])
                    yield word
                    break
            else:
                return


if __name__ == '__main__':
    word_list = WordList('../word_lists/enable1.marisa')
    #gen = [word for word in word_list.find_words(3, 'rakgn', 'c')]
    gen = word_list.find_words('rax', 1, prefix="ca")
    for i in gen:
        print(''.join(i) + " *")
    # word_list.permutations("abc")
