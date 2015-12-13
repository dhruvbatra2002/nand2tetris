from parser import command_type, arg1, arg2, advance

f = False
set_true_count = 0
continue_count = 0

def set_file_name (string) :
  file_name = string[0:(len(string)-2)] + 'asm'
  global f
  f = open(file_name, 'w')

def close () :
  global f
  f.close()

def write_arithmetic () :
  command = arg1()
  # (if command operates on single value)
  if command == 'not' or command == 'neg' : 
    f.write('@SP' + '\n')
    f.write('A=M' + '\n')
    if command =='not' :
      f.write('M=!M' + '\n')
    else :
      f.write('M=-M' + '\n')

  else : # (if command operates on two values)
    f.write('@SP' + '\n')
    f.write('M=M-1' + '\n')
    f.write('A=M+1' + '\n')
    f.write('D=M' + '\n')
    f.write('A=A-1' + '\n')

    if command == 'add' :
      f.write('M=M+D' + '\n')
    elif command == 'sub' :
      f.write('M=M-D' + '\n')
    elif command == 'and' :
      f.write('M=M&D' + '\n')
    elif command == 'or' :
      f.write('M=M|D' + '\n')

    else : # (if operation is comparative)
      f.write('D=M-D' + '\n')
      global set_true_count, continue_count
      f.write('@SET_TRUE.' + str(set_true_count) + '\n')
      if command == 'eq' :
        f.write('D;JEQ' + '\n')
      if command == 'gt' :
        f.write('D;JGT' + '\n')
      if command == 'lt' :
        f.write('D;JLT' + '\n')
      f.write('@SP' + '\n')
      f.write('A=M' + '\n')
      f.write('M=0' + '\n')
      f.write('@CONTINUE.' + str(continue_count) + '\n')
      f.write('0;JMP' + '\n')
      f.write('(SET_TRUE.' + str(set_true_count) + ')' + '\n')
      f.write('@SP' + '\n')
      f.write('A=M' + '\n')
      f.write('M=1' + '\n')
      f.write('(CONTINUE.' + str(continue_count) + ')' + '\n')
      set_true_count += 1
      continue_count += 1

def write_push_pop () :
  base = arg1()
  if base == 'static' :
    f.write('@16' + '\n')
    f.write('D=A' + '\n')
  elif base == 'local' :
    f.write('@LCL' + '\n')
    f.write('D=M' + '\n')
  elif base == 'argument' :
    f.write('@ARG' + '\n')
    f.write('D=M' + '\n')
  elif base == 'this' :
    f.write('@THIS' + '\n')
    f.write('D=M' + '\n')
  elif base == 'that' :
    f.write('@THAT' + '\n')
    f.write('D=M' + '\n')
  elif base == 'constant' :
    f.write('@SP' + '\n')
    f.write('D=A' + '\n')
  elif base == 'temp' :
    f.write('@5' + '\n')
    f.write('D=A' + '\n')
  f.write('@R13' + '\n')
  f.write('M=D' + '\n')

  index = arg2()
  f.write('@' + index + '\n')
  f.write('D=A' + '\n')
  f.write('@R13' + '\n')
  f.write('M=M+D' + '\n')

  command = command_type()
  if command == 'C_PUSH' :
    f.write('D=M' + '\n')
    if base != 'constant' :
      f.write('A=D' + '\n')
      f.write('D=M' + '\n')
    f.write('@SP' + '\n')
    f.write('M=M+1' + '\n')
    f.write('A=M-1' + '\n')
    f.write('M=D' + '\n')
  else : # (if command == 'C_POP')
    f.write('@SP' + '\n')
    f.write('M=M-1' + '\n')
    f.write('A=M+1' + '\n')
    f.write('D=M' + '\n')
    f.write('@R13' + '\n')
    f.write('A=M' + '\n')
    f.write('M=D' + '\n')
