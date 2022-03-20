#membuat set dan mengisi value/nilai didalamnya
nilai = {"ainum sahra",18,1.44,False}
#menampilkan set menggunakan perulangan
for i in nilai :
    print(i)

#mengupdate nilai/valuedalam set
#menghapus salahsatu nilai/value dalam set
nilai.remove("ainum sahra")
print(nilai)

nilai.pop ()
print(nilai)
#menambahkan nilai/value k dalam set
nilai.add (True)
print(nilai)

nilai.update ({"rayhan","apel",6})
print(nilai)
