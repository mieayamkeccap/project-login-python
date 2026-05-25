# data username dan password
username_db = ""
password_db = ""


def register():
    global username_db
    global password_db

    print("\n=== REGISTER ===")

    username = input("Buat Username : ")
    password = input("Buat Password : ")

    username_db = username
    password_db = password

    print("Register Berhasil!")


def login():
    print("\n=== LOGIN ===")

    kesempatan = 3

    while kesempatan > 0:
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")

        if username == username_db and password == password_db:
            print("Login Berhasil!")
            break
        else:
            kesempatan = kesempatan - 1
            print("Username atau Password Salah!")
            print("Sisa Kesempatan :", kesempatan)

    if kesempatan == 0:
        print("Login Gagal 3x")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Keluar")

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        register()

    elif pilih == "2":
        login()

    elif pilih == "3":
        print("Program Selesai")
        break

    else:
        print("Menu Tidak Ada")
