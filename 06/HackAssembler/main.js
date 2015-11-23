// main function, called on button click
var assemble = function () {

  var code = document.getElementById('input').value + ' ';    // grab assembly code input
  
  assemblyCode = reformatCode(code);                          // converts to array, removes labels

  var machineCode = document.getElementById('machine-code');  // grab ref to 'div' to which machine code will be appended
  machineCode.innerHTML = '';                                 // (and clear it)

  appendHeader();                                             // append 'Machine Code:' to document

  for (var i = 0; i < assemblyCode.length; i++) {             // translate to binary, line by line

    var line = assemblyCode[i];
    binary = parser(line);
    appendToPage(binary, machineCode);
  }

};

// parse out lines of code, put each in array entry;
// remove label headers, assigning them proper numerical values in table...
var reformatCode = function (code) {

  var line = '';
  var result = [];

  for (var i = 0; i < code.length; i++) {

    if (code[i] !== ' ') {                          // discern lines through empty spaces

      line += code[i];
    }
    else if (line) {                                // (line) to ensure long empty-spaces don't create entries in 'result'

      if (code[i-1] === ')') {                      // catches label

        var label = line.slice(1, line.length-1);
        table[label] = result.length;
      }
      else result.push(line);

      line = '';
    }
  }

  return result;
};

var appendToPage = function (binary, target) {

  var machineInstruction = document.createElement('p');
  machineInstruction.innerHTML = binary;
  machineInstruction.style.margin = '0px';
  target.appendChild(machineInstruction);
};

var appendHeader = function () {

  var header = document.getElementById('header');
  header.innerHTML = '';
  header.innerHTML = 'Machine Code: ';
};