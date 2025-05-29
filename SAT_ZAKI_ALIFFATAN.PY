import datetime

kereta = {
    "Argo Bromo": 158000,
    "Sancaka": 270000,
    "Argo Wills Panoramic": 758000
}

print("Selamat datang di Pemesanan Tiket Kereta Api")
print(f"Total pilihan kereta: {len(kereta)}\n")

for nama, harga in kereta.items():
    print(f"- {nama} (Rp{harga})")

pilihan = input("\nMasukkan nama kereta yang ingin Anda pesan: ")
jumlah_tiket = int(input("Masukkan jumlah tiket: "))

if pilihan in kereta:
    harga_tiket = kereta[pilihan]
    total = harga_tiket * jumlah_tiket

    if jumlah_tiket >= 5:
        diskon = round(0.1 * total)  # diskon 10%
    else:
        diskon = 0

    total_bayar = total - diskon

    print("\n-- Ringkasan Pemesanan --")
    print(f"Kereta : {pilihan}")
    print(f"Jumlah tiket : {jumlah_tiket}")
    print(f"Total awal : Rp{total}")
    print(f"Diskon : Rp{diskon}")
    print(f"Total bayar : Rp{total_bayar}")
    print("Waktu pesan :", datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    print("Terima kasih telah memesan tiket.")
else:
    print("Maaf, kereta yang Anda masukkan tidak tersedia.")
