from tkinter import *
import pymongo
from tkinter import ttk,messagebox
import ttkthemes
from PIL import ImageTk
import sys
from random import randint

try:
    client = pymongo.MongoClient("mongodb+srv://Bhavya:Ammulu1906@cluster0.7zd38m0.mongodb.net/?retryWrites=true&w=majority")
    db = client.SoilFarming
    print("Connected to MongoDB")
except:
    print("Database connection Error ")
    print("No connection could be made because the target machine actively refused it ")
    messagebox.showerror("Error", "Connection Error")
    sys.exit(1)

def exit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def register(root,db):
    def reg():
        global root
        id=idEntry.get()
        firstname=firstnameEntry.get()
        lastname=lastnameEntry.get()
        contact=phoneEntry.get()
        username=usernameEntry.get()
        password=pswrdEntry.get()
        email=emailEntry.get()
        Id = [id]
        Firstname = [firstname]
        Lastname = [lastname]
        Contact = [contact]
        Username = [username]
        Password = [password]
        Email = [email]
        SoilFarming={
            'Id':Id[randint(0, (len(Id) - 1))],
            'Firstname': Firstname[randint(0, (len(Firstname) - 1))],
            'Lastname': Lastname[randint(0, (len(Lastname) - 1))],
            'Contact': Contact[randint(0, (len(Contact) - 1))],
            'Username': Username[randint(0,(len(Username) - 1))],
            'Password':Password[randint(0, (len(Password) - 1))],
            'Email':Email[randint(0, (len(Email) - 1))]
        }
        if len(id)==0:
            messagebox.showwarning('Warning','All fields are required(Except: Email)')
            return
        if len(firstname)==0:
            messagebox.showwarning('Warning','All fields are required(Except: Email)')
            return
        if len(lastname)==0:
            messagebox.showwarning('Warning','All fields are required(Except: Email)')
            return
        if len(contact)==0:
            messagebox.showwarning('Warning','All fields are required(Except: Email)')
            return
        if len(username)==0:
            messagebox.showwarning('Warning','All fields are required(Except: Email)')
            return
        if len(password)==0:
            messagebox.showwarning('Warning','All fields are required(Except: Email)')
            return
        if len(email)==0 and db.details.count_documents({'Id':id}, limit=1)==0:
            result=db.details.insert_one({'Id':id,'Firstame':firstname,'Lastname':lastname,'Contact':contact,'Username':username,'Password':password})
        elif len(email)!=0 and db.details.count_documents({'Id':id}, limit=1)==0:
            result=db.details.insert_one(SoilFarming)
            messagebox.showinfo('Success','Registered successfully')
        else:
            messagebox.showerror('Error','Error')
            return
    register=Toplevel()
    register.grab_set()
    register.title('Register')
    register.geometry('400x500+200+200')
    register.resizable(0,0)
    idLabel=Label(register,text='Id',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,pady=15,padx=15)
    idEntry=Entry(register,font=('arial',15))
    idEntry.grid(row=0,column=1,pady=15,padx=15)

    firstnameLabel=Label(register,text='Firstname',font=('times new roman',15,'bold'))
    firstnameLabel.grid(row=1,column=0,pady=15,padx=15)
    firstnameEntry=Entry(register,font=('arial',15))
    firstnameEntry.grid(row=1,column=1,pady=15,padx=15)

    lastnameLabel=Label(register,text='Lastname',font=('times new roman',15,'bold'))
    lastnameLabel.grid(row=2,column=0,pady=15,padx=15)
    lastnameEntry=Entry(register,font=('arial',15))
    lastnameEntry.grid(row=2,column=1,pady=15,padx=15)

    phoneLabel=Label(register,text='Contact',font=('times new roman',15,'bold'))
    phoneLabel.grid(row=3,column=0,pady=15,padx=15)
    phoneEntry=Entry(register,font=('arial',15))
    phoneEntry.grid(row=3,column=1,pady=15,padx=15)

    usernameLabel=Label(register,text='Username',font=('times new roman',15,'bold'))
    usernameLabel.grid(row=4,column=0,pady=15,padx=15)
    usernameEntry=Entry(register,font=('arial',15))
    usernameEntry.grid(row=4,column=1,pady=15,padx=15)

    pswrdLabel=Label(register,text='Password',font=('times new roman',15,'bold'))
    pswrdLabel.grid(row=5,column=0,pady=15,padx=15)
    pswrdEntry=Entry(register,font=('arial',15))
    pswrdEntry.grid(row=5,column=1,pady=15,padx=15)

    emailLabel=Label(register,text='Email Id',font=('times new roman',15,'bold'))
    emailLabel.grid(row=6,column=0,pady=15,padx=15)
    emailEntry=Entry(register,font=('arial',15))
    emailEntry.grid(row=6,column=1,pady=15,padx=15)

    registerButton=ttk.Button(register,text='Register',compound=CENTER,command=reg)
    registerButton.grid(row=7,columnspan=2,pady=15)


def login(root,db):
    def userlogin():
        if usernameEntry.get() == '' or pswrdEntry.get() == '':
            messagebox.showerror('Error', "Fields cannot be empty")
        elif usernameEntry.get() == 'user' and pswrdEntry.get() == '1234':
            messagebox.showinfo('Success', 'Welcome')
        else:
            messagebox.showerror('Error', 'Enter valid details')


    user = Toplevel()
    user.grab_set()
    user.title('User Login')
    user.geometry('350x140+630+230')
    user.resizable(0, 0)

    usernameLabel = Label(user, text='Username', font=('times new roman', 20, 'bold'))
    usernameLabel.grid(row=0, column=0)
    usernameEntry = Entry(user, font=('arial', 15))
    usernameEntry.grid(row=0, column=1, pady=10, padx=10)

    pswrdLabel = Label(user, text='password', font=('times new roman', 20, 'bold'))
    pswrdLabel.grid(row=1, column=0)
    pswrdEntry = Entry(user, font=('arial', 15))
    pswrdEntry.grid(row=1, column=1, pady=10, padx=10)

    loginButton = ttk.Button(user, text='login', cursor='hand2', command=userlogin)
    loginButton.grid(row=2, columnspan=2)

def viewsand(root,db):
    view=Toplevel()
    view.geometry('750x400+200+200')
    view.title('Sand Details')
    serialnolabel=Label(view,text='SN')
    serialnolabel.grid(row=0,column=0,pady=10,padx=10)
    typeofsoillabel=Label(view,text='Type_of_Soil')
    typeofsoillabel.grid(row=0,column=2,pady=10,padx=10)
    cropsgrownlabel=Label(view,text='Crops_grown')
    cropsgrownlabel.grid(row=0,column=4,pady=10,padx=10)
    nutrientlabel=Label(view,text='Nutrient_content')
    nutrientlabel.grid(row=0,column=6,pady=10,padx=10)
    dryingoutlabel=Label(view,text='Drying_out')
    dryingoutlabel.grid(row=0,column=8,pady=10,padx=10)
    waterretentionlabel=Label(view,text='Water_retention')
    waterretentionlabel.grid(row=0,column=10,pady=10,padx=10)
    whentogrowlabel=Label(view,text='When_to_grow')
    whentogrowlabel.grid(row=0,column=12,pady=10,padx=10)
    i=1
    for x in db.details.find():
        y=len(x)
        print(x)
        serialnolabel = Label(view, text=x['SN'])
        serialnolabel.grid(row=i, column=0, pady=10, padx=10)
        typeofsoillabel = Label(view, text=x['Type_of_Soil'])
        typeofsoillabel.grid(row=i, column=2, pady=10, padx=10)
        cropsgrownlabel = Label(view, text=x['Crops_grown'])
        cropsgrownlabel.grid(row=i, column=4, pady=10, padx=10)
        nutrientlabel = Label(view, text=x['Nutrient_content'])
        nutrientlabel.grid(row=i, column=6, pady=10, padx=10)
        dryingoutlabel = Label(view, text=x['Drying_out'])
        dryingoutlabel.grid(row=i, column=8, pady=10, padx=10)
        waterretentionlabel = Label(view, text=x['Water_retention'])
        waterretentionlabel.grid(row=i, column=10, pady=10, padx=10)
        if y==10:
            whentogrowlabel = Label(view, text=x['When_to_grow'])
            whentogrowlabel.grid(row=i, column=12, pady=10, padx=10)
        i += 1

def viewdist(root,db):
    new = Toplevel()
    new.geometry('680x400+200+200')
    new.title('Distributor Details')

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('300x350+450+300')
root.resizable(0,0)
root.title('User window')


registerButton=ttk.Button(root,text='Register',width=25,command=lambda: register(root,db))
registerButton.grid(row=0,column=0,pady=15,padx=20)

loginButton=ttk.Button(root,text='Login',width=25,command=lambda: login(root,db))
loginButton.grid(row=1,column=0,pady=15,padx=20)

viewButton=ttk.Button(root,text='View Sand Details',width=25,command=lambda: viewsand(root,db))
viewButton.grid(row=2,column=0,pady=15,padx=20)

viewdsButton=ttk.Button(root,text='View Distributor Details',width=25,command=lambda: viewdist(root,db))
viewdsButton.grid(row=3,column=0,pady=15,padx=20)

exitButton=ttk.Button(root,text='Exit',width=25,command=exit)
exitButton.grid(row=4,column=0,pady=15,padx=20)

root.mainloop()