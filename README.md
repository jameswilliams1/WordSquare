# Word Square

## About

A set of python scripts for producing a [word square](https://en.wikipedia.org/wiki/Word_square "Wikipedia page") of arbitrary size from user defined characters and word length. This project uses a word list stored as a [Marisa Trie](https://github.com/pytries/marisa-trie "GitHub page") implemented in C++, allowing fast generation of valid words from a string.

## Usage

### Requirements

This project requires the [Microsoft Visual C++ 14.0 Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017 "Download link"), as well as
[Python3](https://www.python.org/ "Download link").

### Installation & Setup

It is recommended to use a python [virtualenv](https://virtualenv.pypa.io/en/latest/ "Usage guide") to run this program. From a terminal, run `virtualenv venv` from the project root to create a `venv` folder. Follow the instructions on the virtualenv website to activate it for your OS. Then install the project requirements with `pip install -r requirements.txt`.

This program can be used out of the box with the included [word list](http://norvig.com/ngrams/enable1.txt "Enable1 word list") which has already been converted to a Trie file as required. Alternatively run `python build_trie.py` and enter the path to a custom word list. This will generate and save a trie word list in the `word_lists` directory.

### Running the Program

From a terminal run `python word_square.py`. Input must then be of the form `n string_of_letters` where n is the integer size of the word square to make (word length/number of words) and string_of_letters is a string of n<sup>2</sup> a-z letters (case-insensitive). The program will print the first word square that can be found then prompt for more input.

## Performance
This project attempts to find words from the input string recursively.
