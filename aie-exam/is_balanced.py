#!/bin/python3

import argparse

BRACKETS = [('(',')'), ('[',']'), ('{','}')]

def is_balanced(s):
    """
    Checks if a string X starts with `(`,`[`,`{` and ends with the matching
    bracket `)`,`]`,`}`.
    """
    if len(s) <= 2:
        return False
    opening_chars = [ x[0] for x in BRACKETS ]
    if s[0] in opening_chars:
        closing_char = BRACKETS[opening_chars.index(s[0])][1]
        return s[-1] == closing_char
    else:
        return False 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Checks if a string is balanced')
    parser.add_argument('s', metavar='<string>', type=str,
            help='Input string')
    args = parser.parse_args()
    print(is_balanced(args.s))
