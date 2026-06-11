# Topic 2: Computer Arithmetic and Booth's Algorithm

- **2s Complement Arithmetic**: Subtraction is performed via addition: $A - B = A + \bar{B} + 1$.
- **Booth's Multiplication**: Multiplies signed 2s complement values. Evaluates multiplier bit pairs ($Q_0, Q_{-1}$) to decide whether to add, subtract, or just shift the accumulator.
