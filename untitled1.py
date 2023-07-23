import random

def kelime_listesi_oku(kelime_tahmin):
    with open(kelime_tahmin, "r", encoding="utf-8") as dosya:
        kelime_listesi = dosya.readlines()
    return kelime_listesi

def rastgele_kelime_sec(kelime_listesi):
    return random.choice(kelime_listesi).strip()

def oyunu_baslat():
    print("Kelime Tahmin Oyununa Hoş Geldiniz!")
    print("Kurallar:")
    print("- Bilgisayar rastgele bir kelime seçecek.")
    print("- Tahmin etmek için kelimenin uzunluğunu bilmeye çalışın.")
    print("- Her yanlış tahminde size doğru harf sayısı gösterilecektir.")
    print("- Toplamda 5 tahmin hakkınız vardır.\n")

    kelime_tahmin = "kelimeler.txt"
    kelimeler = kelime_listesi_oku(kelime_tahmin)
    rastgele_kelime = rastgele_kelime_sec(kelimeler)
    kelime_uzunlugu = len(rastgele_kelime)  # Kelimenin uzunluğunu doğru bir şekilde alıyoruz
    tahmin_hakki = 5
    skor = 0
    dogru_tahmin = ["_" for _ in range(kelime_uzunlugu)]

    while tahmin_hakki > 0:
        print("Kelimenin Uzunluğu:", kelime_uzunlugu)
        print(" ".join(dogru_tahmin))

        while True:
            tahmin = input("Tahmininizi girin: ").lower()
            if len(tahmin) != kelime_uzunlugu:
                print("Hatalı tahmin. Lütfen kelime uzunluğunda bir tahmin yapın.")
            else:
                break

        if tahmin == rastgele_kelime:
            skor += 1
            print("Tebrikler! Doğru tahmin. Skorunuz:", skor)
            break
        else:
            dogru_harf_sayisi = sum(1 for x, y in zip(tahmin, rastgele_kelime) if x == y)
            print("Yanlış tahmin. Doğru harf sayısı:", dogru_harf_sayisi)
            tahmin_hakki -= 1
            print("Kalan tahmin hakkınız:", tahmin_hakki)

            for i in range(kelime_uzunlugu):
                if tahmin[i] == rastgele_kelime[i]:
                    dogru_tahmin[i] = tahmin[i]

    if tahmin_hakki == 0:
        print("Üzgünüm, tahmin hakkınız kalmadı. Doğru kelime:", rastgele_kelime)

    tekrar_oyna = input("Tekrar oynamak istiyor musunuz? (Evet/Hayır): ").lower()
    if tekrar_oyna == "evet":
        oyunu_baslat()
    else:
        print("Oyunu tamamladınız. İyi günler!")

if __name__ == "__main__":
    oyunu_baslat()
