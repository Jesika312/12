daftar_harga= [
    {"nama":"apel","harga": 10000},
    {"nama":"jeruk","harga": 20000},
    {"nama":"durian","harga": 120000},
    {"nama":"kiwi","harga": 60000},
    {"nama":"melon","harga": 300000},
]

# tampilkan nama buah dan harga
# for buah in daftar_harga:
#     print(f'{buah["nama"]}-{buah["harga"]}')

# tampilkan buah yang paling mahal
# harga_termahal=0
# nama_buah_termahal=""
# for buah in daftar_harga:
#     if buah['harga'] > harga_termahal:
#         harga_termahal=buah['harga']
#         nama_buah_termahal=buah['nama']
#     print(f'nama buah termahal adalah {nama_buah_termahal} harga {harga_termahal}')

# hapus harga <100000
batas=100000
'''
for index in range (len(daftar_harga)):
    if daftar_harga [index]['harga'] < batas:
        del daftar_harga[index]
'''
# ambil jumlah dalam index
count=len(daftar_harga)
index=0
while index<count:
    if daftar_harga[index]["harga"] < batas:
        del daftar_harga[index]
    else:
        index=index+1
    count=len(daftar_harga)
# tampilkan semua buah dan harga
print("setelah di hapus")
for buah in daftar_harga:
    print(f'{buah["nama"]}-{buah["harga"]}')