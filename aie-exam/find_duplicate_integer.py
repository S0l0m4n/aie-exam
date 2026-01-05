#!/bin/python3

import argparse
import ast
import pdb

def find_duplicate_integer(integers):
    """
    Given a list of n+1 integers from 1 to n. One of the integers will be
    duplicated; this is what is returned. If the list is invalid, -1 is
    returned.
    ---
    Method: A list of integers from 1 to n adds up to N = n*(n+1)/2. If it adds
    up to S = N + x, then the duplicate number is x = S - N. Confirm by ensuring
    that x is found twice in the list.
    """
    S = sum(integers)
    n = len(integers) - 1
    N = n*(n+1)//2      # do integer division (Python 3)
    x = int(S - N)
    
    try:
        assert integers.count(x) == 2
        return int(x)
    except AssertionError:
        return -1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            usage="Example: %(prog)s '[1,2,3,3]'",
            description='Returns the duplicate integer in the list')
    parser.add_argument('integers', metavar='[integers]', type=str,
            help='List of n+1 integers 1 to n containing a duplicate')
    args = parser.parse_args()
    integers = ast.literal_eval(args.integers)
    duplicate = find_duplicate_integer(integers)
    print(duplicate)
