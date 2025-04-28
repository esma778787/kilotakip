from datetime import date

class Kisi:
    def __init__(self, ad, soyad, boy, kilo, cinsiyet, d_yil, d_ay, d_gun):
        self.ad = ad
        self.soyad = soyad
        self.boy = boy
        self.kilo = kilo
        self.cinsiyet = cinsiyet
        self.d_yil = d_yil
        self.d_ay = d_ay
        self.d_gun = d_gun
        self.yaş = self.yas_hesapla()
        self.cins = "Bayan" if cinsiyet == 0 else "Bay"
        self.haftalar = []
        self.aylar = []
        self.bk_hesapla(kilo)

    def bk_hesapla(self, kilo):
        endeks = kilo / (self.boy ** 2)
        hafta = (self.boy, kilo, endeks)
        self.haftalar.append(hafta)
        self.c = endeks  # güncel endeksi kaydet

    def VucutEndeksiGoster(self):
        txt = "{} isimli, {} soyisimli, {} yaşında olan Sayın {}, vücut kitle endeksiniz: {:.2f}"
        print(txt.format(self.ad, self.soyad, self.yaş, self.cins, self.c), "\n")

    def aylik_kilo_gir(self, kilo):
        aylik_endeks = kilo / (self.boy ** 2)
        ay = (self.boy, kilo, aylik_endeks)
        self.aylar.append(ay)

    def bilgi(self):
        print("\n--- Haftalık Kilo Değişimi ---")
        for i in range(len(self.haftalar)):
            hafta = self.haftalar[i]
            bk_kategori = self.get_kategori(hafta[2])

            if i == 0:
                txt = "İlk durum -> Kilo: {:<10}, BK: {:.2f} => {:<30} Boy: {}"
                print(txt.format(hafta[1], hafta[2], bk_kategori, hafta[0]))
            else:
                haftalik_kilo_farki = hafta[1] - self.haftalar[i-1][1]
                gunluk_kilo_farki = haftalik_kilo_farki / 7
                txt = "{:<2}. hafta -> Kilo: {:<10}, BK: {:.2f} => {:<30} Günlük değişim: {:.2f} kg"
                print(txt.format(i, hafta[1], hafta[2], bk_kategori, gunluk_kilo_farki))

    def get_kategori(self, endeks):
        if endeks < 18.49:
            return "Zayıf (ideal kilonun altında)"
        elif endeks < 24.99:
            return "Normal (ideal kilo)"
        elif endeks < 29.99:
            return "Kilolu (ideal kilonun üstü)"
        else:
            return "Obez (ideal kilonun çok üstü)"

    def yas_hesapla(self):
        today = date.today()
        yaş = today.year - self.d_yil - ((today.month, today.day) < (self.d_ay, self.d_gun))
        return yaş

# Kullanıcıdan bilgi alma
ben = Kisi(
    input("Adınız: "),
    input("Soyadınız: "),
    float(input("Boyunuz (m): ")),
    float(input("Kilonuz (kg): ")),
    int(input("Cinsiyetiniz (Kadın=0, Erkek=1): ")),
    int(input("Doğum yılınız: ")),
    int(input("Doğum ayınız: ")),
    int(input("Doğum gününüz: "))
)

# Aylık kilo girişi
ben.aylik_kilo_gir(58.88)
ben.aylik_kilo_gir(54.66)

# Haftalık kilo girişi
girilecek_hafta = int(input("Kaç hafta girilecek (minimum 8 hafta)? "))
while girilecek_hafta < 8:
    girilecek_hafta = int(input("Lütfen en az 8 hafta giriniz: "))

for _ in range(girilecek_hafta):
    bu_haftaki_kilo = float(input("Bu haftaki kilonuz (kg): "))
    ben.bk_hesapla(bu_haftaki_kilo)

# Sonuçları gösterme
ben.VucutEndeksiGoster()
ben.bilgi()
