import sys
import random
from random import choice

file_path = sys.argv[1]

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus_text = open(file_path).read()

    return corpus_text

def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    #Creates empty dictionary
    chains = {}

    #Splits the string by empty spaces
    words = text_string.split()

    i = 0

    #While the index i is less than the -nth (aka last tuple possible)
    #Loop over the list words and create tuples

    while i < (len(words) - n):
        #Creates ngram
        ngram = []

        # loops n number of times to create tuples and next_word list
        for j in range(i, i + n):
            ngram.append(words[j])
            # sets next_word equal to the next word after the new ngram tuple
            next_word = words[words.index(ngram[-1]) + 1]
            i += 1

        ngram = tuple(ngram)
            
        #If ngram exists as a key in the dictionary, appends next_word to value list
        #Creates next_word value
        if ngram in chains:
            chains[ngram].append(next_word)
        #If ngram is not a key in the dictionary, adds ngram as key and next_word as value
        #And makes the value a list
        else:
            chains[ngram] = []
            chains[ngram].append(next_word)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""



    # Add the key/tupe/ngram with the next word to text
    # Add new_key with second index of current_key and chosen_word
    # Repeat process until new key is not found in dict

    # Use .choice to randomly select a starter key aka tuple-ngram
    current_key = random.choice(chains.keys())
    # Use .choice to randomly select an associated value from the list of next_word(s)
    chosen_word = random.choice(chains[current_key])
    text += current_key[0] + " " + current_key[1] + " " + chosen_word + " "
    while True:
        chosen_word = random.choice(chains[current_key])
        text += chosen_word + " "
        new_key = (current_key[1], chosen_word)
        current_key = new_key
        if new_key not in chains:
            break

    return text
#    return text


# input_path = "green-eggs.txt"

# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text,4)

# Produce random text
random_text = make_text(chains)

print random_text
