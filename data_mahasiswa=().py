data_mahasiswa=()
{
    "nim": "71220899",
    "nama": "bambang",
    "prodi": "imformatika",
    "ipk": 5.2,
    "semester":4,
    "mata_kuliah":[
        {"nama":"IMK","sks":3,"nilai": "B"},
        {"nama":"tekkom","sks":3,"nilai": "C"},
        {"nama":"Jarkom","sks":5,"nilai": "E"},
    ],
}
print(data_mahasiswa["nama"])
print(f'IPK-nya: {data_mahasiswa["ipk"]}')
print(f'sudah mengambil{len(data_mahasiswa["mata_kuliah"])}mata_kuliah')
transkrip= data_mahasiswa["mata_kuliah"]
total=0
# total sks
total_bobot=0
for matkul in transkrip:
    if matkul["nilai"] == "E":
        print(matkul["nama"])
        total=total+matkul["sks"]
    elif  matkul["nilai"] =="A":
        total_bobot=total_bobot+4* matkul["sks"]
    elif  matkul["nilai"] =="B":
        total_bobot=total_bobot+3* matkul["sks"]
    elif  matkul["nilai"] =="C":
        total_bobot=total_bobot+2* matkul["sks"]
    elif  matkul["nilai"] =="D":
        total_bobot=total_bobot+1* matkul["sks"]
    elif  matkul["nilai"] =="E":
        total_bobot=total_bobot+0* matkul["sks"]
    
print(f'total sks yang diambil ')