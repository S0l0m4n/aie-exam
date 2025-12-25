#!/bin/python3

import argparse
import pdb

def longest_unique_substring(s):
    """
    Get the longest unique substring, with no repeated characters in the given
    string, O(n) speed
    """
    current = ""
    best = ""
    last_seen = {}

    for i, ch in enumerate(s):
        if ch in current:
            # repeated char, check if this new substring is longer
            if len(current) > len(best):
                # replace substring
                best = current
                if len(s[i:]) < len(best):
                    # cannot find a longer substring, quit now
                    break
            # start new substring attempt from next char after last seen
            current = s[last_seen[ch]+1 : i+1]
        else:
            # accumulate the substring
            current += ch
        # track last seen
        last_seen[ch] = i
            
    if len(current) > len(best):
        # last accumulated substring is longer
        best = current

    return best

def test_longest_unique_substring():
    assert longest_unique_substring("text") == "tex"
    assert longest_unique_substring("textt") == "tex"
    assert longest_unique_substring("aaaab") == "ab"
    assert longest_unique_substring("aabccbcdef") == "bcdef"
    assert longest_unique_substring("aaaaabcbcdefa") == "bcdefa"
    assert longest_unique_substring("aaaaabcbcdefdd") == "bcdef"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Gets the longest unique substring')
    parser.add_argument('s', metavar='<string>', type=str,
            help='Input string')
    args = parser.parse_args()
    print(longest_unique_substring(args.s))
