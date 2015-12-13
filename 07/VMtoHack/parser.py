line_index = 0
props = {}

def is_command (line) :
  if not line.startswith('/') and len(line) > 1 :
    return True
  return False

def set_current (line) :
  global props
  inst = line.split(' ')
  if len(inst) == 1 :
    props['C_TYPE'] = 'C_ARITHMETIC'
    props['ARG1'] = inst[0].strip()
  else :
    props['ARG1'] = inst[1].strip()
    props['ARG2'] = inst[2].strip()
    if inst[0] == 'push' :
      props['C_TYPE'] = 'C_PUSH'
    else :
      props['C_TYPE'] = 'C_POP'

#######################################
# Only the methods below are exported #
#######################################

def advance (script) :
  global line_index
  line = script[line_index]
  line_index += 1
  if is_command(line) :
    set_current(line)
    return False
  if line_index < len(script) :
    advance(script)
    return False
  return True

def command_type () :
  global props
  return props['C_TYPE']

def arg1 () :
  global props
  return props['ARG1']

def arg2 () :
  global props
  return props['ARG2']


