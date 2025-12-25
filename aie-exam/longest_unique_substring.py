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

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            # repeated char, check if this new substring is longer
            if len(s[substart:i]) > len(substring):
                # replace substring
                substring = s[substart:i]

            substart = i

            if len(s[i:]) < len(substring):
                # cannot find a longer substring, quit now
                break

    if len(s[substart:]) > len(substring):
        # last accumulated substring is longer
        substring = s[substart:]

    return substring

def test_longest_unique_substring():
    assert longest_unique_substring("text") == "text"
    assert longest_unique_substring("textt") == "text"
    assert longest_unique_substring("aaaab") == "ab"
    assert longest_unique_substring("aabccbcdef") == "cbcdef"
    assert longest_unique_substring("aaaaabcbcdef") == "abcbcdef"
    assert longest_unique_substring("aaaaabcbcdefdd") == "abcbcdefd"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Gets the longest unique substring')
    parser.add_argument('s', metavar='<string>', type=str,
            help='Input string')
    args = parser.parse_args()
    print(longest_unique_substring(args.s))
