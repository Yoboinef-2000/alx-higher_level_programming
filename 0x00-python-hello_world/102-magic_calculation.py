#!/usr/bin/python3
import dis

def magic_calculation(a, b):

    return a ** b + 98

# Compare bytecode
original_bytecode = dis.Bytecode(magic_calculation)
expected_bytecode = dis.Bytecode("""
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_POWER
              6 LOAD_CONST               1 (98)
              8 BINARY_ADD
             10 RETURN_VALUE
""")
assert list(original_bytecode) == list(expected_bytecode)
