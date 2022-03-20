#membuat dictionary dan mengisi value/nilai
perkenalan = {"nama" : "Ainum sahra","fakultas" : "teknik", "alamat" : "lapeo"}


#menampilkan dictionary menggunakan perulangan
for i in perkenalan :
    print(i, '->', perkenalan[i])


#mengupdate nilai/value didalam dictionary
perkenalan ["nama"] = "inung"
print(perkenalan)
#menghapus salah satu nilai/value dalam dictionary
perkenalan.pop("alamat")
print(perkenalan)

#menambahkan nilai/value ke dalam dictionary
perkenalan ["hobi"] = "badminton"
print(perkenalan)
