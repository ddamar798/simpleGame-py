import random

welcome_message = "LEARN PYTHON"
tupai_position = random.randint(1,4)



print("||============||")
print(f"||{welcome_message}||")
print("||============||")

# nomorSaya = 7
# if nomorSaya == 3:
#     print("Yaa nomor saya emang 3")
# else: print("Salah nomermu bukan 3")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 #GOA INI HARUS TETAP KOSONG.
goa = goa_kosong.copy() #DISINI GOA TEMPAT TUPAI MUNCUL.

goa[tupai_position - 1] = "|🐰|"

goa_kosong = " ".join(goa_kosong) # .join digunakan untuk menhilangkan tanda array [" "]
goa = " ".join(goa)
 
namaUser = input("masukan namamu :")
print(f'''
Haii {namaUser}!
Coba perhatikan Goa dibawah ini :
{goa_kosong}
''')

pilihanUser = int (input("Menurutmu dimana Kelinci berada? [1 / 2 / 3 / 4 ]: "))
# apapun yang di masukan kedalam input bernilai string kecuali di validasi

validasi_pilihan = input (f"apakah kamu yakin jawabanya adalah {pilihanUser}? [y/n] : ")

if validasi_pilihan == "y":
    if pilihanUser == tupai_position:
         print(f"{goa} \n Selamat anda benar 🏆")
    else: 
         print(f"Pilihan anda salah!{goa} \n Kelinci berada di Goa {tupai_position}😛")
elif validasi_pilihan == "n":
    print("oke, program ditutup!")
    exit()
else :
    print("program eror! silahkan pilih [y/n]")
    exit()
