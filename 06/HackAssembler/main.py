from parser   import parser
from parser   import extract_code

# configure 'python' command
import sys
assembly_code_fn = sys.argv[1]

# read from file inputted into command-line
assembly_code = open(assembly_code_fn, 'r').read()

# convert to a list holding code; no labels, no comments, no white-spaces
assembly_code = extract_code(assembly_code.split('\n'))

code = ''
# translate to binary, line by line
for i in range(len(assembly_code)) :
  line = assembly_code[i]
  binary = parser(line)
  code += binary + '\n'

# write binary translation to '.hack' file in same folder as target
machine_code_fn = assembly_code_fn[0:(len(assembly_code_fn)-3)] + 'hack'
machine_code = open(machine_code_fn, 'w')
machine_code.write(code)
machine_code.close()
