# Word Square

## About

A set of python scripts for producing a [word square](https://en.wikipedia.org/wiki/Word_square "Wikipedia page") of arbitrary size from user defined characters and word length. This project uses a word list stored as a [Marisa Trie](https://github.com/pytries/marisa-trie "GitHub page") implemented in C++, allowing fast generation of valid words from a string.

## Usage

### Requirements

This project requires the [Microsoft Visual C++ 14.0 Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017 "Download link"), as well as
[Python3](https://www.python.org/ "Download link"). The Python environment variable should also be set for your OS (i.e. running `python` from the CLI should start Python3).

### Installation & Setup

It is recommended to use a python [virtualenv](https://virtualenv.pypa.io/en/latest/ "Usage guide") to run this program. From a terminal, run `virtualenv venv` from the project root to create a `venv` folder. Follow the instructions on the virtualenv website to activate it for your OS. Then, from the project root run `pip install -r requirements.txt` to install the project requirements.

This program can be used out of the box with the included [word list](http://norvig.com/ngrams/enable1.txt "Enable1 word list") which has already been converted to a Trie file as required. Alternatively run `python build_trie.py` and enter the path to a custom word list. This will generate and save a trie word list in the `word_lists` directory. The path to this word list should then be added in word_square.py in place of the default one.

### Running the Program

From a terminal, cd to the word_square directory and run `python word_square.py n string` where `n` is the integer size of the word square to make (word length/number of words) and `string` is a string of at least n<sup>2</sup> a-z letters (case-insensitive). The program will print a valid word square if one can be found. To run the tests cd to tests and run `python word_square_test.py`.

## Performance

This program finds words from the input string recursively using pruning with each recursive call. Any branches that cannot lead to a word aren't followed, as are any that would lead to a duplicate result (as clearly the input string must have multiple repeat characters for a word square to be possible). Small word squares can generally be found in around 1s on a modern PC, but this time grows exponentially for larger words.
