from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('student info')
root.geometry("400x400")

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
#database

#create a database
conn = sqlite3.connect('address_book.db')

#create cursor
c = conn.cursor()

#crate table
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		age integer,
		id_number integer,
		course text)""")
'''
#update record
def update():
#create a database
	conn = sqlite3.connect('address_book.db')
	#create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	c.execute("""UPDATE addresses SET
		first_name =:first,
		last_name =:last,
		age = :age,
		id_number =:idno,
		course =:course

		WHERE oid = :oid""",
		{
		'first':f_name_editor.get(),
		'last':l_name_editor.get(),
		'age':age_editor.get(),
		'idno':id_number_editor.get(),
		'course':course_editor.get(),

		'oid':record_id

		}
		)


	#commut changes
	conn.commit()
	#close connection
	conn.close()

	editor.destroy()

#create edit to update record
def edit():
	global editor
	editor = Tk()
	editor.title('Update Record')
	editor.geometry("400x400")

	#create a database
	conn = sqlite3.connect('address_book.db')
	#create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	#query data
	c.execute("SELECT * FROM addresses WHERE id_number=" + record_id)
	records = c.fetchall()
	
	#create golbal var for textbox names
	global f_name_editor
	global l_name_editor
	global age_editor
	global id_number_editor
	global course_editor


	#create text box
	f_name_editor = Entry(editor,width = 30)
	f_name_editor.grid(row = 0, column = 1, padx =20, pady=(10,0))
	l_name_editor = Entry(editor,width = 30)
	l_name_editor.grid(row = 1, column = 1)
	age_editor = Entry(editor,width = 30)
	age_editor.grid(row = 2, column = 1)
	id_number_editor = Entry(editor,width = 30)
	id_number_editor.grid(row = 3, column = 1)
	course_editor = Entry(editor,width = 30)
	course_editor.grid(row = 4, column = 1)

	#create textbox labels
	f_name_label = Label(editor, text='First Name')
	f_name_label.grid(row=0, column= 0, pady=(10,0))
	l_name_label = Label(editor, text='Last Name')
	l_name_label.grid(row=1, column= 0)
	age_label = Label(editor, text='Age')
	age_label.grid(row=2, column= 0)
	id_number_label = Label(editor, text='ID number')
	id_number_label.grid(row=3, column= 0)
	course_label = Label(editor, text='Course')
	course_label.grid(row=4, column= 0)

	#Loop results
	for record in records:
		f_name_editor.insert(0,record[0])
		l_name_editor.insert(0,record[1])
		age_editor.insert(0,record[2])
		id_number_editor.insert(0,record[3])
		course_editor.insert(0,record[4])

	#Save record
	save_btn = Button(editor,text="Update Record", command = update)
	save_btn.grid(row=6,column=0,columnspan=2, pady=10, padx=10,ipadx=133)


#delete record fun
def delete():
	#create a database
	conn = sqlite3.connect('address_book.db')
	#create cursor
	c = conn.cursor()
	
	#delete record
	c.execute("DELETE from addresses WHERE id_number= " + delete_box.get())

	#commut changes
	conn.commit()
	#close connection
	conn.close()



#create submit
def submit():
	#create a database
	conn = sqlite3.connect('address_book.db')
	#create cursor
	c = conn.cursor()
	#inser to table
	c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:age,:id_number,:course)",
		{
					'f_name': f_name.get(),
					'l_name': l_name.get(),
					'age': age.get(),
					'id_number': id_number.get(),
					'course': course.get()
				})

	#commut changes
	conn.commit()
	#close connection
	conn.close()

	#clear box
	f_name.delete(0,END)
	l_name.delete(0,END)
	age.delete(0,END)
	id_number.delete(0,END)
	course.delete(0,END)

#create query fun
def query():
	#create a database
	conn = sqlite3.connect('address_book.db')
	#create cursor
	c = conn.cursor()

	#query data
	c.execute("SELECT *,oid FROM addresses")
	records = c.fetchall()
	#print(records)

	#loop result
	print_records = ''
	for record in records:
		print_records += str(record[0])+" "+str(record[1])+" "+"\t"+str(record[5]) +"\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column= 0, columnspan=2)

	#commut changes
	conn.commit()
	#close connection
	conn.close()



#create text box
f_name = Entry(root,width = 30)
f_name.grid(row = 0, column = 1, padx =20, pady=(10,0))
l_name = Entry(root,width = 30)
l_name.grid(row = 1, column = 1)
age = Entry(root,width = 30)
age.grid(row = 2, column = 1)
id_number = Entry(root,width = 30)
id_number.grid(row = 3, column = 1)
course = Entry(root,width = 30)
course.grid(row = 4, column = 1)
delete_box = Entry(root, width =30)
delete_box.grid(row=9,column=1,pady=5)



#create textbox labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column= 0, pady=(10,0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column= 0)
age_label = Label(root, text='Age')
age_label.grid(row=2, column= 0)
id_number_label = Label(root, text='ID number')
id_number_label.grid(row=3, column= 0)
course_label = Label(root, text='Course')
course_label.grid(row=4, column= 0)
delete_box_label = Label(root, text="Search ID No.")
delete_box_label.grid(row=9,column=0, pady=5)

#create buttons
submit_btn = Button(root, text="Add record to database", command = submit)
submit_btn.grid(row=6, column = 0 , columnspan = 2, pady = 10, padx = 10, ipadx = 100)


#Query button
query_btn = Button(root,text="Show records", command = query)
query_btn.grid(row=7,column=0,columnspan=2, pady=10, padx=10,ipadx=128)


#Delete button
delete_btn = Button(root,text="Delete Record", command = delete)
delete_btn.grid(row=10,column=0,columnspan=2, pady=10, padx=10,ipadx=125)

#Update button
edit_btn = Button(root,text="Search Record", command = edit)
edit_btn.grid(row=11,column=0,columnspan=2, pady=10, padx=10,ipadx=133)

#if len(delete_box.get())== 0:
#		messagebox.showerror("Warning!", "Box is empty! Write something")


#commut changes
conn.commit()

#close connection
conn.close()


root.mainloop()