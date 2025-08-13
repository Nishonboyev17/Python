# 1. Mashina nomlarini ajratish

txt = 'MsaatmiazD'

mashina = txt[::2]
print("Mashina nomi:", mashina)



# 2. Shaxs qayerdan ekanligini ajratish

txt = "I'm John. I am from London"

sozlar = txt.split()
index = sozlar.index("from")
joy = sozlar[index + 1]
print("Qayerdan:", joy)


# 3. Matnni teskari chiqarish
matn = input("Matn kiriting: ")
teskari = matn[::-1]
print("Teskari matn:", teskari)


# 4. Palindrom tekshiruvi

soz = input("So‘z kiriting: ")
if soz == soz[::-1]:
     print("Bu so‘z palindrom.")
else:
     print("Bu so‘z palindrom emas.")


# 5. Mevalar ro‘yxati va uchinchi meva

mevalar = ['olma', 'banan', 'shaftoli', 'gilos', 'anor']
print("Uchinchi meva:", mevalar[2])


# 6. Ikkita ro‘yxatni birlashtirish


 a = [1, 2, 3]
 b = [4, 5, 6]
 birlashtirilgan = a + b
 print("Yangi ro‘yxat:", birlashtirilgan)


# 7. Birinchi, o‘rta va oxirgi elementlardan yangi ro‘yxat

 royxat = [10, 20, 30, 40, 50, 60, 70]
 yangi_royxat = [royxat[0], royxat[len(royxat)//2], royxat[-1]]
 print("Yangi ro‘yxat:", yangi_royxat)


# 8. "Paris" shahri bor yoki yo‘qligini tekshirish

 shaharlar = ['Toshkent', 'New York', 'Paris', 'London']
 if 'Paris' in shaharlar:
     print("Paris ro‘yxatda bor.")
 else:
     print("Paris ro‘yxatda yo‘q.")

# 9. Ro‘yxatni siklsiz ikki marta takrorlash


 sonlar = [1, 2, 3]
 yangi_royxat = sonlar * 2
 print("Takrorlangan ro‘yxat:", yangi_royxat)


# 10. Birinchi va oxirgi elementlarni almashtirish

 sonlar = [10, 20, 30, 40, 50]
 sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]
 print("O‘zgartirilgan ro‘yxat:", sonlar)
