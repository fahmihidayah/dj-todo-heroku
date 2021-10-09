print("hello")

# variable

umur = 30

nama = "fahmi"

alamat = 'malang'

jarak = 20.4

print(nama + ' ' + alamat + ' ' + str(umur) + ' ' + str(jarak))


# percabangan

if umur == 12:
    print('umur muda')
else:
    print('umur tua')

print('baris baru')


if jarak > 50:
    print('jarak jauh')
elif jarak > 20 and jarak < 50:
    print('jarak sedang')
else:
    print('jarak dekat')


# perulangan
mahasiswa = [
    'budi',
    'tono',
    'fahmi'
]

for item_mahasiswa in mahasiswa:
    print(item_mahasiswa)

i = 0
while i < 10:
    print('data index ' + str(i))
    i = i + 1

for i in range(0, 10):
    print('data index lain ' + str(i))