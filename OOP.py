class BangunDatar:
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 3.14 * self.jari_jari ** 2

class Trapesium(BangunDatar):
    def __init__(self, sisi_atas, sisi_bawah, tinggi):
        self.sisi_atas = sisi_atas
        self.sisi_bawah = sisi_bawah
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * (self.sisi_atas + self.sisi_bawah) * self.tinggi

def main():
    n = int(input("Masukkan jumlah bangun datar: "))
    bangun_datar_list = []
    for i in range(n):
        jenis = input(f"Bangun datar ke-{i+1} (persegi/persegi panjang/segitiga/lingkaran/trapesium): ")

        if jenis == "persegi":
            sisi = float(input("Masukkan panjang sisi: "))
            bangun_datar_list.append(Persegi(sisi))
        elif jenis == "persegi panjang":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            bangun_datar_list.append(PersegiPanjang(panjang, lebar))
        elif jenis == "segitiga":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            bangun_datar_list.append(Segitiga(alas, tinggi))
        elif jenis == "lingkaran":
            jari_jari = float(input("Masukkan jari-jari: "))
            bangun_datar_list.append(Lingkaran(jari_jari))
        elif jenis == "trapesium":
            sisi_atas = float(input("Masukkan panjang sisi atas: "))
            sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
            tinggi = float(input("Masukkan tinggi: "))
            bangun_datar_list.append(Trapesium(sisi_atas, sisi_bawah, tinggi))
        else:
            print("Jenis bangun datar tidak valid.")

    luas_list = [bd.hitung_luas() for bd in bangun_datar_list]
    luas_list.sort()

    total_luas = sum(luas_list)

    print("Luas masing-masing bangun datar:", luas_list)
    print("Total luas bangun datar:", total_luas)


if __name__ == "__main__":
    main()