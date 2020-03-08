import mysql.connector
import os
from Account import Account
file = open("temp.txt","r")
acc = ""
temp = 1
for line in file:
	if(acc != " "):
		acc = line
if(acc != 'admin'):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor() 
	sql = "select * from account where acc_no='"+acc+"';"
	cur.execute(sql)
	a = Account()
	for line in cur:
		print("Account Number: \t"+line[0])
		print("Account Holder Name: \t"+line[1])
		print("Type of Account: \t"+line[2])
		print("Personal Mobile number: "+line[3])
		print("Current Balance: \t"+line[4])
		a.set_data(line[0],line[1],line[2],line[3],line[4])
	cur.close()
	con.close()
		
	while(temp != 0):
			print("1.Deposit Amount\n2.Withdraw Amount\n3.Transfer Funds\n4.Balance Enquiry\n5.Mobile Number Change\n6.Avail Loan\n7.Account Closure\n8.LogOut\nEnter your choice")
			choice = int(input())
			if(choice == 1):
				con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
				cur = con.cursor()
				print("Enter the amount to be deposited: ")
				amount = int(input())
				a.deposit(amount)
				sql = "update account set balance = %s where acc_no = %s"
				cur.execute(sql,(b.get_balance(),account))
				cur.close()
				con.commit()
				con.close()
			elif(choice == 2):
				con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
				cur = con.cursor()
				print("Enter the amount to withdraw: ")
				amount = int(input())
				a.withdraw(amount)
				sql = "update account set balance = %s where acc_no = %s"
				cur.execute(sql,(b.get_balance(),account))
				cur.close()
				con.commit()
				con.close()
			elif(choice == 3):
				print("Enter the account number to which the funds to be transfered: ")
				account = input()
				print("Enter the amount to be transferred: ")
				amt = int(input())
				if(int(a.get_balance()) < amt):
					print("You have insufficient funds to do the transfer.")
				else:
					con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
					cur = con.cursor()
					sql = "select * from account where acc_no ='"+account+"'"
					cur.execute(sql)
					b = Account()
					for line in cur:
						b.set_data(line[0],line[1],line[2],line[3],line[4])
					a.transfer(amt,b)
					print("Other Bal:"+b.get_balance(),account)
					#sql = "update account set balance='"+b.get_balance()+"' where acc_no='"+account+"';"
					sql = "update account set balance = %s where acc_no = %s"
					cur.execute(sql,(b.get_balance(),account))
					sql = "update account set balance = %s where acc_no = %s"
					cur.execute(sql,(a.get_balance(),acc))
					if(cur.rowcount == 1):
						print("Transaction Succesful")
					else:
						print("Transaction failed")
					cur.close()
					con.commit()
					con.close()
			elif(choice == 4):
				print(a.get_balance())
			elif(choice == 5):
				con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
				cur = con.cursor()
				print("Enter the new mobile number to be updated: ")
				mob = input()
				sql = "update account set mobile = %s where acc_no = %s"
				cur.execute(sql,(mobile,account))
				if(cur.rowcount==1):
					print("Mobile Number Succesfully")
				cur.close()
				con.close()
			elif(choice == 6):
				con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
				cur = con.cursor()
				print("Enter the loan amount required: ")
				loan_amt = int(input())
				if(loan_amt < 2*int(a.get_balance()) and loan_amt > 0 and loan_amt%1000 == 0):
					print("Enter the Repayment Term (in months) :")
					mon = int(input())
					if(mon > 0):
						print("Your loan application is accepted")
						sql = "update account set loan_availed='"+str(loan_amt)+"', lrepay_term='"+str(mon)+"' where acc_no='"+a.get_acc_no()+"'"
						cur.execute(sql)
						cur.close()
						con.close()
				else:
					print("You are not eligible for the loan")
			elif(choice == 7):
				print("Enter your account number to close your account: ")
				ac = int(input())
				if(int(a.get_acc_no()) == ac):
					con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
					cur = con.cursor()
					sql = "delete from account where acc_no='"+str(ac)+"'"
					cur.execute(sql)
					sql = "delete from login where id='"+str(ac)+"'"
					cur.execute(sql)
					sql = "Insert into closed values('"+a.get_acc_no()+"','"+a.get_name()+"','"+a.get_mobile()+"')"
					cur.execute(sql)
					print("Your Account is Closed. Thank You for your Support.\nThe current balance: "+a.get_balance()+" will be sent to your registered address.")
					cur.close()
					con.commit()
					con.close()
				temp = 0
			elif(choice == 8):
				temp = 0
			else:
				print("You have entered an incorrect option.")

if(acc == 'admin'):
	os.system('python admin.py')