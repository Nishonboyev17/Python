# 1. Kvadratning perimetri va yuzasini topish
tomon = 5
perimetr = 4 * tomon
yuza = tomon ** 2
print(perimetr)
print(yuza)



# 2. Doiraning diametri berilgan. Uzunligini (aylanasini) topish

diametr = float(input("Doiraning diametrini kiriting: "))
uzunlik = math.pi * diametr
print("Doiraning uzunligi:", uzunlik)


# 3. Ikkita son a va b berilgan. Ularning o‘rtacha qiymatini topish

 a = float(input("a sonini kiriting: "))
 b = float(input("b sonini kiriting: "))
 ortacha = (a + b) / 2
 print("O‘rtacha qiymat:", ortacha)


# 4. Ikkita son a va b berilgan. Yig‘indisi, ko‘paytmasi va kvadratlari

 a = float(input("a sonini kiriting: "))
 b = float(input("b sonini kiriting: "))

 yigindi = a + b
 kopaytma = a * b
 a_kvadrat = a ** 2
 b_kvadrat = b ** 2

print("Yig‘indi:", yigindi)
print("Ko‘paytma:", kopaytma)
print("a ning kvadrati:", a_kvadrat)
print("b ning kvadrati:", b_kvadrat)
