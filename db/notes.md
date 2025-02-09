# Sign-Magnitude Representation

## Overview
- Sign-magnitude representation is used to store the sign of a number separately from its magnitude.
- It mimics conventional mathematical notation (e.g., +3, -102).

## Structure
- The left-most bit indicates the sign of the number:
  - `0` represents positive numbers (+)
  - `1` represents negative numbers (-)
- The remaining bits represent the absolute value of the number.

## Example in 4-bit Representation
- **Positive Values:**
  - +3 is represented as `0011`
  
- **Negative Values:**
  - -3 is represented as `1011`