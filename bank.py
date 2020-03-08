from tkinter import *
from tkinter import messagebox
import tkinter
import mysql.connector
import os 
window = Tk()
window.title("HARI BANK")
window.geometry("500x500")
#window.wm_iconbitmap('icon.ico')
window.configure(background='skyblue')


#background_image=tkinter.PhotoImage('icon.jpg')
#background_label = tkinter.Label(image=background_image)
#background_label.place(x=0, y=0, relwidth=100, relheight=100)


value_usr = StringVar()
value_pass = StringVar()

def log_in():
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor() 
	sql = "select password from login where id = '"+value_usr.get()+"'"
	cur.execute(sql)
	for row in cur:
		if(row[0] == value_pass.get()):
			file = open("temp.txt","w")
			file.write(value_usr.get())
			file.close()
			cur.close()
			con.close()
			messagebox.showinfo(title='Login',message="Login Succesful")
			window.destroy()
			os.system('python operation_form.py')
			#os.system('python operations.py')
		else:
			messagebox.showinfo(title='Login',message='Login Failed')			
	
	
	
def sign_up():
	window.destroy()
	screen = Tk()
	screen.title("Sign Up")
	screen.geometry("500x500")
	screen.configure(background='skyblue')
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur = con.cursor()
	sql = "select acc_no from account"
	cur.execute(sql)
	max = '0'
	for line in cur:
		if(int(max) < int(line[0])):
			max = line[0]
	value_type = StringVar()
	value_acc = StringVar()
	value_name = StringVar() 
	value_type =  StringVar()
	value_mobile = StringVar()
	value_password = StringVar()
	value_fdamount = StringVar(0)
	value_fdterm = StringVar(0)
	max = str(int(max) + 1)
	value_acc.set(max)
	value_fdamount.set(0)
	value_fdterm.set(0)
	label_acc = Label(text="Account Number").place(x=50,y=50)
	text_acc = Entry(width=20,textvariable=value_acc).place(x=150,y=50)
	label_name = Label(text="Customer Name").place(x=50,y=100)
	text_name = Entry(width=20,textvariable=value_name).place(x=150,y=100)
	label_type = Label(text="Account Type").place(x=50,y=150)
	text_type = Entry(width=20,textvariable=value_type).place(x=150,y=150)
	label_mobile = Label(text="Mobile Numer").place(x=50,y=200)
	text_mobile = Entry(width=20,textvariable=value_mobile).place(x=150,y=200)
	label_pass = Label(text="Password").place(x=50,y=250)
	text_pass = Entry(width=20,show="*",textvariable=value_password).place(x=150,y=250)
	label_pass = Label(text="FD Amount").place(x=50,y=300)
	text_fdamount = Entry(width=20,textvariable=value_fdamount).place(x=150,y=300)
	label_pass = Label(text="Enter if only type is FD").place(x=250,y=300)
	label_pass = Label(text="FD Term").place(x=50,y=350)
	text_fdterm = Entry(width=20,textvariable=value_fdterm).place(x=150,y=350)
	label_pass = Label(text="Enter if only type is FD").place(x=250,y=350)
	button_SignUp = Button(text="SIGN UP",command = lambda: sign_db(value_acc.get(),value_name.get(),value_type.get(),value_mobile.get(),value_password.get(),value_fdamount.get(),value_fdterm.get())).place(x=175,y=400)
	screen.mainloop()
	file = open("temp.txt","w")
	file.write(value_acc.get())
	file.close()
	os.system('python operation_form.py')
	#os.system('python operations.py')
	
def sign_db(a,b,c,d,e,f,g):
	con = mysql.connector.connect(host="localhost", user="root", password="", database="bank")
	cur1 = con.cursor()
	cur2 = con.cursor()
	balance = 1000
	sql1 = "insert into account(acc_no,name,type,mobile,balance,fd_amount,deposit_term) values('"+a+"','"+b+"','"+c+"','"+d+"','1000','"+f+"','"+g+"')"
	cur1.execute(sql1)
	print(cur1.rowcount)
	sql2 = "insert into login values('"+a+"','"+e+"')"
	cur2.execute(sql2)
	if(cur1.rowcount and cur2.rowcount):
		temp = 1
	cur1.close()
	cur2.close()
	con.commit()
	con.close()
	if(temp == 1):
		messagebox.showinfo(title='Login',message='Sign Up Succesful')
	else:
		messagebox.showinfo(title='Login',message='Sign Up Failed')
	

label_usr = Label(text="User Name").place(x=50,y=50)
text_usr = Entry(width=20,textvariable=value_usr).place(x=150,y=50)
label_pass = Label(text="Password").place(x=50,y=100)
text_pass = Entry(width=20,show="*",textvariable=value_pass).place(x=150,y=100)

button_login = Button(text="LOG IN",command = log_in).place(x=175,y=150)
button_signup = Button(text="Sign UP",command = sign_up).place(x=175,y=185)
#os.system('python filename.py')
window.mainloop()