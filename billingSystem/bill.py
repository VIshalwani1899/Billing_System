from tkinter import *
import math,random,os
from tkinter import  messagebox


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        # self.root.title("Billing System")
        self.root.title("vishal wani")

        bg_color="#074463"
        # bg_color = "#4C787E"
        title=Label(self.root,text="RETAIL SHOP",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #----------VARIABLES--------------
        #----------COSMETICS--------------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

        #----------GROCERY----------------

        self.rice=IntVar()
        self.foodoil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #----------cold drinks-------------
        self.maza=IntVar()
        self.limca=IntVar()
        self.slice=IntVar()
        self.cococola=IntVar()
        self.pepsi=IntVar()
        self.redbull=IntVar()


        #------------customer--------------
        self.cname=StringVar()
        self.phone=StringVar()
        self.billno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set(str(x))
        self.searchbill=StringVar()


        #-----------total price----------

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.colddrinks_price=StringVar()


        #----------tax-------------
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.colddrinks_tax=StringVar()


 #-----customer details parent frame---------

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman", 18, "bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.cname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)


        cphone_label=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)


        cbill_label=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.searchbill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #---------cosmetics-------------

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 18, "bold"),fg="gold", bg=bg_color)
        F2.place(x=0, y=180,width=320,height=380)

        bath_label = Label(F2, text="Bath Soap", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10,sticky="w")
        bath_txt = Entry(F2, width=10,textvariable=self.soap, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Facecream_label = Label(F2, text="Face Cream", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Facecream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Facewash_label = Label(F2, text="Face Wash", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Facewash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,   padx=10, pady=10)

        Hairs_label = Label(F2, text="Hair Sparay", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hairs_txt = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hairgel_label = Label(F2, text="Hair Gel", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hairgel_txt = Entry(F2, width=10,textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        bodyl_label = Label(F2, text="Body Lotion", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        bodyl_txt = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        #-----------grocery------------




        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Groceries", font=("times new roman", 18, "bold"),fg="gold", bg=bg_color)
        F3.place(x=320, y=180,width=320,height=380)

        g0_label = Label(F3, text="Rice", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10,sticky="w")
        g0_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g1_label = Label(F3, text="Food Oil", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.foodoil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        g2_label = Label(F3, text="Daal", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,   padx=10, pady=10)

        g3_label = Label(F3, text="Wheat", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        g4_label = Label(F3, text="Sugar", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        g5_label = Label(F3, text="Tea", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)


        #------cold drinks----------


        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 18, "bold"),fg="gold", bg=bg_color)
        F4.place(x=640, y=180,width=320,height=380)

        c1_label = Label(F4, text="Maaaza", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10,sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_label = Label(F4, text="Limca", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        c3_label = Label(F4, text="Slice", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.slice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,   padx=10, pady=10)

        c4_label = Label(F4, text="Coco Cola", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.cococola, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        c5_label = Label(F4, text="Pepsi", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.pepsi, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        c6_label = Label(F4, text="Redbull", bg=bg_color, fg="lightgreen",font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.redbull, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        #---------Bill Area-----------

        F5= Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=960, y=180, width=323, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)

        #scrollbar

        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)



        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 18, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=557,relwidth=1,height=140)

        m1_label=Label(F6,bg=bg_color,fg="white",text="Total Cosmetic Price",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


        m2_label=Label(F6,bg=bg_color,fg="white",text="Total Grocery Price",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,textvariable=self.grocery_price,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)


        m3_label=Label(F6,bg=bg_color,fg="white",text="Total Cold drinks Price",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,textvariable=self.colddrinks_price,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        T1_label=Label(F6,bg=bg_color,fg="white",text="Cosmetic Tax",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        T1_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,textvariable=self.cosmetic_tax,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)


        T2_label=Label(F6,bg=bg_color,fg="white",text="Grocery Tax",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        T2_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,textvariable=self.grocery_tax,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)


        T3_label=Label(F6,bg=bg_color,fg="white",text="Cold drinks Tax",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        T3_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,textvariable=self.colddrinks_tax,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


        btn_frame=Frame(F6,bd=7,relief=GROOVE)
        btn_frame.place(x=750,width=510,height=101)

        total_btn=Button(btn_frame,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=8,font="arail 15 bold",bd=2).grid(row=0,column=0,padx=6,pady=5)
        Gbill_btn=Button(btn_frame,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=10,font="arail 15 bold",bd=2).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_frame,text="Clear",command=self.clear_bill,bg="cadetblue",fg="white",pady=15,width=8,font="arail 15 bold",bd=2).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_frame,text="Exit",command=self.Exit,bg="cadetblue",fg="white",pady=15,width=8,font="arail 15 bold",bd=2).grid(row=0,column=3,padx=5,pady=5)


    def total(self):
        self.soap_price=self.soap.get()*40
        self.face_cream_price=self.face_cream.get() * 120
        self.face_wash_price=self.face_wash.get() * 180
        self.gel_price=self.gel.get() * 60
        self.spray_price=self.spray.get() * 400
        self.lotion_price=self.lotion.get() * 200

        self.total_cosmetic_price=float(
            self.soap_price+
            self.face_cream_price +
            self.face_wash_price +
            self.gel_price +
            self.spray_price +
            self.lotion_price

        )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.rice_price=self.rice.get() * 60
        self.foodoil_price=self.foodoil.get() * 250
        self.daal_price=self.daal.get() * 100
        self.tea_price=self.tea.get() * 320
        self.wheat_price=self.wheat.get() * 50
        self.sugar_price=self.sugar.get() * 45

        self.total_grocery_price = float(
             self.rice_price +
             self.foodoil_price+
             self.daal_price +
             self.tea_price +
             self.wheat_price+
             self.sugar_price


        )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.maza_price=self.maza.get() * 70
        self.limca_price=self.limca.get() * 40
        self.slice_price=self.slice.get() * 90
        self.cococola_price=self.cococola.get() * 60
        self.pepsi_price=self.pepsi.get() * 50
        self.redbull_price=self.redbull.get() * 150


        self.total_colddrinks_price = float(
             self.maza_price+
             self.limca_price +
             self.slice_price+
             self.cococola_price+
             self.pepsi_price+
             self.redbull_price


        )

        self.colddrinks_price.set("Rs. "+str(self.total_colddrinks_price))
        self.cd_tax=round((self.total_colddrinks_price * 0.15), 2)
        self.colddrinks_tax.set("Rs. "+str(self.cd_tax))


        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_colddrinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax
                              )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"      Welcome to riddhi foods")
        self.txtarea.insert(END,f"\n\n Bill Number : {self.billno.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.cname.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.phone.get()}")
        self.txtarea.insert(END,"\n===================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t  Price")
        self.txtarea.insert(END, "\n===================================")

    def bill_area(self):
        self.welcome_bill()

        if self.cname.get()=="" or self.phone.get()=="":
            messagebox.showerror("Error","Fill the Customer details!")

        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.colddrinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","no product has selected")

        else:

            #-----------cosmetics---------------
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t Rs. {self.soap_price}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t Rs. {self.face_cream_price}")


            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t Rs. {self.face_wash_price}")


            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gel.get()}\t Rs. {self.gel_price}")

            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t Rs. {self.spray_price}")

            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t Rs. {self.lotion_price}")




            #------------grocery--------------
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t Rs. {self.rice_price}")

            if self.foodoil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.foodoil.get()}\t Rs. {self.foodoil_price}")

            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t Rs. {self.daal_price}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t Rs. {self.wheat_price}")


            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t Rs. {self.sugar_price}")



            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t Rs. {self.tea_price}")


            #-----------cold drinks---------------

            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.maza.get()}\t Rs. {self.maza_price}")

            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t Rs. {self.limca_price}")

            if self.slice.get()!=0:
                self.txtarea.insert(END,f"\n Slice\t\t{self.slice.get()}\t Rs. {self.slice_price}")

            if self.cococola.get()!=0:
                self.txtarea.insert(END,f"\n CocoCola\t\t{self.cococola.get()}\t Rs. {self.cococola_price}")

            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t Rs. {self.pepsi_price}")

            if self.redbull.get()!=0:
                self.txtarea.insert(END,f"\n RedBull\t\t{self.redbull.get()}\t Rs. {self.redbull_price}")



            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, "\n-----------------------------------")
                self.txtarea.insert(END,f"\n Cosmetic Tax   \t\t\t {self.cosmetic_tax.get()}")


            if self.grocery_tax.get()!="Rs. 0.0":

                self.txtarea.insert(END,f"\n Grocery Tax    \t\t\t {self.grocery_tax.get()}")



            if self.colddrinks_tax.get()!="Rs. 0.0":

                self.txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t {self.colddrinks_tax.get()}")
                self.txtarea.insert(END, "\n-----------------------------------")

            self.txtarea.insert(END, f"\n Total Bill\t\t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END, "\n-----------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save","you want to save this bill?")
        if op>0:

            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.billno.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved successfully",f"Bill no. {self.billno.get()} saved succssfully")
        else:
            return


    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.searchbill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("Error","INVALID BILL NUMBER")

    def clear_bill(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")

        if op > 0:

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            # ----------GROCERY----------------

            self.rice.set(0)
            self.foodoil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ----------cold drinks-------------
            self.maza.set(0)
            self.limca.set(0)
            self.slice.set(0)
            self.cococola.set(0)
            self.pepsi.set(0)
            self.redbull.set(0)

            # ------------customer--------------
            self.cname.set("")
            self.phone.set("")
            self.billno.set("")
            x = random.randint(1000, 9999)
            self.billno.set(str(x))
            self.searchbill.set("")

            # -----------total price----------

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.colddrinks_price.set("")

            # ----------tax-------------
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.colddrinks_tax.set("")

            self.welcome_bill()

    def Exit(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")

        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)

root.mainloop()