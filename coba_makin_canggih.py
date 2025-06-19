from tabulate import tabulate
# ini cuman buat tabel aja
headers = ["Fasilitas", "basic", "standart", "premium"]
data_fasilitas = [
    {"Harga": 120000, "Kualitas": "SD", "Konten": "3rd party movie", "Download_movie": True, "Number of Device" : 1},
    {"Harga": 160000, "Kualitas": "SD & HD", "Konten": "Basic Plan + Sport(Football/Soccer, F1, Basketball)", "Download_movie": True, "Number of Device" : 2},
    {"Harga": 200000, "Kualitas": "SD, HD, UHD", "Konten": "Basic Plan + Standart Plan + Pacflix Original Series/Movies", "Download_movie": True, "Number of Device" : 4},
]
daftar_harga = ["Harga"]
daftar_kualitas = ["Kualitas"]
daftar_konten = ["Konten"]
daftar_download =["Download"]
daftar_device = ["Number of Device"]
for mydata in data_fasilitas:
    daftar_harga.append(mydata["Harga"])
    daftar_kualitas.append(mydata["Kualitas"])
    daftar_konten.append(mydata["Konten"])
    daftar_download.append(mydata["Download_movie"])
    daftar_device.append(mydata["Number of Device"])
data_tiap = [daftar_harga,daftar_kualitas,daftar_konten,daftar_download,daftar_device]

print(tabulate(data_tiap, headers, tablefmt="grid"))
print("\nApabila anda pengguna baru, anda mendapatkan diskon dengan memasukkan referal code 'BPANDA'")

daftar_user = ["umi"] # ini ceritanya nama yang udah terdaftar
# tujuan : kalau input username = "umi" dia bakal nge-"trigger" class User

class PacFlix: # Parent Class
    def __init__ (self,username, current_plan, duration_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan
    
    def Facility_table (self): # buat plan-plannya sama fasilitas - fasilitasnya
        self.headers = ["basic", "standart", "premium"]
        self.data_fasilitas = [
            {"Harga": 120000, "Kualitas": "SD", "Konten": "3rd party movie", "Download_movie": True, "Number of Device" : 1},
            {"Harga": 160000, "Kualitas": "SD & HD", "Konten": "Basic Plan + Sport(Football/Soccer, F1, Basketball)", "Download_movie": True, "Number of Device" : 2},
            {"Harga": 200000, "Kualitas": "SD, HD, UHD", "Konten": "Basic Plan + Standart Plan + Pacflix Original Series/Movies", "Download_movie": True, "Number of Device" : 4},
        ]
    
    def check_benefit (self):
        self.Facility_table() 
        # self.Facility_table() disini supaya method check_benefit nge-"triger" atau ngerjain self.facility_table, perlu atau nggak ?
        # for this case, PERLU !!! supaya.... walaupun kita cuman manggil check_benefit dia juga sekalian ngejalanin self.Facility_table
        # sehingga kita bisa bebas makai variabel self.headers dan self.data_fasilitas (yang ada di self.Facility_table) di loop kita
        for i in range(len(self.headers)) :
            if self.current_plan.lower() == self.headers[i]:
                self.kualitas = self.data_fasilitas[i]["Kualitas"]
                self.content = self.data_fasilitas[i]["Konten"]
                self.download = self.data_fasilitas[i]["Download_movie"]
                self.harga = self.data_fasilitas[i]["Harga"]
                self.device = self.data_fasilitas[i]["Number of Device"]
    
        return f"benefit yang anda dapatkan berupa resolusi {self.kualitas} dengan konten {self.content}, serta anda dapat menghubungkan akun anda ke {self.device} device berbeda"
    
    def check_plan (self, username):
        return f"username {self.username} saat ini berlangganan {self.current_plan} selama {self.duration_plan}"


class User (PacFlix):
    def __init__ (self, username, current_plan, duration_plan):
        super().__init__(username, current_plan, duration_plan)
        self.discount = 0
        self.harga = 0
        self.final_cost_plan()
        print("\nAnda adalah user lama")
    
    
    def final_cost_plan (self):
        self.check_benefit()
        if self.duration_plan > 12:
            self.discount = 0.05
            self.diskon = "5%"
        else:
            self.discount = 0
            self.diskon = "0%"
        
        self.final_price = self.harga - (self.harga*self.discount)
        return f"Harga yang perlu di bayarkan = {self.final_price}"
    


class New_user (PacFlix):
    def __init__ (self, username, pick_plan,duration_plan ):
        super().__init__(username, pick_plan, duration_plan)
        self.referal_code = input("karana anda user baru, masukkan referal code: ")
        self.final_cost_plan()
    
    
    def final_cost_plan (self):
        list_referal = ["PacflixHemat", "PacflixExpo", "Pacflix123", "BPANDA"]
        self.check_benefit()
        if self.referal_code in list_referal:
            self.discount = 0.04
            print("\nReferal code exist")
            self.diskon = "4%"
        else:
            self.discount = 0
            self.diskon = "0%"
            print("\nReferal code not exist\n")
        
        self.final_price = self.harga - (self.harga*self.discount)
        return f"Harga yang perlu di bayarkan = {self.final_price}"

# ini supaya lebih interaktif pas di-Run
if __name__ == "__main__":
    nama_user = input("\nUsername : ").lower()
    current_plan_user = input("Plan yang ingin diambil (Basic, Standart, Premium): ").lower()
    durasi_user = int(input("Durasi anda telah berlangganan (dalam bulan): "))


    Type_user = New_user if nama_user not in daftar_user or durasi_user == 0 else User
    # Tujuan : buat nentuin pakai class User atau class New_user
    # maksud code ini kalau kamu input username selain yang ada di daftar_user(line 25) atau kamu input durasi-nya 0
    # maka dia bakal pakai class New_User

    user_1 = Type_user(nama_user, current_plan_user, durasi_user)
    # kenapa Pakai Type_user ? bukan User atau New_user ? seperti -> (user_1 = User(bla,bla....))
    # karena di variabel Type_User udah nenentuin makai class yang mana


    daftar_user.append(user_1.username) #abaikan ini
    print (f"\nUsername {user_1.username} telah memilih plan {user_1.current_plan} dengan diskon sebesar {user_1.diskon} sehingga total biaya sebesar Rp {user_1.final_price}\n")

    print (f"1. benefit yang anda dapatkan berupa resolusi {user_1.kualitas}")
    print (f"2. konten {user_1.content}")
    print( f"3. serta anda dapat menghubungkan akun anda ke {user_1.device} device\n")