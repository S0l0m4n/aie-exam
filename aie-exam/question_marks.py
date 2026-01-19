#!/bin/python3
"""
Have the function QuestionsMarks(str) take the str string parameter, which will
contain single digit numbers, letters, and question marks, and check if there
are exactly 3 question marks between every pair of two numbers that add up to
10. If so, then your program should return the string true, otherwise it should
return the string false. If there aren't any two numbers that add up to 10 in
the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return
true because there are exactly 3 question marks between 6 and 4, and 3 question
marks between 5 and 5 at the end of the string.
"""

from enum import Enum, auto

class State(Enum):
  NO_INT = auto()
  FIRST_INT = auto()
  FAIL = auto()

NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def QuestionMarks(strParam):
  state = State.NO_INT
  ret = False
  sum = 0
  qmcount = 0
  for x in strParam:
    #print(f"{x}: [{state}]", end=' ')
    if state == State.NO_INT:
      if x in NUMBERS:
        sum += int(x)
        state = State.FIRST_INT
    elif state == State.FIRST_INT:
      if x in NUMBERS:
        sum += int(x)
        if sum == 10:
          if qmcount == 3:
            ret = True
            state = State.FIRST_INT
          else:
            ret = False
            state = State.FAIL
        else:
          state = State.NO_INT
        sum = int(x)
        qmcount = 0
      elif x == '?':
        qmcount += 1
    else:
        # FAIL state or invalid state
        ret = False
        break
    #print(f"-> [{state}] ({ret})")
  return ret

assert(QuestionMarks("9???1???9??1???9") == False)
assert(QuestionMarks("5??aaaaaaaaaaaaaaaaaaa?5?5") == False)
assert(QuestionMarks("1?2?7") == False)
