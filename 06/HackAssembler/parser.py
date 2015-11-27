from binary import *
from symbols import *

# intial parse, differentiates between C- and A- instructions
def parser (instruction) :
  if instruction[0] == '@' :
    return parseA(instruction)
  return parseC(instruction)

# parse A-instruction
def parseA (code) :
  address = code[1:]
  if is_number(address) != True :
      address = table_check(address)  # if address is a variable, pull/create entry in table
  return '0' + to_binary(address)

# parse C-instruction
def parseC (code) :
  substr = ''
  destination = ''
  operation = ''
  jump = ''

  for i in range(len(code)) :
    if code[i] == '=' :      # '=' indicates a destination is defined
      destination = substr
      substr = ''
    elif code[i] == ';' :    # '' indicates a jump is defined
      operation = substr
      substr = ''
    else :
      substr += code[i]
  
  if substr != '' :         # what is leftover after the for-loop?
    if operation != '' :        # if operation has been stored, a jump-code must be leftover
      jump = substr
    else :                      # otherwise, store operation (an operation-code always gets defined)
      operation = substr        
  
  return '111' + op_code[operation] + dest_code[destination] + jump_code[jump]    # binary codes stored in objects, in key-value pairs

# check if string char's are all numbers
def is_number (string) :
    try :
        float(string)
        return True
    except ValueError :
        pass

# extract assembly code from list of lines from file
def extract_code (list) :
  result = []
  for i in range(len(list)) :
    line_len = len(list[i])
    if list[i].startswith('/') == False and line_len > 1 and list[i].startswith('(') == False:  # filter out comment-lines and empty ones and labels
      line = ''
      for j in range(line_len) :
        char = list[i][j]
        if char == '/' or char == '\r':  # strip off comments at the end of lines
          break
        elif char != ' ' :               # filter out white-spaces
          line += char
      result.append(line)
    elif list[i].startswith('(') :       # pair label with correct ROM address
      label = list[i][1:(line_len-2)]
      table[label] = len(result)
  return result

