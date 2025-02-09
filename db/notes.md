## Sign-Magnitude Representation

### Overview
- The sign of a number is stored as an additional piece of information.
- This corresponds to the usual mathematical notation: 
  - +3, -102
  
### Representation
- One bit, usually the left-most, is used for the sign:
  - 0 represents positive (+)
  - 1 represents negative (-)
- The remainder of the sequence represents the absolute value of the number.
  
### Examples in 4-bit Representation
- +3 is represented as `0011`
- -3 is represented as `1011`

### Issues with Sign-Magnitude
- **Arithmetic challenges**:
  - Adding two positive numbers works.
  - Adding two negative numbers works.
  - Adding a positive and a negative does not work as expected.
- There are two representations for zero, leading to wasted representation:
  - +0 is `0000`
  - -0 is `1000`

## Excess Representation

### Overview
- Excess representation ranges from `-2^(n-1)` to `2^(n-1) - 1`.

### Example for n = 8
- `00000000` represents -128
- `11111111` represents 127

### Properties
- Writing bit strings in alphanumeric order places 0 just below the middle, with positive numbers below and negatives above.
- The bias for this system is 0.

### Arithmetic in Excess Representation
- To compute \( x + y \):
  1. Convert to excess: \( x + 2^{(n-1)} + y + 2^{(n-1)} \)
  2. Subtract \( 2^{(n-1)} \)
  3. Final result: \( x + y + 2^{(n-1)} \) (answer in excess representation)
  4. Decode to get \( x + y \) (final answer)
  
### Changing the Bias
- It's possible to adjust the bias when using excess representation.