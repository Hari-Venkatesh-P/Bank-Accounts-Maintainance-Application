from tkinter import *
from tkinter import messagebox
import mysql.connector
import os 
from Account import Account

file = open("temp.txt","r")
acc = ""
for line in file:
	if(acc != " "):
		acc = line

	
def deposit(window,a):
	window.destroy()
	screen = Tk()
	screen.title("Deposit Amount")
	screen.geometry("300x300")
	screen.configure(background='skyblue')
	value_amt = StringVar()
	screen.label_acc = Label(text="Enter amount").place(x=50,y=50)
	screen.text_acc = Entry(width=20,textvariable=value_amt).place(x=150,y=50)
	screen.button_login = Button(text="Deposit",command = lambda: deposit_2(value_amt.get(),a),width=20).place(x=50,y=100)
	screen.mainloop()
	main()
	
def deposit_2(amt,a):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	#print(amt)
	a.deposit(int(amt))
	sql = "update account set balance = %s where acc_no = %s"
	cur.execute(sql,(a.get_balance(),acc))
	messagebox.showinfo(title='Login',message='Amount Deposited Succesfully')
	cur.close()
	con.commit()
	con.close()

def withdraw(window,a):
	window.destroy()
	screen = Tk()
	screen.title("Withdraw Amount")
	screen.geometry("300x300")
	screen.configure(background='skyblue')
	value_amt = StringVar()
	screen.label_acc = Label(text="Enter amount").place(x=50,y=50)
	screen.text_acc = Entry(width=20,textvariable=value_amt).place(x=150,y=50)
	screen.button_login = Button(text="withdraw",command = lambda: withdraw_2(value_amt.get(),a),width=20).place(x=50,y=100)
	screen.mainloop()
	main()

def withdraw_2(amt,a):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	#print(amt)
	a.withdraw(int(amt))
	sql = "update account set balance = %s where acc_no = %s"
	cur.execute(sql,(a.get_balance(),acc))
	messagebox.showinfo(title='Login',message='Amount Withdrawal Succesfull')
	cur.close()
	con.commit()
	con.close()

def transfer(window,a):
	window.destroy()
	screen = Tk()
	screen.title("Transfer Funds")
	screen.geometry("400x400")
	screen.configure(background='skyblue')
	value_amt = StringVar()
	value_acc = StringVar()
	screen.label_acc = Label(text="Enter account to which transfer").place(x=50,y=50)
	screen.text_acc = Entry(width=20,textvariable=value_acc).place(x=250,y=50)
	screen.label_amt = Label(text="Enter amt").place(x=50,y=100)
	screen.text_acc = Entry(width=20,textvariable=value_amt).place(x=250,y=100)
	screen.button_login = Button(text="Transfer",command = lambda: transfer_2(value_acc.get(),value_amt.get(),a),width=20).place(x=50,y=150)
	screen.mainloop()
	main()

def transfer_2(acc,amt,a):
	if(int(a.get_balance()) < int(amt)):
		messagebox.showinfo(title='Transfer',message='You have insufficient funds')
	else:
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "select * from account where acc_no ='"+acc+"'"
		cur.execute(sql)
		b = Account()
		for line in cur:
			b.set_data(line[0],line[1],line[2],line[3],line[4])
			a.transfer(int(amt),b)
			#sql = "update account set balance='"+b.get_balance()+"' where acc_no='"+account+"';"
			sql = "update account set balance = %s where acc_no = %s"
			cur.execute(sql,(b.get_balance(),acc))
			sql = "update account set balance = %s where acc_no = %s"
			cur.execute(sql,(a.get_balance(),a.get_acc_no()))
			if(cur.rowcount == 1):
				messagebox.showinfo(title='Transfer',message='Transaction Succesful')
			else:
				messagebox.showinfo(title='Transfer',message='Transaction Failed')
		cur.close()
		con.commit()
		con.close()

def mobile_change(window,a):
	window.destroy()
	screen = Tk()
	screen.title("Transfer Funds")
	screen.geometry("300x300")
	screen.configure(background='skyblue')
	value_mob = StringVar()
	screen.label_acc = Label(text="New mobile:").place(x=50,y=50)
	screen.text_acc = Entry(width=20,textvariable=value_mob).place(x=150,y=50)
	screen.button_login = Button(text="change",command = lambda: mobile_change_2(value_mob.get(),a),width=20).place(x=50,y=100)
	screen.mainloop()
	main()
	
def mobile_change_2(mob,a):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	sql = "update account set mobile = %s where acc_no = %s"
	cur.execute(sql,(mob,a.get_acc_no()))
	if(cur.rowcount==1):
		messagebox.showinfo(title='Update',message='Mobile number updated succesfully')
	cur.close()
	con.close()
	
def avail_loan(window,a):
	window.destroy()
	screen = Tk()
	screen.title("Avail Loan")
	screen.geometry("300x300")
	screen.configure(background='skyblue')
	value_amt = StringVar()
	value_term = StringVar()
	screen.label_acc = Label(text="Enter amount:").place(x=50,y=50)
	screen.text_acc = Entry(width=20,textvariable=value_amt).place(x=150,y=50)
	screen.label_acc = Label(text="Repayment Term:").place(x=50,y=100)
	screen.text_acc = Entry(width=20,textvariable=value_term).place(x=150,y=100)
	screen.button_login = Button(text="Apply for Loan",command = lambda: avail_loan_2(value_amt.get(),value_term.get(),a),width=20).place(x=50,y=150)
	screen.mainloop()
	main()

def avail_loan_2(amt,mon,a):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	if(int(amt) < 2*int(a.get_balance()) and int(amt) > 0 and int(amt)%1000 == 0):
		if(int(mon) > 0):
			sql = "update account set loan_availed='"+amt+"', lrepay_term='"+mon+"' where acc_no='"+a.get_acc_no()+"'"
			cur.execute(sql)
			cur.close()
			con.commit()
			con.close()
			messagebox.showinfo(title='Loan',message='Your loan application is accepted.')
	else:
		print("You are not eligible for the loan")

def closure(window,a):
	window.destroy()
	screen = Tk()
	screen.title("Account Close")
	screen.geometry("300x300")
	screen.configure(background='skyblue')
	value_acc = StringVar()
	screen.label_acc = Label(text="Enter your account number:").place(x=50,y=50)
	screen.text_acc = Entry(width=20,textvariable=value_acc).place(x=200,y=50)
	screen.button_login = Button(text="Close Account",command = lambda: closure_2(value_acc.get(),a),width=20).place(x=50,y=150)
	screen.mainloop()

def closure_2(ac,a):
	if(int(a.get_acc_no()) == int(ac)):
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor()
		sql = "delete from account where acc_no='"+ac+"'"
		cur.execute(sql)
		sql = "delete from login where id='"+ac+"'"
		cur.execute(sql)
		sql = "Insert into closed values('"+a.get_acc_no()+"','"+a.get_name()+"','"+a.get_mobile()+"')"
		cur.execute(sql)
		msg = "Your account is closed. thank you for your support.\nYour available balance: "+a.get_balance()+" will be sent to your registered home address"
		messagebox.showinfo(title='Close',message=msg)
		cur.close()
		con.commit()
		con.close()

	
def log_out(window):
	window.destroy()
	
def balance(a):
	messagebox.showinfo(title='Login',message="Balance: "+a.get_balance())
	
def main():
	window = Tk()
	window.title("User Details")
	window.geometry("700x600")
	window.configure(background='skyblue')
	value_acc = StringVar()
	value_name = StringVar() 
	value_type =  StringVar()
	value_mobile = StringVar()
	value_balance =  StringVar()
	label_acc = Label(text="Account Number").place(x=50,y=50)
	text_acc = Entry(width=20,textvariable=value_acc).place(x=150,y=50)
	label_name = Label(text="Name").place(x=50,y=100)
	text_acc = Entry(width=20,textvariable=value_name).place(x=150,y=100)
	label_type = Label(text="Account Type").place(x=50,y=150)
	text_acc = Entry(width=20,textvariable=value_type).place(x=150,y=150)
	label_mobile = Label(text="Mobile Number").place(x=50,y=200)
	text_acc = Entry(width=20,textvariable=value_mobile).place(x=150,y=200)
	label_balance = Label(text="Current Balance").place(x=50,y=250)
	text_acc = Entry(width=20,textvariable=value_balance).place(x=150,y=250)
	button_login = Button(text="Deposit Amount",command = lambda: deposit(window,a),width=20).place(x=50,y=300)
	button_login = Button(text="Withdraw Amount",command = lambda: withdraw(window,a),width=20).place(x=250,y=300)
	button_login = Button(text="Transfer Funds",command = lambda: transfer(window,a),width=20).place(x=50,y=350)
	button_login = Button(text="Balance Enquiry",command = lambda: balance(a),width=20).place(x=250,y=350)
	button_login = Button(text="Mobile number Change",command = lambda: mobile_change(window,a),width=20).place(x=50,y=400)
	button_login = Button(text="Avail Loan",command = lambda: avail_loan(window,a),width=20).place(x=250,y=400)
	button_login = Button(text="Account Closure",command = lambda: closure(window,a),width=20).place(x=50,y=450)
	button_login = Button(text="LOG OUT",command = lambda: log_out(window),width=20).place(x=250,y=450)
	if(acc != 'admin'):
		con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
		cur = con.cursor() 
		sql = "select * from account where acc_no='"+acc+"';"
		cur.execute(sql)
		a = Account()
		for line in cur:
			value_acc.set(line[0])
			value_name.set(line[1])
			value_type.set(line[2])
			value_mobile.set(line[3])
			value_balance.set(line[4])
			a.set_data(line[0],line[1],line[2],line[3],line[4])
		cur.close()
		con.close()
	window.mainloop()
if(acc != 'admin'):
	main()
if(acc == 'admin'):
	os.system('python admin_form.py') 