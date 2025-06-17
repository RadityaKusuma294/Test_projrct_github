class User :
    def __init__ (self, username, current_plan, duration_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan
    
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
        
        return f"benefityang anda dapatkan berupa resolusi {self.kualitas} dengan konten {self.content}, serta anda dapat menghubungkan akun anda ke {self.device} device berbeda"
        
    
    def check_plan (self, username):
        return f"username {self.username} saat ini berlangganan {self.current_plan} selama {self.duration_plan}"
    
    def upgrade_plan (self, new_plan):
        self.current_plan = new_plan.lower()
        self.check_benefit()
        self.harga = self.dict_harga_plan[self.current_plan]
        if self.duration_plan > 12:
            self.discount = 0.05
        else:
            self.discount = 0
        
        self.final_price = self.harga - (self.harga*self.discount)
        return f"Harga yang perlu di bayarkan = {self.final_price}"
    


class New_user :
    def __init__ (self, username):
        self.username = username
    
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
        
        return f"benefityang anda dapatkan berupa resolusi {self.kualitas} dengan konten {self.content}, serta anda dapat menghubungkan akun anda ke {self.device} device berbeda"
        
    
    def pick_plan (self, pick_plan, referal_code):
        list_referal = ["PacflixHemat", "PacflixExpo", "Pacflix123"]
        self.current_plan = pick_plan.lower()
        self.check_benefit()
        self.harga = self.dict_harga_plan[self.current_plan]
        if referal_code in list_referal:
            self.discount = 0.04
            print("Referal code exist")
        else:
            self.discount = 0
            print("Referal code not exist")
        
        self.final_price = self.harga - (self.harga*self.discount)
        return f"Harga yang perlu di bayarkan = {self.final_price}"

# myuser = User("andi", "Basic", 13 )

# print(myuser.check_plan("andi"))
# print(myuser.check_benefit())
# print(f"{myuser.upgrade_plan("Premium")}\n")
# print(myuser.check_benefit())

newuser = New_user("Raka")
print(newuser.pick_plan("Basic", "rakakecil"))
        

