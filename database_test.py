import pymysql
from tkinter import *
from tkinter import messagebox

def search():
	try:
		con = pymysql.connect(user='root', password ='admin',\
			host = 'localhost',database ='db')
		cur = con.cursor()
		sql ="select * from student where id_number = '%s'"%id_number.get()
		cur.execute(sql)
		result =cur.fetchone()
		name.set(result[1])
		age.set(result[2])
		e1.configure(state='disable')
		con.close()
	except:
		messagebox.showinfo('No Data','No such data exist...')
		clear()

def clear():
	id_number.set('')
	name.set('')
	age.set('')
	e1.configure(state='normal')

def add():
	try:
		con = pymysql.connect(user='root', password ='admin',\
			host = 'localhost',database ='db')
		cur = con.cursor()
		sql ="insert student values('%s','%s','%s')"\
		%(id_number.get(),name.get(),age.get())
		cur.execute(sql)
		con.commit()
		con.close()
		messagebox.showinfo('Success','Record saved...')
	except:
		messagebox.showinfo('Error','Error data entry...')
	finally:
		clear()

def update():
	try:
		con = pymysql.connect(user='root', password ='admin',\
			host = 'localhost',database ='db')
		cur = con.cursor()
		sql ="update student set name='%s,'' age='%s' where id_number='%s'"\
		%(name.get(), age.get(),id_number.get())
		cur.execute(sql)
		con.commit()
		con.close()
		messagebox.showinfo('Success','Record saved...')
	except:
		messagebox.showinfo('Error','Error data entry...')
	finally:
		clear()

def delete():
	try:
		con = pymysql.connect(user='root', password ='admin',\
			host = 'localhost',database ='db')
		cur = con.cursor()
		sql ="delete from student where id_number='%s'"\
		%(id_number.get())
		cur.execute(sql)
		con.commit()
		con.close()
		messagebox.showinfo('Success','Record deleted...')
	except:
		messagebox.showinfo('Error','Error data entry...')
	finally:
		clear()



w1 = Tk()
w1.title('Student Search/Register App')
w1.geometry('500x200')
ptitle=Label(w1, text='''Program to add, delete and update the records from students info''')

ptitle.grid(row = 0, column = 0, columnspan =2)

id_number=StringVar()
name=StringVar()
age=StringVar()

l1=Label(w1, text = 'Id Number')
e1=Entry(w1, textvariable = id_number)
l2=Label(w1, text = 'Name')
e2=Entry(w1, textvariable = name)
l3=Label(w1, text = 'Age')
e3=Entry(w1, textvariable = age)

b1 = Button(w1, text='Search', command = search)
b2 = Button(w1, text='Add', command = add)
b3 = Button(w1, text='Update', command = update)
b4 = Button(w1, text='Delete', command = delete)
b5 = Button(w1, text='Clear', command = clear)

l1.grid(row = 1, column =0)
e1.grid(row = 1, column =1)
b1.grid(row = 1, column =2)

l2.grid(row = 2, column =0)
e2.grid(row = 2, column =1)

l3.grid(row = 3, column =0)
e3.grid(row = 3, column =1)

b2.grid(row = 4, column =0)
b3.grid(row = 4, column =1)
b4.grid(row = 5, column =0)
b5.grid(row = 5, column =1)

w1.mainloop() 