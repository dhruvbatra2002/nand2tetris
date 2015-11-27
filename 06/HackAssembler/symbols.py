# index where non-allocated registers begin in 'table'
place = 16

# pre-allocated registers in RAM
table = {
  'R0'  : '0',
  'R1'  : '1',
  'R2'  : '2',
  'R3'  : '3',
  'R4'  : '4',
  'R5'  : '5',
  'R6'  : '6',
  'R7'  : '7',
  'R8'  : '8',
  'R9'  : '9',
  'R10' : '10',
  'R11' : '11',
  'R12' : '12',
  'R13' : '13',
  'R14' : '14',
  'R15' : '15',
  'SCREEN' : '16384',
  'KBD' : '24576',
  'SP'  : '0',
  'LCL' : '1',
  'ARG' : '2',
  'THIS': '3',
  'THAT': '4' 
}

# returns numerical address of register associates with symbol;
# (and allocates one if necessary)
def table_check (symbol) :
  if symbol in table.keys() :
    return table[symbol] 
  else :                  # if not associated with a register, assign symbol to first unused one
    global place
    table[symbol] = place
    place += 1
    return place - 1

