#!/bin/python3

import argparse
import string

def get_k_most_tokens(text, k):
    """
    Returns the k most common tokens in the given text, as a list in the form
    [(token1, n1), (token2, n2), ..., (tokenk, nk)]
    where   token1 is the most common token, n1 is its count
            token2 is the second most common, with n2 as its count
            etc.
    """
    tokens = count_tokens(text)

    # create a list of (count, token) pairs
    tokens_list = [ (tokens[x], x) for x in tokens ]

    # reverse sort the list (largest count first)
    tokens_list.sort()
    tokens_list.reverse()

    # return the first k elements
    return tokens_list[0:k]

def count_tokens(text):
    """
    Counts all the tokens in the given text, ignoring punctuation and newlines
    """
    # translation table for ignoring punctuation
    T = str.maketrans({ x: None for x in string.punctuation })

    # split the text into words (newlines get removed here)
    words = text.split()

    # now count the tokens and store the results in a dict
    tokens = {}
    for x in words:
        word = x.translate(T)
        if word == '':
            # this "word" was just punctuation, continue with the next one
            continue
        for key in tokens.keys():
            if word.lower() == key.lower():
                # token previously found, increment its count
                tokens[key] += 1
                break
        else:
            # first time we encounter the token
            tokens[word] = 1

    return tokens

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Gets the k most common tokens in the given text \
                    string or file')
    parser.add_argument('text', metavar='<file|string>', type=str,
            help='Input text file or string')
    parser.add_argument('-k', metavar='<k>', type=int, required=True,
            help='Number of tokens to return (most common)')
    args = parser.parse_args()

    try:
        # assume a file is given
        with open(args.text, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        # interpret the arg as a simple string
        text = args.text

    print(get_k_most_tokens(text, args.k))
