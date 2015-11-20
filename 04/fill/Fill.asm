// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.


// ---------------------------------


// Store screen address
@SCREEN
D = A
@addr
M = D

// Store keyboard address
@KBD
D = A
@addrK
M = D


(LOOP)
	@KBD // checking current state of KBD
	D=M;
	@BLACKEN // if state != 0, blacken screen
	D;JNE
	// else:
	@WHITEN  // otherwise (if state = 0), whiten screen
	0;JMP

(WHITEN)
	// reset current spot to first spot in SCREEN memory map
	@addr 
	D = M
	@curr
	M = D
			
	@WHITEN_LOOP // loop through every address in SCREEN memory map
	0; JMP

(WHITEN_LOOP)
	@addrK // calc distance of current spot to KBD
	D = M - D
	@LOOP // if distane is 0, stop and go back to main LOOP
	D; JEQ
	
	@curr
	AD = M
	M = 0
	@curr
	MD = D + 1
	@WHITEN_LOOP
	0; JMP

(BLACKEN)
	@addr
	D = M
	@curr
	M = D
	@BLACKEN_LOOP
	0; JMP

(BLACKEN_LOOP)
	@addrK
	D = M - D
	@LOOP
	D; JEQ
	@curr
	AD = M
	M = -1
	@curr
	MD = D + 1
	@BLACKEN_LOOP
	0; JMP




