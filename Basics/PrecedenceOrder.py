# PrecedenceOrder.py

# Example 1: Multiplication has higher precedence than addition
result1 = 2 + 3 * 4    # 3*4=12, then 2+12=14
print("2 + 3 * 4 =", result1)

# Example 2: Parentheses change the order
result2 = (2 + 3) * 4  # 2+3=5, then 5*4=20
print("(2 + 3) * 4 =", result2)

# Example 3: Exponentiation has higher precedence than multiplication
result3 = 2 * 3 ** 2   # 3**2=9, then 2*9=18
print("2 * 3 ** 2 =", result3)

# Example 4: Left-to-right associativity for operators with same precedence
result4 = 10 - 4 + 2   # (10-4)=6, then 6+2=8
print("10 - 4 + 2 =", result4)

# Example 5: Comparison and logical operators
result5 = 3 < 4 and 4 < 5  # 3<4=True, 4<5=True, True and True=True
print("3 < 4 and 4 < 5 =", result5)

# Example 6: Not operator has higher precedence than and
result6 = not False and True  # not False=True, True and True=True
print("not False and True =", result6)