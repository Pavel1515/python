class Purse():
	def __init__(self,valuta,course,name = "Uknow"):
		self.__money = 0.00
		self.valuta  = valuta
		self.course = course
		self.name = name

	def info(self):
		print(self.course , self.__money,self.valuta,self.name)

	def top_up_balance(self,howmany):
		self.__money = self.__money + howmany

	def top_down_balance(self,howmany):
		if self.__money - howmany < 0 :
			print("Не достаточно средств")
		else:
			self.__money = self.__money - howmany
	def transfer(self):
		self.__money * self.course
