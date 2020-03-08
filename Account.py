class Account:
	def __init__(self,a="",b="",c="",d="",e=""):
		self.acc_no = a
		self.name = b
		self.type = c
		self.mobile = d
		self.balance = e
	
	def set_data(self,a,b,c,d,e):
		self.acc_no = a
		self.name = b
		self.type = c
		self.mobile = d
		self.balance = e
	
	def get_balance(self):
		return self.balance
	
	def get_acc_no(self):
		return self.acc_no
	
	def get_mobile(self):
		return self.mobile

	def get_name(self):
		return self.name
		
	def deposit(self,amt):
		temp = int(self.balance)
		temp += amt
		self.balance = str(temp)
	
	def withdraw(self,amt):
		temp = int(self.balance)
		temp -= amt
		self.balance = str(temp)
		
	def transfer(self,amt,c):
		self.withdraw(amt)
		c.deposit(amt)
		