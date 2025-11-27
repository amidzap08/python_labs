a = input()
b = input()
a1 = a.replace(",", ".")
b1 = b.replace(",", ".")
a2 = float(a1)
b2 = float(b1)
sum_val = a2 + b2
avg = sum_val / 2
print(f"sum={sum_val:.2f}; avg={avg:.2f}")
