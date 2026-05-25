# hp_prices = [
#     ["iphone", 15000000],
#     ["samsung", 12000000],
#     ["vivo", 1000000],
#     ["oppo", 9000000],
#     ["xiaomi", 7000000]
# ]


# def display_menu():
#     print ("\nMenu:")
#     print ("1. Lihat seluruh data")
#     # print ("2. Tambah data")
#     # print ("3. Hapus data")
#     # print ("4. Ubah harga")
#     # print ("5. Hitung rata-rata harga")
#     print ("6. Keluar")

# def lihat_data():
#     print("\nData Harga HP:")
#     if not hp_prices:
#         print("Tidak ada data.")
#         return
#     for hp in hp_prices:
#         nama, harga = hp
#         print(f"- {nama}: Rp{harga:,}")

# def main():
#     while True:
#         display_menu()
#         pilihan = input("Pilih menu (1-6): ")
#         if pilihan == "1":
#             lihat_data()
#         elif pilihan == "6":
#             print("Terimakasih! Program selesai.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     main()

# data username dan password
username_db = ""
password_db = ""


# function register
def register():
    global username_db
    global password_db

    print("\n=== REGISTER ===")

    username = input("Buat Username : ")
    password = input("Buat Password : ")

    username_db = username
    password_db = password

    print("Register Berhasil!")


# function login
def login():
    print("\n=== LOGIN ===")

    kesempatan = 3

    while kesempatan > 0:
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")

        # cek username dan password
        if username == username_db and password == password_db:
            print("Login Berhasil!")
            break
        else:
            kesempatan = kesempatan - 1
            print("Username atau Password Salah!")
            print("Sisa Kesempatan :", kesempatan)

    if kesempatan == 0:
        print("Login Gagal 3x")


# function lihat akun
def lihat_akun():
    print("\n=== DATA AKUN ===")

    if username_db == "":
        print("Belum ada akun")
    else:
        print("Username :", username_db)
        print("Password :", password_db)


# menu utama
while True:
    print("\n====================")
    print(" SISTEM LOGIN ")
    print("====================")
    print("1. Register")
    print("2. Login")
    print("3. Lihat Akun")
    print("4. Keluar")

    pilih = input("Pilih Menu : ")

    # pilihan menu
    if pilih == "1":
        register()

    elif pilih == "2":
        login()

    elif pilih == "3":
        lihat_akun()

    elif pilih == "4":
        print("Program Selesai")
        break

    else:
        print("Menu Tidak Ada")