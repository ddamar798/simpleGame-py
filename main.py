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

namaUser = input("masukan namamu :")
print(f'''
Haii {namaUser}!
Coba perhatikan Goa dibawah ini :
 1    2    3    4
|_|  |_|  |_|  |_|
''')

pilihanUser = int (input("Menurutmu dimana tupai berada? [1 / 2 / 3 / 4 ]: "))
# apapun yang di masukan kedalam input bernilai string kecuali di validasi

print(f"pilihan kamu adalah {pilihanUser}")

if pilihanUser == tupai_position:
    print("Selamat anda benar!")
else: print(f"Pilihan anda salah! tupai berada di goa {tupai_position}.")
