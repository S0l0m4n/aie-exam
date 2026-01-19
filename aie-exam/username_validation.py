#!/bin/python3

import string

def CodelandUsernameValidation(strParam):
  if not (4 <= len(strParam) <= 25):
    return False

  if not strParam[0].isalpha():
    return False
  
  if strParam[-1] == '_':
    return False
  
  if not all(i.isalnum() or i == '_' for i in strParam):
      return False
  
  return True

assert(CodelandUsernameValidation("aa_") == False)
assert(CodelandUsernameValidation("user__land32_aa") == True)
