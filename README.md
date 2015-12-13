# My solutions for Nand2Tetris

Nand2Tetris allows students to - virtually - build a modern computer, starting with the logic gate Nand. It was developed by Israeli computer scientists Noam Nisan and Shimon Shocken (see nand2tetris.org).

# So far . . .

**Project 1 ~ Boolean Logic:** Given a 1-bit Nand, implemented the other 15 or so most fundamental logic gates (building up to a few 16-bit gates). (See .hdl files.)

**Project 2 ~ Boolean Arithmetic:** Implemented a Half-Adder, a Full-Adder, an ALU, and more, using solely the logic gates from Project 1. (See .hdl files.)

**Project 3 ~ Sequential Logic:** Implemented a single-bit Register, a 16-bit Register, a PC (program counter), and a 16K-register RAM, with only the chips from before, with the exception of a D-flip-flop provided (to discretize time). (See .hdl files.)

**Project 4 ~ Machine Language:** With the provided "Hack" assembly language, wrote a program that turns the output screen black, and another program that multiples two positive integers. (See .asm files.)

**Project 5 ~ Computer Architecture:** With only the chips developed in Project 1 to 3, implemented a CPU that follows instructions written in the assembly code that was introduced in Project 4. (A 'Memory' component was developed as well.) (See .hdl files.)

**Project 6 ~ Assembler:** Wrote an assembler in a higher-language of choice. It converts each line of a Hack program to a 16-bit bus of binary. I learned Python to complete this project, though I completed it initially with Javascript. (See 'HackAssembler' folder.)

* * *

To try the Javascript assembler, open up index.html in HackAssembler, and manually paste your assembly code into the input box.

To try the Python assembler, run the following command in the Project 6 directory:

*python HackAssembler/main.py [path to targeted assembly code]*

This will create a file in the same folder as the chosen assembly code, and store its machine-code translation there.


