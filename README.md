# BrainBack
BrainBack is an open-source BrainFuck IDE.
## What is BrainFuck?
BrainFuck is an esortic programming language 
created by Urban Müller in 1993 as a challange
to create a programming language with smallest
possible compiler. With this language you can't
create software, but make some challange to your
brain.
### Language overview
Brainfuck operates on an array of memory cells, each initially set to zero. (In the original implementation, the array was 30,000 cells long, but this may not be part of the language specification; different sizes for the array length and cell size give different variants of the language). There is a pointer, initially pointing to the first memory cell. The commands are:
* `>` that moves the pointer to the right;
* `<`	that moves the pointer to the left;
* `+`	that increments the memory cell at the pointer;
* `-`	that decrements the memory cell at the pointer;
* `.`	that outputs the character signified by the cell at the pointer;
* `,`	that inputs a character and store it in the cell at the pointer;
* `[`	that jumps past the matching `]` if the cell at the pointer is 0;
* `]`	that jumps back to the matching `[` if the cell at the pointer is non-zero.

All characters other than `>`, `<`, `+`, `-`, `.`, `,`, `[` and `]` should be considered comments and ignored.

### Links
BrainFuck on EsoLang.org: https://esolangs.org/wiki/Brainfuck;

BrainFuck on Wikipedia: https://en.wikipedia.org/wiki/Brainfuck;

BrainFuck in 100 seconds by [FireShip](https://www.youtube.com/c/Fireship): https://www.youtube.com/watch?v=hdHjjBS4cs8.
