## Words

### Definition
- A word is a fixed-sized unit of data that a processor can handle as a single unit.
- Commonly discussed type: unsigned integers (non-negative integers).
- Limitations of computers:
  - Finite storage requires representation for negative numbers and fractions.

### Word Size
- The size of numbers that can be represented is termed the "word size".
- Computer memory is divided into words.
- Typical modern computers:
  - 32-bit or 64-bit machines.
  - Some use 16-bit, especially embedded systems.
- Maximum number for a 64-bit word:
  - \(2^{64} - 1\)

## Byte

### Definition
- A byte consists of 8 bits.
- Binary representation ranges:
  - 00000000 (0) to 11111111 (255)
- Maximum byte-sized number:
  - \(255 = 2^8 - 1\)

### Half Byte
- A half byte contains 4 bits.
- Maximum value:
  - Binary 1111 represents 15.

## Java Integer Types

### Integer Representations
- `int`: Default type, uses 32 bits.
- `byte`: Uses 8 bits.
- `short`: Uses 16 bits, saves memory but limits integer size.
- `long`: Uses 64 bits, accommodates larger values but may impact efficiency in 32-bit environments.

### Negative Integers
- Negative integers commonly represented using ranges (e.g., byte range: -8 to 7).

## Representations Supporting Negative Numbers

### Sign-Magnitude Representation
- Includes sign as an additional piece of information.
  - Corresponds to mathematical notation (e.g., +3, -102).
- Format:
  - Left-most bit for sign: 0 = +, 1 = -.
  - Remaining bits represent absolute value.
- Example (4-bit representation):
  - +3: 0011
  - -3: 1011
- Issues:
  - Dual representations for zero (wasted space).
  - Arithmetic issues with negative numbers.

### Excess Representation
- Range: Starts at \(-2^{n-1}\) to \(2^{n-1} - 1\).
  - Example (n = 8):
    - 00000000 represents -128.
    - 11111111 represents 127.
- Properties:
  - Bit strings in alphanumeric order show a bias at 0 (positives below, negatives above).
- Arithmetic:
  - Calculation method requires additional steps:
    - \(x + 2^{n-1} + y + 2^{n-1}\) 
    - Subtract \(2^{n-1}\) from the result.
- Bias can be adjusted in excess representation.

---