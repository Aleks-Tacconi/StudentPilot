## Sign-Magnitude Representation

### Overview
- The sign of a number is stored as an additional piece of information.
- Corresponds to typical mathematical notation (e.g., +3, -102).
- One of the bits (usually the left-most) is designated for the sign.
- The remaining bits represent the absolute value of the number.

### Bit Representation
- **Sign Encoding**: 
  - 0 for positive (+)
  - 1 for negative (-)
- **Examples in 4-bit Representation**:
  - +3 is represented as `0011`
  - -3 is represented as `1011`

### Issues
- **Arithmetic Limitations**:
  - Addition of two positive numbers works.
  - Addition of two negative numbers works.
  - Addition of a positive and a negative number does not work properly.
- **Redundant Representations**:
  - Two representations for 0 (positive zero and negative zero) lead to wastage.

## Excess Representation

### Concept
- Starts at `-2^(n-1)` and goes up to `2^(n-1) - 1`.
- For `n = 8`:
  - `00000000` represents -128
  - `11111111` represents 127

### Bit String Order
- When arranged in alphanumeric order:
  - 0 is just below the middle.
  - Positive numbers are below, and negative numbers are above.
  - The bias in this case is 0.

### Arithmetic with Excess Representation
- Arithmetic is possible but not straightforward:
  - To perform `x + y`, the process is:
    - Compute: `x + (2^(n-1)) + y + (2^(n-1))`
    - Then subtract: `2^(n-1)` to decode the result.
    - Final equation: `x + y + (2^(n-1))` -> Result in excess representation.
- Bias Adjustment:
  - It is possible to change the bias when using excess representation.