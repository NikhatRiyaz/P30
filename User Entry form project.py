from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector
root = Tk()
root.title('Entry Form')
font = ('Callibri', 20)


conn = mysql.connector.connect(host="localhost",user="root",password="rimsha123")
cur = conn.cursor(buffered=True)

try:
    cur.execute("use personal_details")
    cur.execute("desc persons")
except:
    cur.execute('CREATE TABLE persons(User_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, Name VARCHAR(20),Surname VARCHAR(20),Aadhar VARCHAR(10),Pancard VARCHAR(20),Email VARCHAR(20))')
    conn.commit()
def submit_btn():
    cur.execute(f"INSERT INTO persons(User_id,Name,Surname,Aadhar,Pancard,Email) VALUES ('{ent1.get()}','{ent2.get()}','{ent3.get()}','{ent4.get()}','{ent5.get()}','{ent6.get()}')")
    conn.commit()
def clear_btn():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)

def retrieve_btn():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="rimsha123")
        cur.execute("SELECT * FROM persons")
        records = cur.fetchall()
        if records:
            # Display the records in a messagebox
            messagebox.showinfo("Records Found", "\n".join([f"Record: {record}" for record in records]))
        else:
            # Display error message if no records are found
            messagebox.showerror("Error", "No records found")

    except mysql.connector.Error as err:
        # Display error message if connection or query execution fails
        messagebox.showerror("Error", f"Error: {err}")

def cancel_btn():
    root.destroy()


#Frames
frm_a = LabelFrame(master = root, relief = GROOVE, borderwidth = 10,padx=5,pady=5)
frm_b = LabelFrame(master = root, relief = RIDGE, borderwidth = 10,padx=5,pady=5)

#Labels
lb1=Label(master = frm_a,text = 'User_id : ', font=font)
lb2=Label(master = frm_a,text = 'Name : ', font=font)
lb3=Label(master = frm_a,text = 'Surname : ', font=font)
lb4=Label(master = frm_a,text = 'Aadhar : ', font=font)
lb5=Label(master = frm_a,text = 'Pancard : ', font=font)
lb6=Label(master = frm_a,text = 'Email : ', font=font)

#Buttons
b1=Button(master = frm_b,text = 'Clear', font=font, command=clear_btn)
b2=Button(master = frm_b,text = 'Retrieve', font=font, command=retrieve_btn)
b3=Button(master = frm_b,text = 'Submit', font=font, command=submit_btn)
b4=Button(master = frm_b,text = 'Cancel', font=font, command=cancel_btn)


#Entry widgets
ent1 = Entry(master= frm_a, font=font, width = 30)
ent2 = Entry(master= frm_a, font=font, width = 30)
ent3 = Entry(master= frm_a, font=font, width = 30)
ent4 = Entry(master= frm_a, font=font, width = 30)
ent5 = Entry(master= frm_a, font=font, width = 30)
ent6 = Entry(master= frm_a, font=font, width = 30)

#Grid

frm_a.grid(row=0,column=0)
frm_b.grid(row=1,column=0)

lb1.grid(row=0,column=0,sticky='nw')
lb2.grid(row=1,column=0,sticky='nw')
lb3.grid(row=2,column=0,sticky='nw')
lb4.grid(row=3,column=0,sticky='nw')
lb5.grid(row=4,column=0,sticky='nw')
lb6.grid(row=5,column=0,sticky='nw')

b1.grid(row=5,column=0,sticky='news')
b2.grid(row=5,column=1,sticky='news')
b3.grid(row=5,column=2,sticky='news')
b4.grid(row=5,column=3,sticky='news')

ent1.grid(row=0,column=1,sticky='news')
ent2.grid(row=1,column=1,sticky='news')
ent3.grid(row=2,column=1,sticky='news')
ent4.grid(row=3,column=1,sticky='news')
ent5.grid(row=4,column=1,sticky='news')
ent6.grid(row=5,column=1,sticky='news')

# frm_a.pack()
#
# lb1.pack()
# lb2.pack()
# lb3.pack()
# lb4.pack()
# lb5.pack()
#
# ent1.pack()
# ent2.pack()
# ent3.pack()
# ent4.pack()
# ent5.pack()
#
# frm_b.pack()
#
# b1.pack()
# b2.pack()
# b3.pack()
# b4.pack()






























root.mainloop()