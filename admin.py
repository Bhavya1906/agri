from tkinter import *
import pymongo
from tkinter import ttk,messagebox
import ttkthemes
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

def soil_det(root,db):
    def post_data():
        global root
        SNE = serialnoEntry.get()
        ToS = typeofsoilEntry.get()
        CRE = cropsgrownEntry.get()
        WTG = whentogrowEntry.get()
        NE = nutrientEntry.get()
        DOE = dryingoutEntry.get()
        WRE = waterretentionEntry.get()
        SN = [SNE]
        Type_of_Soil =[ToS]
        Crops_grown = [CRE]
        When_to_grow = [WTG]
        Nutrient_Content = [NE]
        Drying_out = [DOE]
        Water_retention = [WRE]
        SoilFarming={
            'SN':SN[randint(0, (len(SN) - 1))],
            'Type_of_Soil':Type_of_Soil[randint(0, (len(Type_of_Soil) - 1))],
            'Crops_grown':Crops_grown[randint(0, (len(Crops_grown) - 1))],
            'When_to_grow':When_to_grow[randint(0, (len(When_to_grow) - 1))],
            'Nutrient_Content':Nutrient_Content[randint(0, (len(Nutrient_Content) - 1))],
            'Drying_out':Drying_out[randint(0, len(Drying_out) - 1)],
            'Water_retention':Water_retention[randint(0, len(Water_retention) - 1)]
        }
        if (len(SN)==0):
            messagebox.showwarning('Warning','Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Type_of_Soil)==0):
            messagebox.showwarning('Warning','Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Crops_grown)==0):
            messagebox.showwarning('Warning','Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Nutrient_Content)==0):
            messagebox.showwarning('Warning','Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Drying_out)==0):
            messagebox.showwarning('Warning','Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Water_retention)==0):
            messagebox.showwarning('Warning','Fields cannot be empty(Except:When_to_grow)')
            return
        if len(When_to_grow)==0 and db.details.count_documents({'SN':SNE}, limit=1)==0:
            result = db.details.insert_one(
                {'SN':SNE, 'Type_of_soil': ToS, 'Crops_grown': CRE, 'When_to_grow': WTG, 'Nutrient_Content': NE,
                 'Drying_out': DOE, 'Water_retention': WRE})
        elif len(When_to_grow)!=0and db.details.count_documents({'SN':SNE}, limit=1)==0:
            result = db.details.insert_one(SoilFarming)
            messagebox.showinfo('Success','Data added successfully')

        else:
            messagebox.showerror('Error','All details are required')
            return
    new=Toplevel(root)
    new.geometry('530x450')
    new.resizable(0,0)
    new.title('Soil info')
    serialnolabel=Label(new,text='SN',font=('times new roman',20,'bold'))
    serialnolabel.grid(row=0,column=0,pady=10,padx=10)
    serialnoEntry=Entry(new,font=('calibri',15))
    serialnoEntry.grid(row=0,column=1,pady=10,padx=10)

    typeofsoillabel=Label(new,text='Type_of_Soil',font=('times new roman',20,'bold'))
    typeofsoillabel.grid(row=1,column=0,pady=10,padx=10)
    typeofsoilEntry=Entry(new,font=('calibri',15))
    typeofsoilEntry.grid(row=1,column=1,pady=10,padx=10)

    cropsgrownlabel=Label(new,text='Crops_grown',font=('times new roman',20,'bold'))
    cropsgrownlabel.grid(row=2,column=0,pady=10,padx=10)
    cropsgrownEntry=Entry(new,font=('calibri',15))
    cropsgrownEntry.grid(row=2,column=1,pady=10,padx=10)

    nutrientlabel=Label(new,text='Nutrient_content',font=('times new roman',20,'bold'))
    nutrientlabel.grid(row=3,column=0,pady=10,padx=10)
    nutrientEntry=Entry(new,font=('calibri',15))
    nutrientEntry.grid(row=3,column=1,pady=10,padx=10)

    dryingoutlabel=Label(new,text='Drying_out',font=('times new roman',20,'bold'))
    dryingoutlabel.grid(row=4,column=0,pady=10,padx=10)
    dryingoutEntry=Entry(new,font=('calibri',15))
    dryingoutEntry.grid(row=4,column=1,pady=10,padx=10)

    waterretentionlabel=Label(new,text='Water_retention',font=('times new roman',20,'bold'))
    waterretentionlabel.grid(row=5,column=0,pady=10,padx=10)
    waterretentionEntry=Entry(new,font=('calibri',15))
    waterretentionEntry.grid(row=5,column=1,pady=10,padx=10)

    whentogrowlabel=Label(new,text='When_to_grow',font=('times new roman',20,'bold'))
    whentogrowlabel.grid(row=6,column=0,pady=10,padx=10)
    whentogrowEntry=Entry(new,font=('calibri',15))
    whentogrowEntry.grid(row=6,column=1,pady=10,padx=10)

    submitButton=ttk.Button(new,text='Submit',command=post_data)
    submitButton.grid(row=7,columnspan=2)

def update(root,db):
    def update_data():
        global root
        SNE = serialnoEntry.get()
        ToS = typeofsoilEntry.get()
        CRE = cropsgrownEntry.get()
        WTG = whentogrowEntry.get()
        NE = nutrientEntry.get()
        DOE = dryingoutEntry.get()
        WRE = waterretentionEntry.get()
        if len(SNE)==0:
            messagebox.showwarning('Warning','Enter valid serial number')
            return
        if db.details.count_documents({'SN':SNE}, limit=1)==0:
            messagebox.showwarning('Error','Serial does not exist')
            return
        if len(ToS)!=0:
            db.details.update_one({'SN':SNE},{'$set':{'Type_of_soil':ToS}})
        if len(CRE)!=0:
            db.details.update_one({'SN':SNE},{'$set':{'Crops_grown':CRE}})
        if len(WTG)!=0:
            db.details.update_one({'SN':SNE},{'$set':{'When_to_grow':WTG}})
        if len(NE)!=0:
            db.details.update_one({'SN':SNE},{'$set':{'Nutrient_Content':NE}})
        if len(DOE)!=0:
            db.details.update_one({'SN':SNE},{'$set':{'Drying_out':DOE}})
        if len(WRE)!=0:
            db.details.update_one({'SN':SNE},{'$set':{'Water_retention':WRE}})
            messagebox.showinfo("Success",'Info updated successfully')
    new1=Toplevel(root)
    new1.geometry('530x450')
    new1.resizable(0,0)
    new1.title('Update info')
    serialnolabel=Label(new1,text='SN',font=('times new roman',20,'bold'))
    serialnolabel.grid(row=0,column=0,pady=10,padx=10)
    serialnoEntry=Entry(new1,font=('calibri',15))
    serialnoEntry.grid(row=0,column=1,pady=10,padx=10)

    typeofsoillabel=Label(new1,text='Type_of_Soil',font=('times new roman',20,'bold'))
    typeofsoillabel.grid(row=1,column=0,pady=10,padx=10)
    typeofsoilEntry=Entry(new1,font=('calibri',15))
    typeofsoilEntry.grid(row=1,column=1,pady=10,padx=10)

    cropsgrownlabel=Label(new1,text='Crops_grown',font=('times new roman',20,'bold'))
    cropsgrownlabel.grid(row=2,column=0,pady=10,padx=10)
    cropsgrownEntry=Entry(new1,font=('calibri',15))
    cropsgrownEntry.grid(row=2,column=1,pady=10,padx=10)

    nutrientlabel=Label(new1,text='Nutrient_content',font=('times new roman',20,'bold'))
    nutrientlabel.grid(row=3,column=0,pady=10,padx=10)
    nutrientEntry=Entry(new1,font=('calibri',15))
    nutrientEntry.grid(row=3,column=1,pady=10,padx=10)

    dryingoutlabel=Label(new1,text='Drying_out',font=('times new roman',20,'bold'))
    dryingoutlabel.grid(row=4,column=0,pady=10,padx=10)
    dryingoutEntry=Entry(new1,font=('calibri',15))
    dryingoutEntry.grid(row=4,column=1,pady=10,padx=10)

    waterretentionlabel=Label(new1,text='Water_retention',font=('times new roman',20,'bold'))
    waterretentionlabel.grid(row=5,column=0,pady=10,padx=10)
    waterretentionEntry=Entry(new1,font=('calibri',15))
    waterretentionEntry.grid(row=5,column=1,pady=10,padx=10)

    whentogrowlabel=Label(new1,text='When_to_grow',font=('times new roman',20,'bold'))
    whentogrowlabel.grid(row=6,column=0,pady=10,padx=10)
    whentogrowEntry=Entry(new1,font=('calibri',15))
    whentogrowEntry.grid(row=6,column=1,pady=10,padx=10)

    submitButton=ttk.Button(new1,text='Update',command=update_data)
    submitButton.grid(row=7,columnspan=2)

def dist_det(root,db):
    def dist_data():
        global root
        id=idEntry.get()
        name=nameEntry.get()
        email=emailEntry.get()
        contact=phoneEntry.get()
        gender=genderEntry.get()
        place=placeEntry.get()
        Id = [id]
        Name = [name]
        Email = [email]
        Contact = [contact]
        Gender = [gender]
        Place = [place]
        SoilFarming={
            'Id':Id[randint(0, (len(Id) - 1))],
            'Name':Name[randint(0, (len(Name) - 1))],
            'Email':Email[randint(0, (len(Email) - 1))],
            'Contact':Contact[randint(0, (len(Contact) - 1))],
            'Gender':Gender[randint(0, (len(Gender) - 1))],
            'Place':Place[randint(0, (len(Place) - 1))]
        }
        if (len(Id)==0):
            messagebox.showwarning('warning','Fields cannot be empty(Except:Email)')
            return
        if (len(name)==0):
            messagebox.showwarning('warning','Fields cannot be empty(Except:Email)')
            return
        if (len(contact)==0):
            messagebox.showwarning('warning','Fields cannot be empty(Except:Email)')
            return
        if (len(gender)==0):
            messagebox.showwarning('warning','Fields cannot be empty(Except:Email)')
            return
        if (len(place)==0):
            messagebox.showwarning('warning','Fields cannot be empty(Except:Email)')
            return
        if len(email)==0 and db.details.count_documents({'Id':id}, limit=1)==0:
            result=db.details.insert_one({'Id':id,'Name':name,'Place':place,'Gender':gender,'Contact':contact})
        elif len(email)!=0 and db.details.count_documents({'Id':id}, limit=1)==0:
            result=db.details.insert_one(SoilFarming)
            messagebox.showinfo('Success','Data added successfully')
        else:
            messagebox.showerror('Error','All details are required')
            return
    new2=Toplevel(root)
    new2.geometry('450x400')
    new2.resizable(0,0)
    new2.title('Distributive details')
    idlabel=Label(new2,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,pady=10,padx=10)
    idEntry=Entry(new2,font=('calibri',15))
    idEntry.grid(row=0,column=1,pady=10,padx=10)

    namelabel=Label(new2,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,pady=10,padx=10)
    nameEntry=Entry(new2,font=('calibri',15))
    nameEntry.grid(row=1,column=1,pady=10,padx=10)

    emaillabel=Label(new2,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=2,column=0,pady=10,padx=10)
    emailEntry=Entry(new2,font=('calibri',15))
    emailEntry.grid(row=2,column=1,pady=10,padx=10)

    phonelabel=Label(new2,text='Contact',font=('times new roman',20,'bold'))
    phonelabel.grid(row=3,column=0,pady=10,padx=10)
    phoneEntry=Entry(new2,font=('calibri',15))
    phoneEntry.grid(row=3,column=1,pady=10,padx=10)

    genderlabel=Label(new2,text='Gender',font=('times new roman',20,'bold'))
    genderlabel.grid(row=4,column=0,pady=10,padx=10)
    genderEntry=Entry(new2,font=('calibri',15))
    genderEntry.grid(row=4,column=1,pady=10,padx=10)

    placelabel=Label(new2,text='Place',font=('times new roman',20,'bold'))
    placelabel.grid(row=5,column=0,pady=10,padx=10)
    placeEntry=Entry(new2,font=('calibri',15))
    placeEntry.grid(row=5,column=1,pady=10,padx=10)

    submitButton=ttk.Button(new2,text='Submit',command=dist_data)
    submitButton.grid(row=6,columnspan=2)

def update_dist(rrot,db):
    def update():
        global root
        id=idEntry.get()
        name=nameEntry.get()
        email=emailEntry.get()
        contact=phoneEntry.get()
        gender=genderEntry.get()
        place=placeEntry.get()
        if len(id)==0:
            messagebox.showwarning('Warning','Enter valid id')
            return
        if db.details.count_documents({'Id':id},limit=1)==0:
            messagebox.showwarning('Warning','Id does not exist')
            return
        if len(name)!=0:
            db.details.update_one({'Id':id},{'$set':{'Name':name}})
        if len(email)!=0:
            db.details.update_one({'Id':id},{'$set':{'Email':email}})
        if len(contact)!=0:
            db.details.update_one({'Id':id},{'$set':{'Contact':contact}})
        if len(gender)!=0:
            db.details.update_one({'Id':id},{'$set':{'Gender':gender}})
        if len(place)!=0:
            db.details.update_one({'Id':id},{'$set':{'Place':place}})
            messagebox.showinfo("Success",'Details updated successfully')
    new3=Toplevel(root)
    new3.geometry('450x400')
    new3.resizable(0,0)
    new3.title('Distributive details')
    idlabel=Label(new3,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,pady=10,padx=10)
    idEntry=Entry(new3,font=('calibri',15))
    idEntry.grid(row=0,column=1,pady=10,padx=10)

    namelabel=Label(new3,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,pady=10,padx=10)
    nameEntry=Entry(new3,font=('calibri',15))
    nameEntry.grid(row=1,column=1,pady=10,padx=10)

    emaillabel=Label(new3,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=2,column=0,pady=10,padx=10)
    emailEntry=Entry(new3,font=('calibri',15))
    emailEntry.grid(row=2,column=1,pady=10,padx=10)

    phonelabel=Label(new3,text='Contact',font=('times new roman',20,'bold'))
    phonelabel.grid(row=3,column=0,pady=10,padx=10)
    phoneEntry=Entry(new3,font=('calibri',15))
    phoneEntry.grid(row=3,column=1,pady=10,padx=10)

    genderlabel=Label(new3,text='Gender',font=('times new roman',20,'bold'))
    genderlabel.grid(row=4,column=0,pady=10,padx=10)
    genderEntry=Entry(new3,font=('calibri',15))
    genderEntry.grid(row=4,column=1,pady=10,padx=10)

    placelabel=Label(new3,text='Place',font=('times new roman',20,'bold'))
    placelabel.grid(row=5,column=0,pady=10,padx=10)
    placeEntry=Entry(new3,font=('calibri',15))
    placeEntry.grid(row=5,column=1,pady=10,padx=10)

    submitButton=ttk.Button(new3,text='Update',command=update)
    submitButton.grid(row=6,columnspan=2)

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('300x450+150+150')
root.resizable(0,0)
root.title('Admin window')

postButton=ttk.Button(root,text='Post soil details',width=25,compound=CENTER,command=lambda: soil_det(root,db))
postButton.grid(row=0,column=0,pady=20,padx=10)

updateButton=ttk.Button(root,text='Update soil details',width=25,compound=CENTER,command=lambda: update(root,db))
updateButton.grid(row=1,column=0,pady=20,padx=10)

postdisButton=ttk.Button(root,text='Post distributor det',width=25,compound=CENTER,command=lambda: dist_det(root,db))
postdisButton.grid(row=2,column=0,pady=20,padx=10)

updatedisButton=ttk.Button(root,text='Update dist details',width=25,compound=CENTER,command=lambda: update_dist(root,db))
updatedisButton.grid(row=3,column=0,pady=20,padx=10)

exitButton=ttk.Button(root,text='Exit',width=25,compound=CENTER,command=exit)
exitButton.grid(row=4,column=0,pady=20,padx=10)

root.mainloop()