price=float(input())
discount=float(input())
vat=float(input())
base = price*(1-discount/100)
vat_amount= base*(vat/100)
total = base+vat_amount
print(f"База после скидки: {base:.2F} ₽")
print(f"НДС: {vat_amount:.2F} ₽")
print(f"Итого к оплате: {total:.2F} ₽")