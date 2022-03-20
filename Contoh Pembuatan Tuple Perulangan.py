#membuat contoh tuple
buah = ("apel","anggur","nanas","pisang","cherry")

#menampilkan tuple dengan perulangan
for i in buah :
    print(i)

b = 0
while b < len(buah):
    print(buah[b])
    b += 1

#mengupdate salah satu tuple
buah = list(buah)

buah [2] = "nangka"
print(buah)

#menghapus salah satu tuple
buah.pop ()
print(buah)

del buah [0:3]
print(buah)

buah.remove ("pisang")
print(buah)

#menambah tuple
buah.append ("rambutan")
print(buah)

buah.extend (["mangga","manggis"])
print(buah)

buah.insert (3, "lengkeng")
print(buah)
