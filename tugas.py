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
