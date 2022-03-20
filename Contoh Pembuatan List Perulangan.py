#membuat contoh list
nama = ["inung","cumma","ciyyu","mon","nami"]

#menampilkan list dengan perulangan
for i in nama :
    print(i)

print("="*20)
i = 0
while i < len(nama) :
    print(nama[i])
    i += 1

#mengupdate salah satu list
nama [1] = "mell"
print(nama)

#menghapus salah satu list
nama.pop()
print(nama)

del nama[1:4]
print(nama)

nama.remove("inung")
print(nama)

#menambahkan list
nama.append("inung")
print(nama)

nama.extend(["rayhan","angga"])
print(nama)

nama.insert(3, "avivi")
print(nama)
