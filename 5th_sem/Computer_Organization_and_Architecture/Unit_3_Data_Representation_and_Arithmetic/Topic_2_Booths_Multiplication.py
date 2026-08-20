# Python simulation of Booth's Multiplication Algorithm
def int_to_bin_list(val, bits):
    if val < 0:
        val = (1 << bits) + val
    bin_str = bin(val)[2:].zfill(bits)[-bits:]
    return [int(char) for char in bin_str]

def bin_list_to_int(bin_list):
    bits = len(bin_list)
    val = 0
    for idx, bit in enumerate(bin_list):
        val += bit * (2 ** (bits - 1 - idx))
    if bin_list[0] == 1:
        val -= (2 ** bits)
    return val

def add_bin(a, b):
    bits = len(a)
    result = [0] * bits
    carry = 0
    for i in range(bits - 1, -1, -1):
        total = a[i] + b[i] + carry
        result[i] = total % 2
        carry = total // 2
    return result

def twos_complement(a):
    bits = len(a)
    inverted = [1 - bit for bit in a]
    one = [0] * bits
    one[-1] = 1
    return add_bin(inverted, one)

def arithmetic_shift_right(A, Q, Q_minus_1):
    combined = A + Q + [Q_minus_1]
    shifted = [combined[0]] + combined[:-1]
    half_len = len(A)
    return shifted[:half_len], shifted[half_len:-1], shifted[-1]

def booths_multiply(m_val, q_val, bits=6):
    M = int_to_bin_list(m_val, bits)
    Q = int_to_bin_list(q_val, bits)
    M_neg = twos_complement(M)
    A = [0] * bits
    Q_minus_1 = 0
    for _ in range(bits):
        q0 = Q[-1]
        if q0 == 1 and Q_minus_1 == 0:
            A = add_bin(A, M_neg)
        elif q0 == 0 and Q_minus_1 == 1:
            A = add_bin(A, M)
        A, Q, Q_minus_1 = arithmetic_shift_right(A, Q, Q_minus_1)
    result = A + Q
    return bin_list_to_int(result)

print("Booth's Multiplication (7 * -3):", booths_multiply(7, -3))
