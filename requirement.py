class Pacflix_user :
    def __init__ (self):
        self.nama = ""
        self.plan = ""
        self.duration = 0
        self.harga_basic = 120000
        self.harga_standart = 160000
        self.harga_premium = 200000
        self.diskon_user_baru = 0.05
        self.diskon_upgrade_user_lama = 0.
        self.nama_user_tersedia = []

    def daftar_layanan (self,on):
        print("\nBerikut 3 plan yang Kami tawar kan dalam Paclix untuk 1 bulan:\n" )
        print (f"1. Basic Plan: Rp. {harga_basic}")
        print ("    a. Layanan Streaming film")
        print ("    b. film berkualitas SD")
        print ("    c. layanan download film")
        print ("    d. dengan konten 3rd party movie ")
        print ("    e. 1 Akun hanya 1 device")

        print("\n")

        print (f"2. Standart Plan: Rp. {harga_standart}")
        print ("    a. Layanan Streaming film")
        print ("    b. film berkualitas SD & HD")
        print ("    c. layanan download film")
        print ("    d. dengan konten 3rd party movie + Sport(Football/Soccer, F1, Basketball) ")
        print ("    e. 1 Akun hanya 2 device")
        print("\n")

        print (f"3. Premium Plan: Rp. {harga_premium}")
        print ("    a. Layanan Streaming film")
        print ("    b. film berkualitas SD, HD, UHD")
        print ("    c. layanan download film")
        print ("    d. dengan konten Basic Plan + Standart Plan + Pacflix Original Series/Movies")
        print ("    e. 1 Akun hanya 4 device")
        print("\n")

        def login (self):
            self.daftar_layanan()
            

                try:
                    user = input("Masukkan nama user anda : ")
                    layanan_dipesan = input("Layanan yang anda pilih (Bisa input nama paln atau no. daftar plan, ex: 3) : ")
                    # for user_data in nama_user_tersedia:
                    #     if user not in nama_user_tersedia:
                    #         print("Mnedapat diskon sebesar 4%")
                    #         nama_user_tersedia.append(user)
                    #         diskon_user = diskon_user_baru
                    #     else:
                    #         if self.plan.lower() == "basic"


                    if layanan_dipesan.lower() == "basic" or layanan_dipesan == "1":
                        harga_layanan = harga_basic
                        print("layanan yang anda pilih Basic")
                        break
                    elif layanan_dipesan.lower() == "standart" or layanan_dipesan == "2":
                        harga_layanan = harga_standart
                        print("layanan yang anda pilih Standart")
                        break
                    elif layanan_dipesan.lower() == "premium" or layanan_dipesan == "3":
                        harga_layanan = harga_premium
                        print("layanan yang anda pilih Premium")
                        break
                    else:
                        raise NameError
                except NameError or ValueError:
                    print("tolong input dengan benar")
    

user_1 = Pacflix_user()

men_user_1 = user_1.login()





    # while True:
    #     try:
    #         layanan_dipesan = input("Layanan yang anda pilih (Bisa input nama paln atau no. daftar plan, ex: 3) : ")
    #         if layanan_dipesan.lower() == "basic" or layanan_dipesan == "1":
    #             harga_layanan = harga_basic
    #             print("layanan yang anda pilih Basic")
    #             break
    #         elif layanan_dipesan.lower() == "standart" or layanan_dipesan == "2":
    #             harga_layanan = harga_standart
    #             print("layanan yang anda pilih Standart")
    #             break
    #         elif layanan_dipesan.lower() == "premium" or layanan_dipesan == "3":
    #             harga_layanan = harga_premium
    #             print("layanan yang anda pilih Premium")
    #             break
    #         else:
    #             raise NameError
    #     except NameError or ValueError:
    #         print("tolong input dengan benar")
        