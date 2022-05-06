class Purse():
	def __init__(self,valuta,course,name = "Uknow"):
		self._money = 0.00
		self.valuta  = valuta
		self.course = course
		self.name = name


	def info(self):
		print(self.course , self._money,self.valuta,self.name)

	def top_up_balance(self,howmany):
		self._money = self._money + howmany

	def top_down_balance(self,howmany):
		if self._money - howmany < 0 :
			print("Не достаточно средств")
		else:
			self._money = self.money - howmany
	def transfer(self):
		self._money * self.course
