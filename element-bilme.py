import time # kullanmamın nedeni oyuna başlamadan önce biraz ara vermesini istiyorum

kolay1cevap = "C"
kolay2cevap = "C"
kolay3cevap = "A"
kolay4cevap = "C"
kolay5cevap = "B"
kolay6cevap = "D"

zor1cevap = "A"
zor2cevap = "D"
zor3cevap = "D"


girdi = int(input("Element Bilme Oyununa Hoşgeldiniz!\n\n1 - Kolay\n2 - Orta\n3 - Zor\n\nLütfen bir zorluk seviyesi belirtiniz: "))

if girdi == 1:
    print("Kolay seviyeyi seçtiniz. Oyun başlıyor...")
    time.sleep(1.5) # 1.5 saniye sonra mesajı gönderecek
    kolay1 = input("Hidrojen elementinin sembolü nedir?\nA) Hi  B) He  C) H  D) Be\nCevabınız: ")
    kolay1 == kolay1cevap and print("Cevabınız doğru!")
    kolay1 != kolay1cevap and print("Cevabınız yanlış!")

    kolay2 = input("Karbon elementinin sembolü nedir?\nA) Ka  B) K  C) C  D) Ca\nCevabınız: ")
    kolay2 == kolay2cevap and print("Cevabınız doğru!")
    kolay2 != kolay2cevap and print("Cevabınız yanlış!")

    kolay3 = input("Potasyum elementinin sembolü nedir?\nA) K  B) Po  C) P  D) Au\nCevabınız: ")
    kolay3 == kolay3cevap and print("Cevabınız doğru!")
    kolay3 != kolay3cevap and print("Cevabınız yanlış!")

    kolay4 = input("Neon elementinin sembolü nedir?\nA) N  B) Neo  C) Ne  D) No\nCevabınız: ")
    kolay4 == kolay4cevap and print("Cevabınız doğru!")
    kolay4 != kolay4cevap and print("Cevabınız yanlış!")

    kolay5 = input("Altın elementinin sembolü nedir?\nA) Al  B) Au  C) Cu  D) C\nCevabınız: ")
    kolay5 == kolay5cevap and print("Cevabınız doğru!")
    kolay5 != kolay5cevap and print("Cevabınız yanlış!")

    kolay6 = input("Bakır elementinin sembolü nedir?\nA) B  B) Bo  C) Ba  D) Cu\nCevabınız: ")
    kolay6 == kolay6cevap and print("Cevabınız doğru!")
    kolay6 != kolay6cevap and print("Cevabınız yanlış!")
    print("Oyun bitmiştir..")

if girdi == 3:
    print("Zor seviyeyi seçtiniz. Oyun başlıyor..")
    time.sleep(1.5)
    zor1 = input("Aşağıdakilerden hangisi alkali metal grubunda değildir?\nA) Berilyum\nB) Lityum\nC) Potasyum\nD) Sodyum")
    zor1 == zor1cevap and print("Cevabınız doğru!")
    zor1 != zor1cevap and print("Cevabınız yanlış!")

    zor2 = input("Aşağıdakilerden hangisi ilk 20 elementin içinde bulunmaz?\nA) Magnezyum\nB) Hidrojen\nC) Helyum\nD) Titanyum")
    zor2 == zor2cevap and print("Cevabınız doğru!")
    zor2 != zor2cevap and print("Cevabınız yanlış!")

    zor3 = input("Aşağıdakilerden hangisi soygazlar grubunda değildir?\nA) Kripton\nB) Argon\nC) Radon\nD) Hidrojen")
    zor3 == zor3cevap and print("Cevabınız doğru!")
    zor3 != zor3cevap and print("Cevabınız yanlış!")

# python element-bilme.py
