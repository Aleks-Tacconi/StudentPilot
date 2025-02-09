## Sign-Magnitude Representation

### Overview
- The sign of a number is stored as an additional piece of information.
- Corresponds to mathematical notation (e.g., +3, -102).
- Uses one bit for the sign, with the left-most bit typically used.
- Remainder of the sequence represents the absolute value of the number.
- Represents `0` for positive and `1` for negative.

### 4-bit Representation Examples
- +3 is represented as `0011`
- -3 is represented as `1011`

### Issues
- Arithmetic complications:
  - Adding two positive numbers works.
  - Adding two negative numbers works.
  - Adding a positive and a negative does not work.
- Presence of two representations for zero, leading to wasted representation.

## Excess Representation

### Overview
- Starts at `-2^(n-1)` and goes up to `2^(n-1) - 1`.
  
### Example for n = 8
- `00000000` represents `-128`
- `11111111` represents `127`

### Characteristics
- In alphanumeric order, `0` is just below the middle:
  - Positive numbers are below `0`.
  - Negative numbers are above `0`.
- Bias is `0`.

### Arithmetic with Excess Representation
- Not natural; for `x + y`, the process is:
  - Compute: `x + 2^(n-1) + y + 2^(n-1)`
  - Subtract: `2^(n-1)`
  - Result: `x + y + 2^(n-1)` in excess representation.
  - Decode the final answer to get `x + y`.

### Adjusting Bias
- It is possible to change the bias when using excess representation.