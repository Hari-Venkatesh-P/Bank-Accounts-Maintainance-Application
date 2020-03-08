from tkinter import *
from tkinter import messagebox
import mysql.connector
import os 
from Account import Account

def closed(window):
	window.withdraw()
	screen = Tk()
	screen.title("Deposit Amount")
	screen.geometry("700x500")
	screen.configure(background='skyblue')
	i = 50
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	label_acc = Label(screen,text="Account Number").place(x=50,y=i)
	label_acc = Label(screen,text="Name").place(x=250,y=i)
	label_acc = Label(screen,text="Mobile Number").place(x=450,y=i)
	sql = "Select * from closed"
	cur.execute(sql)
	for line in cur:
		i+=50
		label_acc = Label(screen,text=line[0]).place(x=50,y=i)
		label_acc = Label(screen,text=line[1]).place(x=250,y=i)
		label_acc = Label(screen,text=line[2]).place(x=450,y=i)
	cur.close()
	con.close()
	window.deiconify()
	
def fd_report(window):
	window.destroy()
	screen = Tk()
	value_acc = StringVar()
	screen.title("FD Report")
	screen.geometry("350x300")
	screen.configure(background='skyblue')
	label_acc = Label(screen,text="Enter account number: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc).place(x=200,y=50)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: fd_report_action(value_acc.get()),width=20).place(x=50,y=100)
	screen.mainloop()
	main()
	
def fd_report_action(acc):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	screen2 = Tk()
	screen2.title("FD Report")
	screen2.geometry("600x300")
	screen2.configure(background='skyblue')
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	i=50
	label_acc = Label(screen2,text="Account Number").place(x=50,y=i)
	label_acc = Label(screen2,text="FD Amount").place(x=250,y=i)
	label_acc = Label(screen2,text="FD Term").place(x=450,y=i)	
	sql = "Select * from account where acc_no = '"+acc+"'"
	cur.execute(sql)
	for line in cur:
		i+=50
		label_acc = Label(screen2,text=line[0]).place(x=50,y=i)
		label_acc = Label(screen2,text=line[7]).place(x=250,y=i)
		label_acc = Label(screen2,text=line[8]).place(x=450,y=i)
	cur.close()
	con.close()	
	
def fd_report_vs(window):
	window.destroy()
	screen = Tk()
	value_acc1 = StringVar()
	value_acc2 = StringVar()
	screen.title("FD Report")
	screen.geometry("350x300")
	screen.configure(background='skyblue')
	label_acc = Label(screen,text="Enter 1st account no: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc1).place(x=200,y=50)
	label_acc = Label(screen,text="Enter 2nd account no: ").place(x=50,y=100)
	text_acc = Entry(screen,width=20,textvariable=value_acc2).place(x=200,y=100)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: fd_report_vs_action(value_acc1.get(),value_acc2.get()),width=20).place(x=50,y=150)
	screen.mainloop()
	main()

def fd_report_vs_action(acc1,acc2):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
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
	screen2 = Tk()
	screen2.title("FD Report")
	screen2.geometry("600x300")
	screen2.configure(background='skyblue')
	label_acc = Label(screen2,text="Account Number").place(x=50,y=50)
	label_acc = Label(screen2,text=acc1).place(x=250,y=50)
	label_acc = Label(screen2,text=acc2).place(x=450,y=50)
	label_acc = Label(screen2,text="Name").place(x=50,y=100)
	label_acc = Label(screen2,text=usr1[0]).place(x=250,y=100)
	label_acc = Label(screen2,text=usr2[0]).place(x=450,y=100)
	label_acc = Label(screen2,text="Balance").place(x=50,y=150)
	label_acc = Label(screen2,text=usr1[1]).place(x=250,y=150)
	label_acc = Label(screen2,text=usr2[1]).place(x=450,y=150)
	label_acc = Label(screen2,text="FD Amount").place(x=50,y=200)
	label_acc = Label(screen2,text=usr1[2]).place(x=250,y=200)
	label_acc = Label(screen2,text=usr2[2]).place(x=450,y=200)
	label_acc = Label(screen2,text="FD Term").place(x=50,y=250)
	label_acc = Label(screen2,text=usr1[3]).place(x=250,y=250)
	label_acc = Label(screen2,text=usr2[3]).place(x=450,y=250)
	cur.close()
	con.close()

def fd_report_range(window):
	window.destroy()
	screen = Tk()
	value_acc1 = StringVar()
	value_acc2 = StringVar()
	screen.title("FD Report")
	screen.geometry("350x300")
	screen.configure(background='skyblue')
	label_acc = Label(screen,text="Enter lower range: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc1).place(x=200,y=50)
	label_acc = Label(screen,text="Enter higher range: ").place(x=50,y=100)
	text_acc = Entry(screen,width=20,textvariable=value_acc2).place(x=200,y=100)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: fd_report_range_action(value_acc1.get(),value_acc2.get()),width=20).place(x=50,y=150)
	screen.mainloop()
	main()
	
def fd_report_range_action(low,up):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	sql = "select * from account"
	cur.execute(sql)
	screen2 = Tk()
	screen2.title("FD Report")
	screen2.geometry("900x700")
	screen2.configure(background='skyblue')
	label_acc = Label(screen2,text="Account Number").place(x=50,y=50)
	label_acc = Label(screen2,text="Name").place(x=250,y=50)
	label_acc = Label(screen2,text="FD Amount").place(x=450,y=50)
	label_acc = Label(screen2,text="FD Term").place(x=650,y=50)
	i = 50
	for line in cur:
		if(int(line[7]) < int(up) and int(line[7]) > int(low)):
			#print(i)
			i+=50
			label_acc = Label(screen2,text=line[0]).place(x=50,y=i)
			label_acc = Label(screen2,text=line[1]).place(x=250,y=i)
			label_acc = Label(screen2,text=line[7]).place(x=450,y=i)
			label_acc = Label(screen2,text=line[8]).place(x=650,y=i)	
	cur.close()
	con.close()

def loan_report(window):
	window.destroy()
	screen = Tk()
	value_acc = StringVar()
	screen.title("Loan Report")
	screen.geometry("350x300")
	screen.configure(background='skyblue')
	label_acc = Label(screen,text="Enter account number: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc).place(x=200,y=50)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: loan_report_action(value_acc.get()),width=20).place(x=50,y=100)
	screen.mainloop()
	main()

def loan_report_action(acc):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	screen2 = Tk()
	screen2.title("FD Report")
	screen2.geometry("600x300")
	screen2.configure(background='skyblue')
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	i=50
	label_acc = Label(screen2,text="Customer Name").place(x=50,y=i)
	label_acc = Label(screen2,text="Avail Balance").place(x=250,y=i)
	label_acc = Label(screen2,text="Loan Amount").place(x=450,y=i)	
	label_acc = Label(screen2,text="Loan Term").place(x=650,y=i)
	sql = "Select * from account where acc_no = '"+acc+"'"
	cur.execute(sql)
	for line in cur:
		i+=50
		label_acc = Label(screen2,text=line[1]).place(x=50,y=i)
		label_acc = Label(screen2,text=line[4]).place(x=250,y=i)
		label_acc = Label(screen2,text=line[5]).place(x=450,y=i)
		label_acc = Label(screen2,text=line[6]).place(x=650,y=i)
	cur.close()
	con.close()	

def loan_report_vs(window):
	window.destroy()
	screen = Tk()
	value_acc1 = StringVar()
	value_acc2 = StringVar()
	screen.title("Loan Report")
	screen.geometry("350x300")
	screen.configure(background='skyblue')
	label_acc = Label(screen,text="Enter 1st account no: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc1).place(x=200,y=50)
	label_acc = Label(screen,text="Enter 2nd account no: ").place(x=50,y=100)
	text_acc = Entry(screen,width=20,textvariable=value_acc2).place(x=200,y=100)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: loan_report_vs_action(value_acc1.get(),value_acc2.get()),width=20).place(x=50,y=150)
	screen.mainloop()
	main()

def loan_report_vs_action(acc1,acc2):
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
	screen2 = Tk()
	screen2.title("FD Report")
	screen2.geometry("600x300")
	screen2.configure(background='skyblue')
	label_acc = Label(screen2,text="Account Number").place(x=50,y=50)
	label_acc = Label(screen2,text=acc1).place(x=250,y=50)
	label_acc = Label(screen2,text=acc2).place(x=450,y=50)
	label_acc = Label(screen2,text="Name").place(x=50,y=100)
	label_acc = Label(screen2,text=usr1[0]).place(x=250,y=100)
	label_acc = Label(screen2,text=usr2[0]).place(x=450,y=100)
	label_acc = Label(screen2,text="Balance").place(x=50,y=150)
	label_acc = Label(screen2,text=usr1[1]).place(x=250,y=150)
	label_acc = Label(screen2,text=usr2[1]).place(x=450,y=150)
	label_acc = Label(screen2,text="Loan Amount").place(x=50,y=200)
	label_acc = Label(screen2,text=usr1[2]).place(x=250,y=200)
	label_acc = Label(screen2,text=usr2[2]).place(x=450,y=200)
	label_acc = Label(screen2,text="Loan Term").place(x=50,y=250)
	label_acc = Label(screen2,text=usr1[3]).place(x=250,y=250)
	label_acc = Label(screen2,text=usr2[3]).place(x=450,y=250)
	cur.close()
	con.close()
	
def loan_report_range(window):
	window.destroy()
	screen = Tk()
	value_acc1 = StringVar()
	value_acc2 = StringVar()
	screen.title("FD Report")
	screen.geometry("350x300")
	screen.configure(background='skyblue')
	label_acc = Label(screen,text="Enter lower range: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc1).place(x=200,y=50)
	label_acc = Label(screen,text="Enter higher range: ").place(x=50,y=100)
	text_acc = Entry(screen,width=20,textvariable=value_acc2).place(x=200,y=100)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: loan_report_range_action(value_acc1.get(),value_acc2.get()),width=20).place(x=50,y=150)
	screen.mainloop()
	main()
	
def loan_report_range_action(low,up):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	sql = "select * from account"
	cur.execute(sql)
	screen2 = Tk()
	screen2.title("FD Report")
	screen2.geometry("900x700")
	screen2.configure(background='skyblue')
	label_acc = Label(screen2,text="Account Number").place(x=50,y=50)
	label_acc = Label(screen2,text="Name").place(x=250,y=50)
	label_acc = Label(screen2,text="Loan Amount").place(x=450,y=50)
	label_acc = Label(screen2,text="Loan Term").place(x=650,y=50)
	i = 50
	for line in cur:
		if(int(line[5]) < int(up) and int(line[5]) > int(low)):
			print(i)
			i+=50
			label_acc = Label(screen2,text=line[0]).place(x=50,y=i)
			label_acc = Label(screen2,text=line[1]).place(x=250,y=i)
			label_acc = Label(screen2,text=line[5]).place(x=450,y=i)
			label_acc = Label(screen2,text=line[6]).place(x=650,y=i)	
	cur.close()
	con.close()

def not_availed_loan(window):
	window.destroy()
	screen = Tk()
	screen.title("Loan Report")
	screen.geometry("600x600")
	screen.configure(background='skyblue')
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	sql = "select * from account where loan_availed='0'"
	cur.execute(sql)
	i = 50
	label_acc = Label(screen,text="Account Number").place(x=50,y=50)
	label_acc = Label(screen,text="Name").place(x=250,y=50)
	label_acc = Label(screen,text="Mobile No").place(x=450,y=50)
	for line in cur:
		i += 50
		label_acc = Label(screen,text=line[0]).place(x=50,y=i)
		label_acc = Label(screen,text=line[1]).place(x=250,y=i)
		label_acc = Label(screen,text=line[3]).place(x=450,y=i)
	cur.close()
	con.close()
	screen.mainloop()
	main()

def log_out(window):
	window.destroy()

def main():
	window = Tk()
	window.title("Admin Login")
	window.geometry("700x400")
	window.configure(background='skyblue')
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	sql = "select count(acc_no) from account"
	cur.execute(sql)
	msg = ""
	for line in cur:
		msg = line[0]
	msg = "No. of accounts in the bank: "+str(msg) 
	label_acc = Label(text=msg).place(x=50,y=50)
	button_login = Button(text="Closed Account Report",command = lambda: closed(window),width=30).place(x=50,y=100)
	button_login = Button(text="Customer FD Report",command = lambda: fd_report(window),width=30).place(x=350,y=100)
	button_login = Button(text="Customer FD Report vs Another",command = lambda: fd_report_vs(window),width=30).place(x=50,y=150)
	button_login = Button(text="FD Report w.r.t amount",command = lambda: fd_report_range(window),width=30).place(x=350,y=150)
	button_login = Button(text="Customer Loan Report",command = lambda: loan_report(window),width=30).place(x=50,y=200)
	button_login = Button(text="Customer Loan Report vs Another",command = lambda: loan_report_vs(window),width=30).place(x=350,y=200)
	button_login = Button(text="Loan Report w.r.t amount",command = lambda: loan_report_range(window),width=30).place(x=50,y=250)
	button_login = Button(text="Customers not availed loan",command = lambda: not_availed_loan(window),width=30).place(x=350,y=250)
	button_login = Button(text="LOGOUT",command = lambda: log_out(window),width=30).place(x=200,y=300)
	window.mainloop()
main()