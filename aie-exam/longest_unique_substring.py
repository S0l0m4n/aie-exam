#!/bin/python3

import argparse
import pdb

def longest_unique_substring(s):
    """
    Get the longest unique substring, with no unique characters in the given
    string, O(n) speed
    """
    substart = 0
    substring = ''
    i = 1

    while i < len(s):
        if s[i] == s[i-1]:
            # repeated char, check if this new substring is longer
            if len(s[substart:i]) > len(substring):
                # replace substring
                substring = s[substart:i]

            # skip ahead to the next unique character
            for j in range(i+1, len(s)):
                if s[j] == s[i]:
                    # repeated char
                    i += 1
                else:
                    break

            substart = i

            if len(s[i:]) < len(substring):
                # cannot find a longer substring, quit now
                break
        # increment index in all cases
        i += 1

    if len(s[substart:]) > len(substring):
        # last accumulated substring is longer
        substring = s[substart:]

    return substring

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Gets the longest unique substring')
    parser.add_argument('s', metavar='<string>', type=str,
            help='Input string')
    args = parser.parse_args()
    print(longest_unique_substring(args.s))
