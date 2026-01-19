#!/bin/python3

def QuestionMarks(strParam):
    ret = False
    sum = 0
    qmcount = 0
    for x in strParam:
        if x.isdigit():
            sum += int(x)
            if (sum == 10):
                if (qmcount == 3):
                    ret = True
                else:
                    ret = False
                    break
            # reset
            sum = int(x)
            qmcount = 0
        elif x == '?':
            qmcount += 1
    return ret

assert(QuestionMarks("dd6?9") == False)
assert(QuestionMarks("dd6???4?9") == True)
assert(QuestionMarks("9???1???9??1???9") == False)
assert(QuestionMarks("5??aaaaaaaaaaaaaaaaaaa?5?5") == False)
assert(QuestionMarks("1?2?7") == False)
