# My solutions for Nand2Tetris : Building a Modern Computer from First Principles

Nand2Tetris is a hands-on educational resource that allows students to - virtually - build a modern computer from the logic gate Nand. It was developed by Israeli computer scientists Noam Nisan and Shimon Shocken (see nand2tetris.org).

# So far . . .

**Project 1:** Only given a 1-bit Nand, implement the other 15 or so most fundamental logic gates (building up to a few 16-bit gates).

**Project 2:** Implement a Half-Adder, a Full-Adder, an ALU, and more, all using the logic gates from Project 1.

**Project 3:** Implement a single-bit Register, a 16-bit Register, a PC (program counter), and a 16K-register RAM, all using chips from before with a D-flip-flop provided (to help discretize time).

**Project 4:** Using the provided "Hack" assembly language, write a program that turns the output screen black, and another program that multiples two positive integers. 

**Project 5:** With only the chips developed in Project 1 to 3, implement a CPU that follows instructions from the assembly language that was introduced in Project 4. (A Memory component is developed as well.)

**Project 6:** Write an assembler in a higher-language of choice. It should convert each line of a Hack program to a 16-bit bus of binary. I learned Python to complete this project, though I also completed it with the more familiar Javascript.

* * *

To try out the Javascript assembler, open up index.html in HackAssembler, and manually paste your assembly code into the input box. To use the Python assembler, run:

  $ python HackAssembler/main.py [path to targeted assembly code]

This will create a file in the same folder as the assembly code, and store its machine-code translation there.


