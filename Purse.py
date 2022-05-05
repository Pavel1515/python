class Purse():
	def __init__(self,valuta,course,name = "Uknow" ):
		self.money = 0.00
		self.valuta  = valuta
		self.name = name
		self.course = course
	def info(self):
		print(self.money ,self.valuta ,"Курс " ,self.course,"+")

	def top_up_balance(self,howmany):
		self.money = self.money + howmany

	def top_down_balance(self,howmany):
		if self.money - howmany < 0 :
			print("Не достаточно средств")
		else:
			self.money = self.money - howmany
	def transfer(self):
		self.money * self.course