from Account import Account
import mysql.connector
temp = 1
while(temp != 0):
	print("#########################HARI BANK#########################")
	print("1.Closed Accounts Report\n2.Customer FD Report\n3.Customer FD Report vs Another\n4.FD Report w.r.t amount\n5.Customer Loan Report\n6.Customer Loan Report vs Another\n7.Loan Report w.r.t amount\n8.Report of Customers not availed loan\n9.Logout\nEnter your choice: ")
	choice = int(input())
	print()
	if(choice == 1):
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		print("Account No\tName\tMobile Number")
		sql = "Select * from closed"
		cur.execute(sql)
		for line in cur:
			print(line[0]+"\t"+line[1]+"\t"+line[2])
		print()
		cur.close()
		con.close()
	elif(choice == 2):
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		print("Enter the Account number: ")
		acc = input()
		print("Accoutn No\tFD Amount\tFD Term")
		sql = "Select * from account where acc_no = '"+acc+"'"
		cur.execute(sql)
		for line in cur:
			print(line[0]+"\t"+line[7]+"\t"+line[8])
		cur.close()
		con.close()
	elif(choice == 3):
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		print("Enter the first customer's account number: ")
		acc1 = input()
		print("enter the second customer's account number: ")
		acc2 = input()
		sql = "select * from account where acc_no = '"+acc1+"'"
		usr1 = []
		usr2 = []
		cur.execute(sql)
		for line in cur:
			usr1.append(line[1])
			usr1.append(line[4])
			usr1.append(line[7])
			usr1.append(line[8])
		sql = "select * from account where acc_no = '"+acc2+"'"
		cur.execute(sql)
		for line in cur:
			usr2.append(line[1])
			usr2.append(line[4])
			usr2.append(line[7])
			usr2.append(line[8])
		print("Account No\t"+acc1+"\t"+acc2)
		print("Name\t\t"+usr1[0]+"\t"+usr2[0])
		print("Balance\t"+usr1[1]+"\t"+usr2[1])
		print("FD Amt\t"+usr1[2]+"\t"+usr2[2])
		print("FD Term\t"+usr1[3]+"\t"+usr2[3])
		cur.close()
		con.close()
	elif(choice == 4):
		print("Enter the lower range: ")
		low = int(input())
		print("enter the upper range: ")
		up = int(input())
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "select * from account"
		cur.execute(sql)
		print("Account No\tName\tFD Amount\tFD Term")
		for line in cur:
			if(int(line[7]) < up and int(line[7]) > low):
				print(line[0]+"\t\t"+line[1]+"\t"+line[7]+"\t\t"+line[8])
		cur.close()
		con.close()
	elif(choice == 5):
		print("Enter the Account number: ")
		acc = input()
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "select * from account where acc_no = '"+acc+"'"
		cur.execute(sql)
		for line in cur:
			print("Name of the Customer: "+line[1])
			print("Current Available Balance:"+line[4])
			print("Loan Amount yet to be paid:"+line[5])
			print("Loan Repay Term in months: "+line[6])
		cur.close()
		con.close()
	elif(choice == 6):
		print("Enter the first customer's account number: ")
		acc1 = input()
		print("enter the second customer's account number: ")
		acc2 = input()
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "select * from account where acc_no = '"+acc1+"'"
		usr1 = []
		usr2 = []
		cur.execute(sql)
		for line in cur:
			usr1.append(line[1])
			usr1.append(line[4])
			usr1.append(line[5])
			usr1.append(line[6])
		sql = "select * from account where acc_no = '"+acc2+"'"
		cur.execute(sql)
		for line in cur:
			usr2.append(line[1])
			usr2.append(line[4])
			usr2.append(line[5])
			usr2.append(line[6])
		print("Account No\t"+acc1+"\t"+acc2)
		print("Name\t\t"+usr1[0]+"\t"+usr2[0])
		print("Balance\t"+usr1[1]+"\t"+usr2[1])
		print("Loan Amt\t"+usr1[2]+"\t"+usr2[2])
		print("Repay Term\t"+usr1[3]+"\t"+usr2[3])
		cur.close()
		con.close()
	elif(choice == 7):
		print("Enter the lower range: ")
		low = int(input())
		print("enter the upper range: ")
		up = int(input())
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "select * from account"
		cur.execute(sql)
		print("Account No\tName\tLoan Availed\tLoan Repay Term")
		for line in cur:
			if(int(line[5]) < up and int(line[5]) > low):
				print(line[0]+"\t\t"+line[1]+"\t"+line[5]+"\t\t"+line[6])
		cur.close()
		con.close()
	elif(choice == 8):
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "select * from account where loan_availed='0'"
		cur.execute(sql)
		print("Account No\tName\tMobile Number")
		for line in cur:
			print(line[0]+"\t\t"+line[1]+"\t"+line[3])
		cur.close()
		con.close()
	elif(choice == 9):
		temp = 0