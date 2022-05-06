class Authorization():



    
    def __init__(self , login = "Uknow"):
        pass
        
    def new_login(self):
        self.login = input("Введіть логін ")
        
                 

    def info(self):
        print(self.login)



c = Authorization()
c.new_login()
c.info()