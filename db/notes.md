## Sign-Magnitude Representation

### Overview
- The sign of a number is stored as an additional piece of information.
- This aligns with conventional mathematical notation: 
  - +3, -102
  
### Structure
- One bit (usually the left-most) is used for the sign.
- Remaining bits represent the absolute value of the number.
- 0 is used for positive (+) and 1 for negative (-).

### Examples
- In a 4-bit representation:
  - +3 is represented as `0011`
  - -3 is represented as `1011`

### Issues
- **Arithmetic Limitations**:
  - Adding two positive numbers works.
  - Adding two negative numbers works.
  - Adding a positive and negative number does not work.
- **Redundant Zero Representation**:
  - There are two representations for zero, wasting one possible value.

---

## Excess Representation

### Overview
- Starts at -2^(n-1) and extends to 2^(n-1) - 1.
  
### Example for n = 8 
- `00000000` represents -128.
- `11111111` represents 127.
  
### Properties
- When written in alphanumeric order:
  - 0 is just below the middle.
  - Positive numbers are below 0, while negatives are above.
- The bias is 0.

### Arithmetic in Excess Representation
- While possible, it requires additional steps:
  - For `x + y`, compute:
    - `x + 2^(n-1) + y + 2^(n-1) - 2^(n-1)`
  - Final result in excess representation must be decoded:
    - `x + y` gives the final answer.
  
### Changing the Bias
- The bias can be adjusted when using excess representation.