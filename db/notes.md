## Words

### Definition
- A word is a fixed-sized unit of data that a processor can handle as a single unit.
- Typically represents unsigned integers (non-negative numbers).
- Computers have finite capabilities, leading to the need for:
  - Negative numbers
  - Fractions
- The representation of numbers is limited by the word size, which is the number of digits used.

### Word Size
- Computer memory is usually divided into words.
- Common word sizes in modern computers:
  - 32-bit
  - 64-bit
  - 16-bit (used in some legacy systems)
- The largest number that a 64-bit word can hold is \(2^{64}-1\).

## Byte

### Definition
- A byte equals 8 bits.
  - Binary `00000000` equals 0.
  - Binary `11111111` equals 255.
- The largest byte-sized number is 255 (\(2^8-1\)).
  
### Half Byte
- A half-byte is 4 bits.
  - Binary `1111` represents 15.

## Java Integer Types

### Representation
- Java offers various integer representations:
  - `int`: Default, 32 bits.
  - `byte`: 8 bits.
  - `short`: 16 bits, saving memory but limiting integer size.
  - `long`: 64 bits, allows larger values but less efficient in a 32-bit environment.
- Negative integers are typically represented as:
  - For bytes: -8 to 7 instead of 0 to 15.

## Negative Number Representations

### Sign-Magnitude Representation
- Stores sign as an additional piece of information (corresponds to mathematical notation).
- One bit is used for the sign (usually the left-most).
  - 0 for positive, 1 for negative.
- Example in 4-bit representation:
  - +3 is `0011`
  - -3 is `1011`
- Issues:
  - Arithmetic problems when adding two negative numbers.
  - Existence of two representations for zero.

### Excess Representation
- Starts at \(-2^{n-1}\) and goes up to \(2^{n-1} - 1\).
  - For \(n=8\):
    - `00000000` represents -128
    - `11111111` represents 127
- In alphanumeric order, zero is placed just below the middle with positive numbers below and negatives above.
- The bias in this case is 0.

### Arithmetic with Excess Representation
- Not straightforward, requires additional steps:
  - For addition \(x + y\):
    1. \(x + 2^{n-1} + y + 2^{n-1}\)
    2. Subtract \(2^{n-1}\)
    3. The result is in excess representation.
    4. Decode to get the final answer: \(x + y\).

### Bias Adjustment
- The bias can be changed when using excess representation.