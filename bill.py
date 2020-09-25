from tkinter import *
import math,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#800080"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Chalkduster",30,"bold"),pady=2).pack(fill=X)
        #============Variables=================

        #===========Cosmetics=========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #==========grocery============
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #=============Cold Drinks================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #===============Total Product Price Tax Variable+++++++
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #================Customer
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        #=============Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details :- ",font=("Chalkduster",20,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name :-",bg=bg_color,fg="white",font=("Times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=18,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No. :-", bg=bg_color, fg="white", font=("Times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=18,textvariable=self.c_phon,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number :-", bg=bg_color, fg="white", font=("Times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=18,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=15)

        #==============Cosmetics Frame
        F2=LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics :- ", font=("Chalkduster", 20, "bold"),fg="gold", bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)

        Bath_lbl=Label(F2,text="Bath Soap",font=("Bradley Hand",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("Bradley Hand",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,pady=10, padx=10)

        Face_wash_lbl = Label(F2, text="Face Wash", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_wash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,pady=10, padx=10)

        Hair_spray_lbl = Label(F2, text="Hair Spray", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_spray_txt = Entry(F2, width=10,textvariable=self.spray, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,pady=10, padx=10)

        Hair_gel_lbl = Label(F2, text="Hair Gel", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_gel_txt = Entry(F2, width=10,textvariable=self.gell, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,pady=10, padx=10)

        Body_loshan_lbl = Label(F2, text="Body Loshan", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_loshan_txt = Entry(F2, width=10,textvariable=self.loshan, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,pady=10, padx=10)

        #==============Grocery Frame
        F3=LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery :- ", font=("Chalkduster", 20, "bold"),fg="gold", bg=bg_color)
        F3.place(x=340, y=180,width=325,height=380)

        rice_lbl=Label(F3,text="Rice",font=("Bradley Hand",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("Bradley Hand",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        Food_oil_lbl = Label(F3, text="Food Oil", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Food_oil_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,pady=10, padx=10)

        daal_lbl = Label(F3, text="Daal", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_txt = Entry(F3, width=10,textvariable=self.daal ,font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,pady=10, padx=10)

        wheat_lbl = Label(F3, text="Wheat", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_txt = Entry(F3, width=10,textvariable=self.wheat ,font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,pady=10, padx=10)

        sugar_lbl = Label(F3, text="Sugar", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_txt = Entry(F3, width=10,textvariable=self.sugar ,font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,pady=10, padx=10)

        tea_lbl = Label(F3, text="Tea", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_txt = Entry(F3, width=10, textvariable=self.tea,font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,pady=10, padx=10)

        #==============Cold Drinks Frame
        F4=LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks :- ", font=("Chalkduster", 20, "bold"),fg="gold", bg=bg_color)
        F4.place(x=675, y=180,width=325,height=380)

        maza_lbl=Label(F4,text="Maza",font=("Bradley Hand",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("Bradley Hand",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        cock_oil_lbl = Label(F4, text="Cock", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cock_oil_txt = Entry(F4, width=10,textvariable=self.cock, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,pady=10, padx=10)

        frooti_lbl = Label(F4, text="Frooti", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        frooti_txt = Entry(F4, width=10,textvariable=self.frooti,font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,pady=10, padx=10)

        thumbs_lbl = Label(F4, text="Thumbs UP", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        thumbs_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,pady=10, padx=10)

        limca_lbl = Label(F4, text="Limca", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_txt = Entry(F4, width=10,textvariable=self.limca, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,pady=10, padx=10)

        sprite_lbl = Label(F4, text="Sprite", font=("Bradley Hand", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_txt = Entry(F4, width=10,textvariable=self.sprite, font=("Bradley Hand", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,pady=10, padx=10)

        #==================Bill Area
        F5=Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=420, height=380)
        bill_title=Label(F5,text="Bill Area",font="Chalkduster 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===========Button Frame===============
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu :- ", font=("Chalkduster", 20, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=570, relwidth=1, height=320)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("Chalkduster",14,"bold")).grid(row=0,column=0,padx=20,pady=20,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=20)

        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("Chalkduster",14,"bold")).grid(row=1,column=0,padx=20,pady=20,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=20,pady=20)

        m3 = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white", font=("Chalkduster", 14, "bold")).grid(row=2, column=0, padx=20, pady=20, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 15 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=20, pady=20)

        c1=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("Chalkduster",14,"bold")).grid(row=0,column=2,padx=20,pady=20,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=20)

        c2=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("Chalkduster",14,"bold")).grid(row=1,column=2,padx=20,pady=20,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=20,pady=20)

        c3 = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="white", font=("Chalkduster", 14, "bold")).grid(row=2, column=2, padx=20, pady=20, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 15 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=20, pady=20)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=850,width=560,height=265)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="Magenta",fg="Blue",pady=20,width=18,bd=6,font="arial 18 bold").grid(row=0,column=0,padx=10,pady=10)
        Generate_bill_btn=Button(btn_F,command=self.welcome_bill,text="Genetate Bill",bg="Magenta",fg="Blue",pady=20,width=18,bd=6,font="arial 18 bold").grid(row=0,column=1,padx=10,pady=10)
        Clear_btn=Button(btn_F,text="Clear",bg="Magenta",fg="Blue",pady=20,width=18,bd=6,font="arial 18 bold").grid(row=1,column=0,padx=10,pady=10)
        Exit_btn=Button(btn_F,text="Exit",bg="Magenta",fg="Blue",pady=20,width=18,bd=6,font="arial 18 bold").grid(row=1,column=1,padx=10,pady=10)
        self.welcome_bill()


    def total(self):
        self.total_cosmetics_price=float(
                                    (self.soap.get()*40)+
                                    (self.face_cream.get()*120)+
                                    (self.face_wash.get()*60)+
                                    (self.spray.get()*180)+
                                    (self.gell.get()*140)+
                                    (self.loshan.get()*180)
                                    )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetics_price))
        self.cosmetics_tax.set("Rs. "+str(round((self.total_cosmetics_price*0.05),2)))

        self.total_grocery_price = float(
                                    (self.rice.get() *80) +
                                    (self.food_oil.get() * 180) +
                                    (self.daal.get() * 60) +
                                    (self.wheat.get() * 240) +
                                    (self.sugar.get() * 45) +
                                    (self.tea.get() * 150)
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.grocery_tax.set("Rs. "+str(round((self.total_grocery_price*0.1),2)))


        self.total_drink_price = float(
                                    (self.maza.get() * 60) +
                                    (self.cock.get() * 60) +
                                    (self.frooti.get() * 50) +
                                    (self.thumbsup.get() *45) +
                                    (self.limca.get() * 40) +
                                    (self.sprite.get() * 70)
                                    )
        self.cold_drink_price.set("Rs. "+str(self.total_drink_price))
        self.cold_drink_tax.set("Rs. "+str(round((self.total_drink_price*0.05),2)))

    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t \tWelcome Webcode Retail \n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n ================================================")
        self.txtarea.insert(END, f"\n Produts \t\t\t QTY \t\t\t Price")
        self.txtarea.insert(END, f"\n ================================================")


    def bill_area(self):
        self.welcome_bill()
        if self.soap.get()!=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t\t{self.soap.get()}")


root=Tk()
obj=Bill_App(root)
root.mainloop()
