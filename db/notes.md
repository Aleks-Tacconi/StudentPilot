## Sign-Magnitude Representation

### Overview
- The sign of a number is stored as an additional piece of information.
- Corresponds to usual mathematical notation: +3, -102.
- One bit (usually the left-most) is used for the sign, with the remainder representing the absolute value.

### Sign Representation
- Uses:
  - 0 for positive (+)
  - 1 for negative (-)

### Example in 4-bit Representation
- +3 is represented as: `0011`
- -3 is represented as: `1011`

### Issues with Sign-Magnitude
- **Arithmetic Operations:**
  - Adding two positive numbers works.
  - Adding two negative numbers works.
  - Adding a positive and a negative does not work properly.
- **Redundant Representation:**
  - There are two representations for zero: +0 and -0, wasting a representation.

## Excess Representation

### Definition
- Represents a range from -2^(n-1) to 2^(n-1) - 1.
- For n = 8:
  - `00000000` represents -128.
  - `11111111` represents 127.

### Ordering of Values
- When bit strings are ordered alphanumerically:
  - 0 is just below the middle.
  - Positive numbers are below 0.
  - Negative numbers are above 0.
  
### Bias
- The bias is 0 in this representation.

### Arithmetic with Excess Representation
- Arithmetic is possible but not natural.
- For calculating x + y:
  - Step 1: Compute x + 2^(n-1) + y + 2^(n-1).
  - Step 2: Subtract 2^(n-1).
  - Result in excess representation: x + y + 2^(n-1). 
  - Finally, decode to get the answer.

### Changing the Bias
- It is possible to alter the bias while using excess representation.