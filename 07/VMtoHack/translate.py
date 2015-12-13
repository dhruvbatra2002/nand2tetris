from code_writer import set_file_name, write_arithmetic, write_push_pop, close
from parser import command_type, arg1, arg2, advance


import sys
vm_fn = sys.argv[1]

vm_code = open(vm_fn, 'r').read().split('\n')
set_file_name(vm_fn)

complete = advance(vm_code)

while not complete :
  C_type = command_type()
  if C_type == 'C_ARITHMETIC' :
    write_arithmetic()
  elif C_type == 'C_PUSH' or C_type == 'C_POP' :
    write_push_pop()
  complete = advance(vm_code)

close() 
