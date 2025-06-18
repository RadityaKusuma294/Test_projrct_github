daftar_user = ["umi"]

class User :
    def __init__ (self, username, current_plan, duration_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan
        self.discount = 0
        self.harga = 0
        self.final_cost_plan()
        print("\nAnda adalah user lama")
    
    def check_benefit (self):
        self.dict_harga_plan = {"basic" : 120000, "standart": 160000, "premium":200000 }
        self.kualitas = ["SD", "HD", "UHD"]
        self.content = ["3rd party movie", "Sport(Football/Soccer, F1, Basketball)", "Pacflix Original Series/Movies"]
        self.download = True
        self.device = [1, 2, 4]

        if self.current_plan.lower() == "basic":
            self.kualitas = self.kualitas[0]
            self.content = self.content[0]
            self.download = self.download
            self.harga = self.dict_harga_plan["basic"]
            self.device = self.device[0]
        
        elif self.current_plan.lower() == "standart":
            self.kualitas = self.kualitas[0:2]
            self.content = self.content[0:2]
            self.download = self.download
            self.harga = self.dict_harga_plan["standart"]
            self.device = self.device[1]
        
        elif self.current_plan.lower() == "premium":
            self.kualitas = self.kualitas[0:]
            self.content = self.content[0:]
            self.download = self.download
            self.harga = self.dict_harga_plan["premium"]
            self.device = self.device[2]
        else :
            raise TypeError ("masukkan nama plan dengan benar")
    
        
        return f"benefityang anda dapatkan berupa resolusi {self.kualitas} dengan konten {self.content}, serta anda dapat menghubungkan akun anda ke {self.device} device berbeda"
        
    
    def check_plan (self, username):
        return f"username {self.username} saat ini berlangganan {self.current_plan} selama {self.duration_plan}"
    
    def final_cost_plan (self):
        self.current_plan
        self.check_benefit()
        self.harga = self.dict_harga_plan[self.current_plan]
        if self.duration_plan > 12:
            self.discount = 0.05
            self.diskon = "5%"
        else:
            self.discount = 0
        
        self.final_price = self.harga - (self.harga*self.discount)
        return f"Harga yang perlu di bayarkan = {self.final_price}"
    


class New_user :
    def __init__ (self, username, pick_plan,duration_plan ):
        self.duration_plan = duration_plan
        self.current_plan = pick_plan
        self.username = username
        self.referal_code = input("karana anda user baru masukkan referal code: ")
        self.final_cost_plan()
    
    def check_benefit (self):
        self.dict_harga_plan = {"basic" : 120000, "standart": 160000, "premium":200000 }
        self.kualitas = ["SD", "HD", "UHD"]
        self.content = ["3rd party movie", "Sport(Football/Soccer, F1, Basketball)", "Pacflix Original Series/Movies"]
        self.download = True
        self.device = [1, 2, 4]
        try :

            if self.current_plan.lower() == "basic":
                self.kualitas = self.kualitas[0]
                self.content = self.content[0]
                self.download = self.download
                self.harga = self.dict_harga_plan["basic"]
                self.device = self.device[0]
            
            elif self.current_plan.lower() == "standart":
                self.kualitas = self.kualitas[0:2]
                self.content = self.content[0:2]
                self.download = self.download
                self.harga = self.dict_harga_plan["standart"]
                self.device = self.device[1]
            
            elif self.current_plan.lower() == "premium":
                self.kualitas = self.kualitas[0:]
                self.content = self.content[0:]
                self.download = self.download
                self.harga = self.dict_harga_plan["premium"]
                self.device = self.device[2]
            else :
                raise ValueError ("masukkan nama plan dengan benar")
        except :
            ValueError
        
        return f"benefit yang anda dapatkan berupa resolusi {self.kualitas} dengan konten {self.content}, serta anda dapat menghubungkan akun anda ke {self.device} device berbeda"
        
    
    def final_cost_plan (self):
        list_referal = ["PacflixHemat", "PacflixExpo", "Pacflix123", "BPANDA"]
        self.check_benefit()
        self.harga = self.dict_harga_plan[self.current_plan]
        if self.referal_code in list_referal:
            self.discount = 0.04
            print("\nReferal code exist")
            self.diskon = "4%"
        else:
            self.discount = 0
            print("\nReferal code not exist\n")
        
        self.final_price = self.harga - (self.harga*self.discount)
        return f"Harga yang perlu di bayarkan = {self.final_price}"


nama_user = input("\nUsername : ").lower()
current_plan_user = input("Plan yang ingin diambil (Basic, Standart, Permium): ").lower()
durasi_user = int(input("Durasi anda telah berlangganan (dalam bulan): "))

Type_user = New_user if nama_user not in daftar_user or durasi_user == 0 else User

user_1 = Type_user(nama_user, current_plan_user, durasi_user)
daftar_user.append(user_1)
print (f"\nUsername {user_1.username} telah memilih plan {user_1.current_plan} dengan diskon sebesar {user_1.diskon} sehingga total biaya sebesar Rp {user_1.final_price}\n")

print (f"1. benefit yang anda dapatkan berupa resolusi {user_1.kualitas}")
print (f"2. konten {user_1.content}")
print( f"3. serta anda dapat menghubungkan akun anda ke {user_1.device} device\n")