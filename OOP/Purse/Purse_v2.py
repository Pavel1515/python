from Purse import Purse

class V2(Purse):
    def save(self):
        with open("money.txt" , "a") as r:
            r.write(self.name + " " +str(self._money) + "\n")


c  = V2("USD", 9,'Pavlo')
c.top_up_balance(1000) 
c.info()
c.save()
