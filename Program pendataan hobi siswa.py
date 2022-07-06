nama = []
asal = []
nim = []

masnim = input("masukan nim : ")
nim.append({'nim' : masnim})
masnama = input("masukan nama : ")
nama.append({'nama' : masnama})
masasal = input("masukan asal : ")
asal.append({'asal' : masasal}) 

# Membuat list kosong untuk menampung hobi
hobi = []
stop = False
i = 0

# Mengisi hobi
while(not stop):
    hobi_baru = input("Inputkan hobi yang ke-{}: " +format(i))
    hobi.append(hobi_baru)

     # Increment i
    i += 1
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"):
        stop = True

# Cetak Semua Hobi
print ("=" * 10)
print (nama,asal,nim,"Kamu memiliki hobi" +format(len(hobi)))
for hb in hobi:
    print ("- " +format(hb))