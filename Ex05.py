valores = ["5", 3.2, True]
convertidos = [int(val) if isinstance(val, str) else int(val) for val in valores]
print(convertidos, [type(x).__name__ for x in convertidos])
