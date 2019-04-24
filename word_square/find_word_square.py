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
        def find_word():
            '''Used internally to produce a single word.'''
            word = [prefix]
            loop_finished = True  # Assume loop will run till end
            for i in indices[:r]:
                word.append(pool[i])
                word_as_string = ''.join(word)
                if not self.word_list.has_keys_with_prefix(word_as_string) and not self.word_list.get(word_as_string):
                    loop_finished = False
                    break
            if loop_finished and self.word_list.get(''.join(word)):
                return word
        pool = list(string)
        n = len(pool)
        r = n if r is None else r
        r = r if prefix is None else r - len(prefix)
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        word = find_word()
        if word:
            yield word
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    word = find_word()
                    if word:
                        yield word
                    break
            else:
                return


if __name__ == '__main__':
    word_list = WordList('../word_lists/enable1.marisa')
    gen = word_list.find_words('rax', 3, prefix="c")
    for i in gen:
        print(''.join(i))
        # print(i)
    # word_list.permutations("abc")
