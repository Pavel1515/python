from Purse import Purse

class V2(Purse):
    def save(self):
        with open("money.txt", "a") as r:
            r.write(str(self.money) +"\n")
    def __init__(self,valuta,course,name="Uknow"):
        Purse.__init__(self,valuta,course,name)



c  = V2("USD", 9,"Pavlo" )
c.top_up_balance(1000) 
c.info()