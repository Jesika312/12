# data={
#     'genap':[], 'ganjil':[]
# }

# while True:
#     angka=int(input("masukan sebuah angka[negatif untuk berhenti]:"))
#     if angka<0:
#         break
#     else:
#         if angka%2==0:
#             data["genap"].append(angka)
#         else:
#             data["ganjil"].append(angka)
# print(data)


data={}

while True:
    angka=int(input("masukan sebuah angka[negatif untuk berhenti]:"))
    if angka<0:
        break
    else:
        if angka%2==0:
            if data.get('genap') != None:
                data.get("genap").append(angka)
            
        else:
            data["ganjil"].append(angka)
print(data)