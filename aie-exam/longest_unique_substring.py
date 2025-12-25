#!/bin/python3

import argparse
import pdb

def longest_unique_substring(s):
    """
    Get the longest unique substring, with no repeated characters in the given
    string, O(n) speed
    """
    start = 0
    best_start = 0
    best_len = 0
    last_seen = {}

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            # start new substring attempt from next char after last seen
            # ignore chars seen before start
            start = last_seen[ch] + 1

        # update window and last seen
        window_len = i - start + 1
        last_seen[ch] = i

        # update best
        if window_len > best_len:
                best_len = window_len
                best_start = start

    # return the best window
    return s[best_start:best_start + best_len]

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
