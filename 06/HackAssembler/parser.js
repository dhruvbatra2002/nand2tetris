// intial parse, differentiates between C- and A- instructions
var parser = function (instruction) {

  if (instruction[0] === '@') {
    return parseA(instruction);
  }

  return parseC(instruction);
};

// parse A-instruction
var parseA = function (code) {

  var address = code.slice(1);

  if (isNaN(address)) address = tableCheck(address);  // if address is a variable, pull/create entry in table

  return '0' + toBinary(address);
};

// parse C-instruction
var parseC = function (code) {

  var substr = '';
  var destination = '';
  var operation = '';
  var jump = '';

  for (var i = 0; i < code.length; i++) {

    if (code[i] === '=') {          // '=' indicates a destination is defined

      destination = substr;
      substr = '';
    }

    else if (code[i] === ';') {     // ';' indicates a jump is defined

      operation = substr;
      substr = '';
    }

    else substr += code[i];
  }

  if (substr) {                     // what is leftover after the for-loop?

    if (operation) jump = substr;   // if operation has been stored, a jump-code must be leftover
    else operation = substr;        // otherwise, store operation (an operation-code always gets defined)
  }

  return '111' + opCode[operation] + destCode[destination] + jumpCode[jump];    // binary codes stored in objects, in key-value pairs
};