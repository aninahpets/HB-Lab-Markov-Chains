import random
from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus_text = open(file_path).read()

    return corpus_text

def make_chains(text_string):
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
    for word in words[:-2]: 
        #Creates bigram
        bigram = (words[i],words[i+1])

        #Creates next_word value
        next_word = words[i + 2]
        i += 1

        #If bigram exists as a key in the dictionary, appends next_word to value list
        if bigram in chains:
            chains[bigram].append(next_word)
        #If bigram is not a key in the dictionary, adds bigram as key and next_word as value
        #And makes the value a list
        else:
            chains[bigram] = []
            chains[bigram].append(next_word)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # We select a starter key aka tuple-bigram
    # Use .choice to randomly select an associate value from the list of next_word(s)
    # Add the key/tupe/bigram with the next word to text
    # Add new_key with second index of current_key and chosen_word
    # Repeat process until new key is not found in dict
    for  
        current_key = random.choice(chains.keys())
        chosen_word = random.choice(chains[current_key])
        text += current_key[0] + " " + current_key[1] + " " + chosen_word
        new_key = (current_key[1], chosen_word)
    print text
#    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
