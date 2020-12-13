from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

#Student addition code here
class studentaddition():
    #For optionmenu to insert class
    def check(self):
        self.e6.delete(0,END)
        self.e6.insert(0,self.val1.get())
        self.val1.__del__()
    def addf(self):
        #To Create different tables of class
        if self.e6.get() == "Class 1":

            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute("Create table if not exists Class1(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class1 values(?,?,?,?,?,?)",(str(self.e1.get()),str(self.e4.get()),str(self.e2.get()),str(self.e3.get()),str(self.e5.get()),str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)


        elif self.e6.get() == "Class 2":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class2(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class2 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)

        elif self.e6.get() == "Class 3":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class3(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class3 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 4":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class4(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class4 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 5":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class5(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class5 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 6":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class6(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class6 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 7":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class7(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class7 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 8":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class8(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class8 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 9":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class9(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class9 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 10":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class10(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class10 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
        elif self.e6.get() == "Class 11":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class11(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class11 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)

        elif self.e6.get() == "Class 12":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists Class12(Student Name text,Roll No text,Fathers Name text,Mothers Name text,DOB text,Class text)")
            db.execute("insert into Class12 values(?,?,?,?,?,?)", (
            str(self.e1.get()), str(self.e4.get()), str(self.e2.get()), str(self.e3.get()), str(self.e5.get()),
            str(self.e6.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)

        messagebox.showinfo("Inbox","Student Added")


    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("700x520")
        self.frame.configure(background = "white")
        self.frame.title("Student Registration")
        self.l1 = Label(self.frame,text="",bg="dim gray",height="4",width="100")
        self.l2 = Label(self.frame,text="Welcome To",font=("bold italic","25"),bg="dim gray",fg="orange")
        self.l3 = Label(self.frame,text="STUDENT REGISTRATION",bg="dim gray",fg="white",font=("italic","25"))
        self.ln1 = Label(self.frame,text="Enter Student's Name",bg="white",fg="black")
        self.ln2 = Label(self.frame, text="Enter Father's Name", bg="white", fg="black")
        self.ln3 = Label(self.frame, text="Enter Mother's Name", bg="white", fg="black")
        self.ln4 = Label(self.frame, text="Enter Roll Nmber", bg="white", fg="black")
        self.ln5 = Label(self.frame, text="Enter D.O.B.(*dd/mm/yy-format)", bg="white", fg="black")
        self.ln6 = Button(self.frame, text="ADD Standard", bg="white", fg="black",command=self.check)
        self.val1 = StringVar()
        self.lt1 = ["Class 1","Class 2","Class 3","Class 4","Class 5","Class 6","Class 7","Class 8","Class 9","Class 10","Class 11","Class 12"]
        self.op = OptionMenu(self.frame,self.val1,*self.lt1)
        self.e1 = Entry(self.frame,bg="snow",width="35")
        self.e2 = Entry(self.frame, bg="snow", width="35")
        self.e3 = Entry(self.frame, bg="snow", width="35")
        self.e4 = Entry(self.frame, bg="snow", width="35")
        self.e5 = Entry(self.frame, bg="snow", width="35")
        self.e6 = Entry(self.frame, bg="snow", width="15")
        self.b1 = Button(self.frame,text="SAVE DETAILS",bg="lime green",fg="white",width="25",height="2",command=self.addf)
        self.l1.place(x=0,y=0)
        self.l2.place(x=50,y=2)
        self.l3.place(x=250,y=2)
        self.ln1.place(x=10,y=80)
        self.e1.place(x=10,y=100)
        self.ln2.place(x=10, y=140)
        self.e2.place(x=10, y=160)
        self.ln3.place(x=10, y=200)
        self.e3.place(x=10, y=220)
        self.ln4.place(x=10, y=260)
        self.e4.place(x=10, y=280)
        self.ln5.place(x=10, y=320)
        self.e5.place(x=10, y=340)
        self.op.place(x=500,y=80)
        self.ln6.place(x=400, y=80)
        self.e6.place(x=400, y=100)
        self.b1.place(x=400,y=400)
        self.frame.mainloop()

#Student Addition Code ends Here

#Staff Addition code  starts here

class staffadd():

    def insert(self):
        self.e4.delete(0, END)
        self.e4.insert(0, self.val1.get())
        self.val1.__del__()
    #Code To Save Data of Teacher's in Databse Start's Here
    def saved(self):
        if self.e4.get() == "Physics":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists PhysicsFaculty(Teacher Name text,Contact Number text,DOB text,Subject text)")
            db.execute("insert into PhysicsFaculty values(?,?,?,?)", (
            str(self.e1.get()), str(self.e2.get()), str(self.e3.get()), str(self.e4.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)

        elif self.e4.get() == 'Chemistry':
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists ChemistryFaculty(Teacher Name text,Contact Number text,DOB text,Subject text)")
            db.execute("insert into ChemistryFaculty values(?,?,?,?)", (
                str(self.e1.get()), str(self.e2.get()), str(self.e3.get()), str(self.e4.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
        elif self.e4.get() == 'Maths':
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists MathsFaculty(Teacher Name text,Contact Number text,DOB text,Subject text)")
            db.execute("insert into MathsFaculty values(?,?,?,?)", (
                str(self.e1.get()), str(self.e2.get()), str(self.e3.get()), str(self.e4.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
        elif self.e4.get() == 'Computers':
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            db.execute(
                "Create table if not exists ComputersFaculty(Teacher Name text,Contact Number text,DOB text,Subject text)")
            db.execute("insert into ComputersFaculty values(?,?,?,?)", (
                str(self.e1.get()), str(self.e2.get()), str(self.e3.get()), str(self.e4.get())))
            db.commit()
            db.close()
            print("Succesfull")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
        messagebox.showinfo("Inbox","Data Saved")

    # Code To Save Data of Teacher's in Databse End's Here

    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("700x500")
        self.frame.configure(background="white")
        self.frame.title("Staff Addition")
        self.lh1 = Label(self.frame,bg='maroon4',height="4",width="50")
        self.lh2 = Label(self.frame, bg='snow', height="4", width="50")
        self.lh3 = Label(self.frame,text="  WELCOME TO", fg='snow',bg="maroon4",font=("BOLD","30"))
        self.lh4 = Label(self.frame,text="STAFF ADDITION", fg='maroon4',bg="snow",font=("BOLD","30"))
        self.lh1.place(x=0,y=0)
        self.lh2.place(x=350, y=0)
        self.lh3.place(x=0, y=0)
        self.lh4.place(x=350, y=0)
        self.ln1 = Label(self.frame, text="Enter Teacher's Name", bg="white", fg="black")
        self.ln2 = Label(self.frame, text="Enter Contact Number", bg="white", fg="black")
        self.ln3 = Label(self.frame, text="Enter D.O.B.-(dd/mm/yy-format)", bg="white", fg="black")
        self.e1 = Entry(self.frame, bg="snow", width="35")
        self.e2 = Entry(self.frame, bg="snow", width="35")
        self.e3 = Entry(self.frame, bg="snow", width="35")
        self.e4 = Entry(self.frame, bg="snow", width="15")
        self.val1 = StringVar()
        self.lt = ["Physics",'Chemistry',"Maths","Computers"]
        self.op = OptionMenu(self.frame,self.val1,*self.lt)
        self.b1 = Button(self.frame,text="Add Subject",bg="snow",command=self.insert)
        self.b2 = Button(self.frame,text="Save Details",bg="snow",fg="maroon4",width="10",height="1",font=("BOLD","14"),command=self.saved)
        self.ln1.place(x=20,y=100)
        self.ln2.place(x=20, y=180)
        self.ln3.place(x=20, y=260)
        self.e1.place(x=20,y=120)
        self.e2.place(x=20, y=200)
        self.e3.place(x=20, y=280)
        self.op.place(x=600,y=90)
        self.b1.place(x=500,y=100)
        self.e4.place(x=500,y=130)
        self.b2.place(x=500,y=400)
        self.frame.mainloop()

#Staff Addition Code Ends HERE

#Student Attendence code Starts here

class Stuatt():



    def miniwindow(self):
        def f1(self):
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.frame1.destroy()
            return 0

        def f2(self):
            self.frame1.destroy()
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            return 1


        self.frame1 = Tk()
        self.frame1.geometry('100x100')
        self.bb1 = Button(self.frame1,text="Present",bg="green",fg="white",command=lambda:f1(self))
        self.bb2 = Button(self.frame1, text="Absent", bg="red", fg="white",command= lambda:f2(self))
        self.bb1.place(x=0,y=40)
        self.bb2.place(x=50, y=40)
        self.frame1.mainloop()







    def insert(self):
        self.e1.delete(0, END)
        self.e1.insert(0, self.val1.get())
        self.val1.__del__()

    def trail3(self):
        self.e2.delete(0,END)
        self.e3.delete(0, END)
        i=0


    def takeatt(self):
        if self.e1.get() == "Class 1":
            db = sqlite3.connect("D:\\python codes\\web\\database.db")
            data = db.execute("Select * from Class1")
            pa = sorted(data)
            db.close()
            for row in pa:
                #global  i=1
                self.e2.insert(0, row[0])
                self.e3.insert(0, row[1])
                b__1 = Button(self.frame,text="Present",command=self.trail3)
                b__1.place(x=10,y=400)
                #mini = self.miniwindow()
                #print(mini)
                print(row)










    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("710x500")
        self.frame.configure(background="white")
        self.frame.title("St. Attendance")
        self.lh1 = Label(self.frame, bg='orange', height="4", width="50")
        self.lh2 = Label(self.frame, bg='snow', height="4", width="50")
        self.lh3 = Label(self.frame, text="  WELCOME TO", fg='snow', bg="orange", font=("BOLD", "30"))
        self.lh4 = Label(self.frame, text="St. Attendance", fg='orange', bg="snow", font=("BOLD", "30"))
        self.lh1.place(x=0, y=0)
        self.lh2.place(x=350, y=0)
        self.lh3.place(x=0, y=0)
        self.lh4.place(x=350, y=0)
        self.l2 = Label(self.frame, text="Student Name",bg="white")
        self.l3 = Label(self.frame, text="Student Roll No.",bg="white")
        self.l5 = Label(self.frame, text="Number of Present", bg="white")
        self.l6 = Label(self.frame, text="Number of Absent", bg="white")
        self.l4 = Label(self.frame, text="Enter Initial Date(*dd/mm/yy-format)", bg="white")
        self.l7 = Label(self.frame, text="Enter Final Date(*dd/mm/yy-format)", bg="white")
        self.e1 = Entry(self.frame, bg="snow", width="15")
        self.e4 = Entry(self.frame, bg="snow", width="15")
        self.e5 = Entry(self.frame, bg="snow", width="15")
        self.e6 = Entry(self.frame, bg="snow", width="15")
        self.e7 = Entry(self.frame, bg="snow", width="15")
        self.e2 = Entry(self.frame, bg="snow", width="35")
        self.e3 = Entry(self.frame, bg="snow", width="35")
        self.b1 = Button(self.frame,text="Select Class",bg="snow",fg="orange",command=self.insert)
        self.b2 = Button(self.frame, text="Start Attendence", bg="snow", fg="orange",command=self.takeatt)
        self.val1 = StringVar()
        self.lt1 = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9",
                    "Class 10", "Class 11", "Class 12"]
        self.op = OptionMenu(self.frame, self.val1, *self.lt1)
        self.op.place(x=600,y=100)
        self.b1.place(x=500, y=100)
        self.e1.place(x=500,y=150)#Class input
        self.l2.place(x=20,y=100)
        self.l3.place(x=20, y=180)
        self.e2.place(x=20, y=120)#Name input
        self.e3.place(x=20, y=200)#Roll no.
        self.b2.place(x=500,y=400)
        self.l4.place(x=500,y=180)
        self.e4.place(x=500,y=200)#Date input
        self.l7.place(x=500, y=260)
        self.e7.place(x=500, y=280)#Date Input
        self.l5.place(x=20, y=260)
        self.e5.place(x=20, y=280)#Present Input
        self.l6.place(x=250, y=260)
        self.e6.place(x=250, y=280)#Absent Input
        self.frame.mainloop()







#Student Attendence code Ends here

#Staff Attendence Code Starts here


class staffatt():
    def insert(self):
        self.e1.delete(0, END)
        self.e1.insert(0, self.val1.get())
        self.val1.__del__()

    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("710x500")
        self.frame.configure(background="white")
        self.frame.title("Staff Attendance")
        self.lh1 = Label(self.frame, bg='cyan4', height="4", width="50")
        self.lh2 = Label(self.frame, bg='snow', height="4", width="50")
        self.lh3 = Label(self.frame, text="  WELCOME TO", fg='snow', bg="cyan4", font=("BOLD", "30"))
        self.lh4 = Label(self.frame, text="Staff Attendance", fg='cyan4', bg="snow", font=("BOLD", "30"))
        self.lh1.place(x=0, y=0)
        self.lh2.place(x=350, y=0)
        self.lh3.place(x=0, y=0)
        self.lh4.place(x=350, y=0)
        self.l2 = Label(self.frame, text="Staff Subject",bg="white")
        self.l3 = Label(self.frame, text="Staff Contact Number",bg="white")
        self.l5 = Label(self.frame, text="Number of Present", bg="white")
        self.l6 = Label(self.frame, text="Number of Absent", bg="white")
        self.l4 = Label(self.frame, text="Enter Initial Date(*dd/mm/yy-format)", bg="white")
        self.l7 = Label(self.frame, text="Enter Final Date(*dd/mm/yy-format)", bg="white")
        self.e1 = Entry(self.frame, bg="snow", width="15")
        self.e4 = Entry(self.frame, bg="snow", width="15")
        self.e5 = Entry(self.frame, bg="snow", width="15")
        self.e6 = Entry(self.frame, bg="snow", width="15")
        self.e7 = Entry(self.frame, bg="snow", width="15")
        self.e2 = Entry(self.frame, bg="snow", width="35")
        self.e3 = Entry(self.frame, bg="snow", width="35")
        self.b1 = Button(self.frame,text="Select Subject",bg="snow",fg="cyan4",command=self.insert)
        #self.b2 = Button(self.frame, text="Start Attendence", bg="snow", fg="orange",command=self.takeatt)
        self.val1 = StringVar()
        self.lt1 = ["Physics", "Chemistry", "Maths","Computer Science"]
        self.op = OptionMenu(self.frame, self.val1, *self.lt1)
        self.op.place(x=600,y=100)
        self.b1.place(x=500, y=100)
        self.e1.place(x=500,y=150)#Class input
        self.l2.place(x=20,y=100)
        self.l3.place(x=20, y=180)
        self.e2.place(x=20, y=120)#Name input
        self.e3.place(x=20, y=200)#Roll no.
        #self.b2.place(x=500,y=400)
        self.l4.place(x=500,y=180)
        self.e4.place(x=500,y=200)#Date input
        self.l7.place(x=500, y=260)
        self.e7.place(x=500, y=280)#Date Input
        self.l5.place(x=20, y=260)
        self.e5.place(x=20, y=280)#Present Input
        self.l6.place(x=250, y=260)
        self.e6.place(x=250, y=280)#Absent Input
        self.frame.mainloop()

#Staff Attendance code ends here


#Student Removal Code Starts here
class stremoval():
    def newsubwindow(self):
        messagebox.showinfo("Student Removed","SUCCESSFUL")



    def check(self):
        self.e1.delete(0, END)
        self.e1.insert(0, self.val1.get())
        self.val1.__del__()

    def login(self):
        if len(self.e1.get())==0:
            messagebox.showinfo("Attention","Please Select Class")


        else :
            if self.e1.get()=="Class 1":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class1")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)


            elif self.e1.get()=="Class 2":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class2")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 3":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class3")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 4":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class4")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 5":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class5")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 6":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class6")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get() == "Class 7":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class7")
                for self.row in data:
                    if str(self.row[1]) == self.e2.get() and str(self.row[4]) == self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert", "Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 8":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class8")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)


            elif self.e1.get()=="Class 9":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class9")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 10":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class10")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Class 11":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class11")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Class 12":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class12")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

    def __init__(self):
        self.f1 = Tk()
        self.f1.geometry('300x250')
        self.f1.title("Login")
        self.f1.configure(background = "white")
        self.lh1= Label(self.f1,text="  STUDENT",fg="turquoise4",bg="white" ,font=("Italic", "20"))
        self.lh2 = Label(self.f1, text="  REMOVAL", bg="white", fg="turquoise4", font=("Italic", "20"))
        self.lb1 =  Label(self.f1,bg="white",height="10",width=20)
        self.lb2 = Label(self.f1,bg="white",fg="turquoise3",text="Student Roll Number",font = ("Italic","12"))
        self.lb3 = Label(self.f1, bg="white", fg="turquoise3", text="Student Date of Birth"+"\n"+"(dd/mm/yy-format)", font=("Italic", "12"))
        self.e1 = Entry(self.f1 , bg =  "white" , width= 10 )
        self.e2 = Entry(self.f1, bg="white", width=15)
        self.e3 = Entry(self.f1, bg="white", width=15)
        self.ln = Button(self.f1, text="ADD Standard", bg="white", fg="turquoise3", command=self.check)
        self.val1 = StringVar()
        self.lt1 = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9",
                    "Class 10", "Class 11", "Class 12"]
        self.op = OptionMenu(self.f1, self.val1, *self.lt1)
        self.b = Button(self.f1,text="Log In",width=40,bg="turquoise4",fg="white",command=self.login)
        self.lh1.place(x=0,y=0)
        self.lb2.place(x=0,y=100)
        self.lb3.place(x=0,y=150)
        self.lb1.place(x=150,y=50)
        self.ln.place(x=50,y=50)
        self.e1.place(x=150,y=50)
        self.e2.place(x=150,y=100)
        self.e3.place(x=150,y=150)
        self.op.place(x=0,y=50)
        self.lh2.place(x=150, y=0)
        self.b.place(x=4,y=200)
        self.f1.mainloop()






#Student Removal Code Ends here

#STAFF Removal Code Ends here

class staffremoval():

    def check(self):
        self.e1.delete(0, END)
        self.e1.insert(0, self.val1.get())
        self.val1.__del__()

    def newsubwindow(self):
        messagebox.showinfo("Successfull","Faculty Removed")





    def login(self):

        if len(self.e1.get())==0:
            messagebox.showinfo("Attention","Please Select Class")


        else :
            if self.e1.get()=="Chemistry":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from ChemistryFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Physics":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from PhysicsFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Maths":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from MathsFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Computers":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from ComputersFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

    def __init__(self):
        self.f1 = Tk()
        self.f1.geometry('300x250')
        self.f1.title("Login")
        self.f1.configure(background = "white")
        self.lh1= Label(self.f1,text="  STAFF",fg="SlateBlue1",bg="white" ,font=("Italic", "20"))
        self.lh2 = Label(self.f1, text="  REMOVAL", bg="white", fg="SlateBlue1", font=("Italic", "20"))
        self.lb1 =  Label(self.f1,bg="white",height="10",width=20)
        self.lb2 = Label(self.f1,bg="white",fg="SlateBlue1",text="Staff Contact NO.",font = ("Italic","12"))
        self.lb3 = Label(self.f1, bg="white", fg="SlateBlue1", text="Staff Date of Birth"+"\n"+"(dd/mm/yy-format)", font=("Italic", "12"))
        self.e1 = Entry(self.f1 , bg =  "white" , width= 10 )
        self.e2 = Entry(self.f1, bg="white", width=15)
        self.e3 = Entry(self.f1, bg="white", width=15)
        self.ln = Button(self.f1, text="ADD Subject", bg="white", fg="SlateBlue1", command=self.check)
        self.val1 = StringVar()
        self.lt1 = ["Physics",'Chemistry',"Maths","Computers"]
        self.op = OptionMenu(self.f1, self.val1, *self.lt1)
        self.b = Button(self.f1,text="Log In",width=40,bg="SlateBlue1",fg="white",command=self.login)
        self.lh1.place(x=0,y=0)
        self.lb2.place(x=0,y=100)
        self.lb3.place(x=0,y=150)
        self.lb1.place(x=150,y=50)
        self.ln.place(x=50,y=50)
        self.e1.place(x=150,y=50)
        self.e2.place(x=150,y=100)
        self.e3.place(x=150,y=150)
        self.op.place(x=0,y=50)
        self.lh2.place(x=150, y=0)
        self.b.place(x=4,y=200)
        self.f1.mainloop()


#STAFF Removal Code Ends here



#Student Login Code  Start Here

class stlogin():
    def newsubwindow(self):
        self.f1.destroy()
        self.f2 =Tk()
        self.f2.geometry("750x500")
        self.f2.title("Student Info")
        self.f2.configure(background="White")
        self.lc3 = Label(self.f2, bg="SpringGreen2", width=57, height=4, fg="white")
        self.lc1 = Label(self.f2,text="STUDENT CORNER",fg="white",font=("BOLD","30"), bg="SpringGreen2")
        self.lc2 = Label(self.f2, text="WELCOME TO", fg="SpringGreen2", bg="white", font=("Italic", "30"))

        self.l1 = Label(self.f2, text="NAME                  :"+"\t"+"\t"+self.row[0],font=("BOLD","15"),bg="white")
        self.l2 = Label(self.f2, text="ROLL NUMBER      :" + "\t" + "" + self.row[1], font=("BOLD", "15"), bg="white")
        self.l3 = Label(self.f2, text="FATHERS NAME     :" + "\t" + "" + self.row[2], font=("BOLD", "15"), bg="white")
        self.l4 = Label(self.f2, text="MOTHERS NAME    :" + "\t" + "" + self.row[3], font=("BOLD", "15"), bg="white")
        self.l5 = Label(self.f2, text="D.O.B.                 :" + "\t" + "\t" + self.row[4], font=("BOLD", "15"), bg="white")
        self.l6 = Label(self.f2, text="CLASS                  :" + "\t"  + self.row[5], font=("BOLD", "15"), bg="white")
        self.lc3.place(x=350,y=0)
        self.lc2.place(x=30, y=4)
        self.lc1.place(x=350, y=4)
        self.l1.place(x=200,y=100)
        self.l2.place(x=200, y=150)
        self.l3.place(x=200, y=200)
        self.l4.place(x=200, y=250)
        self.l5.place(x=200, y=300)
        self.l6.place(x=200, y=350)
        self.f2.mainloop()



    def check(self):
        self.e1.delete(0, END)
        self.e1.insert(0, self.val1.get())
        self.val1.__del__()

    def login(self):
        if len(self.e1.get())==0:
            messagebox.showinfo("Attention","Please Select Class")


        else :
            if self.e1.get()=="Class 1":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class1")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)


            elif self.e1.get()=="Class 2":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class2")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 3":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class3")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 4":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class4")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 5":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class5")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 6":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class6")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get() == "Class 7":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class7")
                for self.row in data:
                    if str(self.row[1]) == self.e2.get() and str(self.row[4]) == self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert", "Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 8":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class8")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)


            elif self.e1.get()=="Class 9":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class9")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Class 10":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class10")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Class 11":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class11")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Class 12":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from Class12")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[4])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

    def __init__(self):
        self.f1 = Tk()
        self.f1.geometry('300x250')
        self.f1.title("Login")
        self.f1.configure(background = "white")
        self.lh1= Label(self.f1,text="  STUDENT",fg="turquoise4",bg="white" ,font=("Italic", "20"))
        self.lh2 = Label(self.f1, text="   LOGIN", bg="white", fg="turquoise4", font=("Italic", "20"))
        self.lb1 =  Label(self.f1,bg="white",height="10",width=20)
        self.lb2 = Label(self.f1,bg="white",fg="turquoise3",text="Student Roll Number",font = ("Italic","12"))
        self.lb3 = Label(self.f1, bg="white", fg="turquoise3", text="Student Date of Birth"+"\n"+"(dd/mm/yy-format)", font=("Italic", "12"))
        self.e1 = Entry(self.f1 , bg =  "white" , width= 10 )
        self.e2 = Entry(self.f1, bg="white", width=15)
        self.e3 = Entry(self.f1, bg="white", width=15)
        self.ln = Button(self.f1, text="ADD Standard", bg="white", fg="turquoise3", command=self.check)
        self.val1 = StringVar()
        self.lt1 = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9",
                    "Class 10", "Class 11", "Class 12"]
        self.op = OptionMenu(self.f1, self.val1, *self.lt1)
        self.b = Button(self.f1,text="Log In",width=40,bg="turquoise4",fg="white",command=self.login)
        self.lh1.place(x=0,y=0)
        self.lb2.place(x=0,y=100)
        self.lb3.place(x=0,y=150)
        self.lb1.place(x=150,y=50)
        self.ln.place(x=50,y=50)
        self.e1.place(x=150,y=50)
        self.e2.place(x=150,y=100)
        self.e3.place(x=150,y=150)
        self.op.place(x=0,y=50)
        self.lh2.place(x=150, y=0)
        self.b.place(x=4,y=200)
        self.f1.mainloop()


#Student Login code Ends Here

#Staff Login code starts here

class stafflogin():

    def check(self):
        self.e1.delete(0, END)
        self.e1.insert(0, self.val1.get())
        self.val1.__del__()

    def newsubwindow(self):
        self.f1.destroy()
        self.f2 =Tk()
        self.f2.geometry("750x500")
        self.f2.title("Student Info")
        self.f2.configure(background="White")
        self.lc3 = Label(self.f2, bg="bisque", width=57, height=4, fg="white")
        self.lc1 = Label(self.f2,text="STAFF LOGIN",fg="white",font=("BOLD","30"), bg="bisque")
        self.lc2 = Label(self.f2, text="WELCOME TO", fg="bisque", bg="white", font=("Italic", "30"))

        self.l1 = Label(self.f2, text="NAME                    :"+"\t"+self.row[0],font=("BOLD","15"),bg="white")
        self.l2 = Label(self.f2, text="Contact NUMBER    :" + "\t" + "" + self.row[1], font=("BOLD", "15"), bg="white")
        self.l3 = Label(self.f2, text="Date of Birth     \t:" + "\t" + "" + self.row[2], font=("BOLD", "15"), bg="white")
        self.l4 = Label(self.f2, text="Subject           \t:" + "\t" + "" + self.row[3], font=("BOLD", "15"), bg="white")
        self.lc3.place(x=350,y=0)
        self.lc2.place(x=30, y=4)
        self.lc1.place(x=350, y=4)
        self.l1.place(x=200,y=100)
        self.l2.place(x=200, y=150)
        self.l3.place(x=200, y=200)
        self.l4.place(x=200, y=250)
        self.f2.mainloop()





    def login(self):

        if len(self.e1.get())==0:
            messagebox.showinfo("Attention","Please Select Class")


        else :
            if self.e1.get()=="Chemistry":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from ChemistryFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Physics":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from PhysicsFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

            elif self.e1.get()=="Maths":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from MathsFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
            elif self.e1.get()=="Computers":
                db = sqlite3.connect("D:\\python codes\\web\\database.db")
                data = db.execute("Select *from ComputersFaculty")
                for self.row in data:
                    if str(self.row[1])==self.e2.get() and str(self.row[2])==self.e3.get():
                        print('Succesfull')
                        self.newsubwindow()
                        db.close()
                        break
                else:
                    messagebox.showinfo("Alert","Wrong Roll No or DOB")
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)

    def __init__(self):
        self.f1 = Tk()
        self.f1.geometry('300x250')
        self.f1.title("Login")
        self.f1.configure(background = "white")
        self.lh1= Label(self.f1,text="  STAFF",fg="red",bg="white" ,font=("Italic", "20"))
        self.lh2 = Label(self.f1, text="   LOGIN", bg="white", fg="red", font=("Italic", "20"))
        self.lb1 =  Label(self.f1,bg="white",height="10",width=20)
        self.lb2 = Label(self.f1,bg="white",fg="red",text="Staff Contact NO.",font = ("Italic","12"))
        self.lb3 = Label(self.f1, bg="white", fg="red", text="Staff Date of Birth"+"\n"+"(dd/mm/yy-format)", font=("Italic", "12"))
        self.e1 = Entry(self.f1 , bg =  "white" , width= 10 )
        self.e2 = Entry(self.f1, bg="white", width=15)
        self.e3 = Entry(self.f1, bg="white", width=15)
        self.ln = Button(self.f1, text="ADD Subject", bg="white", fg="red", command=self.check)
        self.val1 = StringVar()
        self.lt1 = ["Physics",'Chemistry',"Maths","Computers"]
        self.op = OptionMenu(self.f1, self.val1, *self.lt1)
        self.b = Button(self.f1,text="Log In",width=40,bg="red3",fg="white",command=self.login)
        self.lh1.place(x=0,y=0)
        self.lb2.place(x=0,y=100)
        self.lb3.place(x=0,y=150)
        self.lb1.place(x=150,y=50)
        self.ln.place(x=50,y=50)
        self.e1.place(x=150,y=50)
        self.e2.place(x=150,y=100)
        self.e3.place(x=150,y=150)
        self.op.place(x=0,y=50)
        self.lh2.place(x=150, y=0)
        self.b.place(x=4,y=200)
        self.f1.mainloop()










#Staff Login Code Ends Here

#Main frame code here
root = Tk()
root.geometry('780x500')
root.title("Main")
root.configure(background='white')
image1 = Image.open("logo1.png")
image2 = Image.open("student.jpg")
image3 = Image.open("logo2.jpg")
photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)
photo3 = ImageTk.PhotoImage(image3)
l1 = Label(root,image=photo1)
l2 = ttk.Label(root,image=photo2)
l3 = Label(image=photo3)
lt1 = Label(root,text="Welcome to"+"\n"+"   ATTENDANCE MANAGEMENT SYSTEM",font=("bold","8"),height="7",bg="white",width="35",fg="light sea green")
b1=Button(root,text="Student Attendance",bg="dark olive green",fg="white",height="2",width="24",command=Stuatt)
b2=Button(root,text="Staff Attendance",bg="dark olive green",fg="white",height="2",width="24",command=staffatt)
b3=Button(root,text="Student Login",bg="dark olive green",fg="white",height="2",width="24",command=stlogin)
b4=Button(root,text="Staff Login",bg="dark olive green",fg="white",height="2",width="24",command=stafflogin)
b5=Button(root,text="Student Addition",bg="dark slate gray",fg="white",height="2",width="24",command=studentaddition)
b6=Button(root,text="Staff Addition",bg="dark slate gray",fg="white",height="2",width="24",command=staffadd)
b7=Button(root,text="Studnet Removal",bg="dark slate gray",fg="white",height="2",width="24",command=stremoval)
b8=Button(root,text="Staff Removal",bg="dark slate gray",fg="white",height="2",width="24",command=staffremoval)
b1.place(x=40,y=120)
b2.place(x=40,y=220)
b3.place(x=40,y=320)
b4.place(x=40,y=420)
b5.place(x=300,y=120)
b6.place(x=300,y=220)
b7.place(x=300,y=320)
b8.place(x=300,y=420)
lt1.place(x=0,y=0)
l1.place(x=230,y=0)
l2.place(x=0,y=100)
l3.place(x=555,y=0)
root.mainloop()
