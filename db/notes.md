## Words
- A word is a fixed-sized unit of data that a processor can handle as a single unit.
- We have discussed unsigned integers: non-negative integer numbers.
- Computers are finite and need to represent negative numbers, fractions, etc.
- There is a limit on the size of numbers a computer can represent (word size).
- Computer memory is usually divided into words.

### Word Sizes
- Modern general purpose computers typically have:
  - 32-bit or 64-bit
  - 16-bit machines are used 
  - Embedded systems often have different word sizes
- Largest number in a 64-bit word = \(2^{64} - 1\)

## Byte
- A byte = 8 bits
- Binary representation:
  - 00000000 is 0
  - 11111111 is 255
- Largest byte-sized number = 255 \(= 2^8 - 1\)

### Half Byte
- A half byte = 4 bits
- Binary representation:
  - 1111 is 15

## Java Integer Types
- Integer representations in Java include:
  - `int`: default, uses 32 bits 
  - `byte`: uses 8 bits 
  - `short`: uses 16 bits (saves memory, restricts integer size)
  - `long`: uses 64 bits (allows larger values, efficiency impact in 32-bit)

### Negative Integers
- Negative integers in byte range: -8 to 7 instead of 0 to 15.
- Several representations that support negative numbers are considered.

## Representations of Integers

### Sign-Magnitude Representation
- Sign of a number stored as additional information.
  - Corresponds to usual mathematical notation (e.g. +3, -102).
- Left-most bit used for the sign; remaining bits represent absolute value.
- Representation:
  - 0 for positive; 1 for negative.
  - 4-bit example:
    - +3 as 0011
    - -3 as 1011
- Issues:
  - Arithmetic problems with two negative numbers.
  - Two representations of zero (wasting a value).

### Excess Representation
- Starts at \(-2^{n-1}\) and goes up to \(2^{n-1} - 1\).
  - Example with \(n = 8\):
    - 00000000 represents -128
    - 11111111 represents 127
- Bit strings in alphanumeric order:
  - Zero below the middle, positive numbers below, negatives above.
  - Bias is 0.
  
#### Arithmetic in Excess
- Arithmetic using excess representation is not natural:
  - To perform \(x + y\), compute:
    - \(x + 2^{n-1} + y + 2^{n-1} - 1\)
    - Subtract \(2^{n-1}\)

### Changing the Bias
- Possible to change the bias when using excess representation.