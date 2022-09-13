



from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox


total = 0                  
cash = 0                   
change = 0                  



def Exit():                 #function of exit button in the main window
    Exit = tkinter.messagebox.askyesno("Ordering System For Chilled Taho Express and Fries", "Do you want to exit?")
    if Exit > 0:            #if the user press YES in the message box
        window.destroy()    #destroy () - used to closed the window
        return
    
#OK button - ORDER frame=================
def calculate():            #function for OK button in Order Frame
    try:                    #for exception handling
        #global t1 to t8,total_t1 to total_t8 - can be a single line declaration
        global t1            #quantity input for classic
        global t2            #quantity input for oreo
        global t3            #quantity input for yema
        global t4            #quantity input for milky choco
        global t5            #quantity input for classic and fries
        global t6            #quantity input for oreo and fries
        global t7            #quantity input for yema and fries
        global t8            #quantity input for milky choco and 
        global t9            #quantity input for reg fries
        global t10           #quantity input for med fries
        global t11           #quantity input for large fries
        global t12           #quantity input for add ons
        global total_t1      #total amount of order for classic
        global total_t2      #total amount of order for oreo
        global total_t3      #total amount of order for yema
        global total_t4      #total amount of order for milky choco
        global total_t5      #total amount for classic and fries
        global total_t6      #total amount for oreo and fries
        global total_t7      #total amount for yema and fries
        global total_t8      #total amount for milky choco and fries
        global total_t9      #total amount for reg fries
        global total_t10     #total amount for med fries
        global total_t11     #total amount for large fries
        global total_t12     #total amount for add ons
        
        global total         #total amount of all orders
        
        total_t1 = 0         #initial value of the total amount of order for classic
        total_t2 = 0         #initial value of the total amount of order for oreo
        total_t3 = 0         #initial value of the total amount of order for yema
        total_t4 = 0         #initial value of the total amount of order for milky choco
        total_t5 = 0         #initial value of the total amount of order for classic+fries
        total_t6 = 0         #initial value of the total amount of order for oreo+fries
        total_t7 = 0         #initial value of the total amount of order for yema+fries
        total_t8 = 0         #initial value of the total amount of order for milky choco+fries
        total_t9 = 0         #initial value of the total amount of order for reg fries
        total_t10 = 0        #initial value of the total amount of order for med fries
        total_t11 = 0        #initial value of the total amount of order for lrg fries
        total_t12 = 0        #initial value of the total amount of order for add ons
    
        if cb1.get() :                   #if checkbutton in checked, get the state of checkbutton, onvalue = 1
            t1 = txtt1.get()               #get the input of quantity from the Entrybox/Textbox named txtt1(classic)
            total_t1 = (int(t1)*60)       #compute for the total amount for classic taho from quantity input(b)*50(price of classic)
            xt1 = str(t1) + "     -----     " + "PHP " + str(total_t1) #Conversion of integer to string type to be able to display on label
            lbt1 = Label(lf_orderPre, text = xt1) #Display of the summary of order for classic taho
            lbt1.place(x=200, y = 10)             #location of the label 
        else:                            #if checkbutton in unchecked
            txtt1.insert(0, 0)            #Entrybox/Textbox is 0, no quantity should be entered     
            lbt1 = Label(lf_orderPre, text = 0) #Display of summary should also be 0, no order was made
            lbt1.place(x=200, y = 10)
        
        if cb2.get():
            t2 = txtt2.get()
            total_t2 = (int(t2)*75)
            xt2 = str(t2) + "     -----     " + "PHP " + str(total_t2)
            lbt2 = Label(lf_orderPre,text = xt2)
            lbt2.place(x=200, y = 25)
        else:
            txtt2.insert(0, 0)
            lbt2 = Label(lf_orderPre, text = 0)
            lbt2.place(x=200, y = 25)
        
        if cb3.get():
            t3 = txtt3.get()
            total_t3 = (int(t3)*75)
            xt3 = str(t3) + "     -----     " + "PHP " + str(total_t3)
            lbt3 = Label(lf_orderPre, text = xt3)
            lbt3.place(x=200, y = 40)
        else:
            txtt3.insert(0, 0)
            lbt3 = Label(lf_orderPre, text = 0)
            lbt3.place(x=200, y = 40)
        
        if cb4.get():
            t4 = txtt4.get()
            total_t4 = (int(t4)*75)
            xt4 = str(t4) + "     -----     " + "PHP " + str(total_t4)
            lbt4 = Label(lf_orderPre, text = xt4)
            lbt4.place(x=200, y = 55)
        else:
            txtt4.insert(0, 0)
            lbt4 = Label(lf_orderPre, text = 0)
            lbt4.place(x=200, y = 55)
            
        if cb5.get():
            t5 = txtt5.get()
            total_t5 = (int(t5)*75)
            xt5 = str(t5) + "     -----     " + "PHP " + str(total_t5)
            lbt5 = Label(lf_orderPre, text = xt5)
            lbt5.place(x=200, y = 70)
        else:
            txtt5.insert(0, 0)
            lbt5 = Label(lf_orderPre, text = 0)
            lbt5.place(x=200, y = 70)
            
        if cb6.get():
            t6 = txtt6.get()
            total_t6 = (int(t6)*95)
            xt6 = str(t6) + "     -----     " + "PHP " + str(total_t6)
            lbt6 = Label(lf_orderPre, text = xt6)
            lbt6.place(x=200, y = 85)
        else:
            txtt6.insert(0, 0)
            lbt6 = Label(lf_orderPre, text = 0)
            lbt6.place(x=200, y = 85)
            
        if cb7.get():
            t7 = txtt7.get()
            total_t7 = (int(t7)*95)
            xt7 = str(t7) + "     -----     " + "PHP " + str(total_t7)
            lbt7 = Label(lf_orderPre, text = xt7)
            lbt7.place(x=200, y = 100)
        else:
            txtt7.insert(0, 0)
            lbt7 = Label(lf_orderPre, text = 0)
            lbt7.place(x=200, y = 100)
            
        if cb8.get():
            t8 = txtt8.get()
            total_t8 = (int(t8)*95)
            xt8 = str(t8) + "     -----     " + "PHP " + str(total_t8)
            lbt8 = Label(lf_orderPre, text = xt8)
            lbt8.place(x=200, y = 115)
        else:
            txtt8.insert(0, 0)
            lbt8 = Label(lf_orderPre, text = 0)
            lbt8.place(x=200, y = 115)
            
        if cb9.get():
            t9 = txtt9.get()
            total_t9 = (int(t9)*25)
            xt9 = str(t9) + "     -----     " + "PHP " + str(total_t9)
            lbt9 = Label(lf_orderPre, text = xt9)
            lbt9.place(x=200, y = 130)
        else:
            txtt9.insert(0, 0)
            lbt9 = Label(lf_orderPre, text = 0)
            lbt9.place(x=200, y = 130)
            
        if cb10.get():
            t10 = txtt10.get()
            total_t10 = (int(t10)*45)
            xt10 = str(t10) + "     -----     " + "PHP " + str(total_t10)
            lbt10 = Label(lf_orderPre, text = xt9)
            lbt10.place(x=200, y = 145)
        else:
            txtt10.insert(0, 0)
            lbt10 = Label(lf_orderPre, text = 0)
            lbt10.place(x=200, y = 145)
            
        if cb11.get():
            t11 = txtt11.get()
            total_t11 = (int(t11)*65)
            xt11 = str(t11) + "     -----     " + "PHP " + str(total_t11)
            lbt11 = Label(lf_orderPre, text = xt11)
            lbt11.place(x=200, y = 160)
        else:
            txtt11.insert(0, 0)
            lbt11 = Label(lf_orderPre, text = 0)
            lbt11.place(x=200, y = 160)
            
        if cb12.get():
            t12 = txtt12.get()
            total_t12 = (int(t12)*10)
            xt12 = str(t12) + "     -----     " + "PHP " + str(total_t12)
            lbt12 = Label(lf_orderPre, text = xt12)
            lbt12.place(x=200, y = 175)
        else:
            txtt12.insert(0, 0)
            lbt12 = Label(lf_orderPre, text = 0)
            lbt12.place(x=200, y = 175)
            
        total = total_t1 + total_t2 + total_t3 + total_t4 + total_t5 + total_t6 + total_t7 + total_t8 + total_t9 + total_t10 + total_t11 + total_t12 #computation of total amount for all orders
        txtT = Entry(lf_payment)                        #Entrybox/Textbox for the display of total
        txtT.insert(0, total)                           #instert() is used to insert the value of 'total' in the EntryBox/Textbox
        txtT.place(x = 150, y = 50)                     #location of Entrybox/Textbox for total
    except ValueError:      #Exception handled if the user enters an invalid input              
        invalid = tkinter.messagebox.showerror("Ordering System", "Invalid Input! Please try again!")
        
    
#CLEAR button - ORDER frame======================
def clear():    #function to clear all the selection of checkButton and make the Entrybox/TextBox and Label Empty

    #check button
    cbt1.deselect()          #deselect() is used to unchecked the CheckButton
    cbt2.deselect()
    cbt3.deselect()
    cbt4.deselect()
    cbt5.deselect()
    cbt6.deselect()
    cbt7.deselect()
    cbt8.deselect()
    cbt9.deselect()
    cbt10.deselect()
    cbt11.deselect()
    cbt12.deselect()
    
    #textbox input
    txtt1.delete(0, "end")   #delete() is used delete the content of Entrybox/Textbox from index 0 to end
    txtt2.delete(0, "end")
    txtt3.delete(0, "end")
    txtt4.delete(0, "end")
    txtt5.delete(0, "end")
    txtt6.delete(0, "end")
    txtt7.delete(0, "end")
    txtt8.delete(0, "end")
    txtt9.delete(0, "end")
    txtt10.delete(0, "end")
    txtt11.delete(0, "end")
    txtt12.delete(0, "end")
    
    #label preview
    lbt1 = Label(lf_orderPre, text = "              ")  #set text to empty the label
    lbt1.place(x=200, y = 10)
    lbt2 = Label(lf_orderPre,text = "               ")
    lbt2.place(x=200, y = 25)
    lbt3 = Label(lf_orderPre,text = "               ")
    lbt3.place(x=200, y = 40)
    lbt4 = Label(lf_orderPre,text = "               ")
    lbt4.place(x=200, y = 55)
    lbt5 = Label(lf_orderPre,text = "               ")
    lbt5.place(x=200, y = 70)
    lbt6 = Label(lf_orderPre,text = "               ")
    lbt6.place(x=200, y = 85)
    lbt7 = Label(lf_orderPre,text = "               ")
    lbt7.place(x=200, y = 100)
    lbt8 = Label(lf_orderPre,text = "               ")
    lbt8.place(x=200, y = 115)
    lbt9 = Label(lf_orderPre,text = "               ")
    lbt9.place(x=200, y = 130)
    lbt10 = Label(lf_orderPre,text = "               ")
    lbt10.place(x=200, y = 145)
    lbt11 = Label(lf_orderPre,text = "               ")
    lbt11.place(x=200, y = 160)
    lbt12 = Label(lf_orderPre,text = "               ")
    lbt12.place(x=200, y = 175)

    #textbox total output
    txtT = Entry(lf_payment)
    txtT.delete(0, "end")
    txtT.place(x = 150, y = 50)
    
#OK button - PAYMENT frame=======================
def bill():             #function for OK button in Payment Frame 
    global cash
    global change
    
    cash = int(txtCash.get())       #get the input of cash from the Entrybox/Textbox named txtCash
    change = (int(cash - total))    #computation of change   
    if change >= 0:                 #if change is positive or cash > total
        txtChange = Entry(lf_payment)
        txtChange.insert(0, change)     #dsiplay the computed change
        txtChange.place(x = 150, y = 180)
        lb_bill = Label (lf_bill, text = "THANK YOU FOR BUYING @ TAHO EXPRESS!", font = "verdana 10 bold") #Display the message THANK YOU in the blank frame
        lb_bill.place(x=10, y=10 )
        
        xcash = "Cash :" + "     -----     " + "PHP " + str(cash) #Conversion of integer to string type to be able to display on label
        lcash = Label(lf_bill, text = xcash, font = "verdana")
        lcash.place(x=10, y = 40)
        
        xchange = "Change :" + "     -----     " + "PHP " + str(change) #Conversion of integer to string type to be able to display on label
        lchange = Label(lf_bill, text = xchange, font = "verdana")
        lchange.place(x=10, y = 120)
        
        xtotal = "Total Amount :" + "     -----     " + "PHP " + str(total) #Conversion of integer to string type to be able to display on label
        ltotal = Label(lf_bill, text = xtotal, font = "verdana")
        ltotal.place(x=10, y = 80)

        lreceipt = Label(lf_bill, text = "---RECEIPT---", font = "verdana 8 bold")
        lreceipt.place(x=130, y = 180)
        
    else:                           #if change is negative or cash < total, display the message INSUFFICIENT AMOUNT
        lb_bill = Label (lf_bill, text = "INSUFFICIENT AMOUNT!", font = "verdana 20 bold") 
        lb_bill.place(x=8, y= 50)
        
    
#NEW ORDER - PAYMENT frame======================
def newOrder():         #function for New Order or to clear all the selection of checkButton and make the Entrybox/TextBox and Label Empty
    #check button
    cbt1.deselect()
    cbt2.deselect()
    cbt3.deselect()
    cbt4.deselect()
    cbt5.deselect()
    cbt6.deselect()
    cbt7.deselect()
    cbt8.deselect()
    cbt9.deselect()
    cbt10.deselect()
    cbt11.deselect()
    cbt12.deselect()

    #textbox input
    txtt1.delete(0, "end")
    txtt2.delete(0, "end")
    txtt3.delete(0, "end")
    txtt4.delete(0, "end")
    txtt5.delete(0, "end")
    txtt6.delete(0, "end")
    txtt7.delete(0, "end")
    txtt8.delete(0, "end")
    txtt9.delete(0, "end")
    txtt10.delete(0, "end")
    txtt11.delete(0, "end")
    txtt12.delete(0, "end")
    
    #label preview
    lbt1 = Label(lf_orderPre, text = "                                        ")  #set text to empty the label
    lbt1.place(x=200, y = 10)
    lbt2 = Label(lf_orderPre,text = "                                         ")
    lbt2.place(x=200, y = 25)
    lbt3 = Label(lf_orderPre,text = "                                         ")
    lbt3.place(x=200, y = 40)
    lbt4 = Label(lf_orderPre,text = "                                         ")
    lbt4.place(x=200, y = 55)
    lbt5 = Label(lf_orderPre,text = "                                         ")
    lbt5.place(x=200, y = 70)
    lbt6 = Label(lf_orderPre,text = "                                         ")
    lbt6.place(x=200, y = 85)
    lbt7 = Label(lf_orderPre,text = "                                         ")
    lbt7.place(x=200, y = 100)
    lbt8 = Label(lf_orderPre,text = "                                         ")
    lbt8.place(x=200, y = 115)
    lbt9 = Label(lf_orderPre,text = "                                         ")
    lbt9.place(x=200, y = 130)
    lbt10 = Label(lf_orderPre,text = "                                        ")
    lbt10.place(x=200, y = 145)
    lbt11 = Label(lf_orderPre,text = "                                        ")
    lbt11.place(x=200, y = 160)
    lbt12 = Label(lf_orderPre,text = "                                        ")
    lbt12.place(x=200, y = 175)

    #textbox output
    txtT = Entry(lf_payment)
    txtT.delete(0, "end")
    total = 0
    txtT.place(x = 150, y = 50)
    txtCash.delete(0, "end")
    cash = 0
    txtChange = Entry(lf_payment)
    txtChange.delete(0, "end")
    txtChange.place(x = 150, y = 180)

    #label output
    lb_bill = Label (lf_bill, text = "\n                        \n                       \n                        \n                        \n                         ", font = "times 20 bold")
    lb_bill.place(x=1, y= 500)


#--------------------------------------------------------DESIGN---------------------------------------
#Design legend:
    #Main window(1st layer) - ============
    #Sub layers (2nd layer) - ************
    #Subs of Sub(3rd layer) - +++++++++++
    
#Window=============================================================================================
window  = Tk()                  #TK() is a function for creating a tkinter window, window is the variable
window.title("Chilled Taho Express And Fries™") #title() is used to assign title of your window, string parameter inside the parenthesis is the title
window.geometry("800x700")      #geometry() function is used to set the preferred size of the window
window.configure(background="#fffdd0")
#window.configure(background="light brown") #configure() for other option like background color


#Label - Title *******************************************************
#variableName = Label (master location, option,......)
title = Label(window, text="Chilled Taho Express and Fries™", font = "verdana 13 bold",fg = "green", background = "#fffdd0")
title.place(x=250,y=3) #place(x,y) - position of widgets


#Button - Exit ********************************************************
#variableName = Button (master location, option,......command = button function name)
btnExit = Button(window, text = "Exit", width = 5, bg = "red", fg = "white",font = "verdana" , command = Exit)
btnExit.place(x=730,y=5)

#LabelFrame=========================================================================================

#Label Frame1 - ORDER ***********************************************
#variableName = LabelFrame (master location, option,......)
lf_order = LabelFrame(window, width = 400,height = 660, bd = 8, text = "ORDER", font = "bold")
lf_order.place(x=0,y=35)

#CheckButton - Menu Choices +++++++++++++++++++++++++++++++++++++++
#initialization of variables for the on/off value of Checkbutton
cb1 = IntVar() #for classic Checkbutton
cb2 = IntVar() #for oreo Checkbutton
cb3 = IntVar() #for yema Checkbutton
cb4 = IntVar() #for milky choco Checkbutton
cb5 = IntVar() #for classic+fries Checkbutton
cb6 = IntVar() #for oreo+fries Checkbutton
cb7 = IntVar() #for yema+fries Checkbutton
cb8 = IntVar() #for milky choco+fries Checkbutton
cb9 = IntVar() #for reg fries Checkbutton
cb10 = IntVar() #for med fries Checkbutton
cb11 = IntVar() #for lrg fries Checkbutton
cb12 = IntVar() #for reg add ons Checkbutton

#variableName = CheckButton(master location, option,......, variable, onvalue=1, offvalue = 1)
cbt1 = Checkbutton(lf_order, text = "A - CLASSIC: PHP 60", font = "fixedsys", variable = cb1, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt1.place(x=10, y = 10 )
txtt1 = Entry(lf_order)  #EntryBox/Textbox for quantity input
txtt1.place(x = 250, y = 10)

cbt2 = Checkbutton(lf_order, text = "B - OREO: PHP 75", font = "fixedsys", variable = cb2, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt2.place(x=10, y = 35)
txtt2 = Entry(lf_order)
txtt2.place(x = 250, y = 35)


cbt3 = Checkbutton(lf_order, text = "C - YEMA: PHP 75", font = "fixedsys", variable = cb3, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt3.place(x=10, y = 60)
txtt3 = Entry(lf_order)
txtt3.place(x = 250, y = 60)

cbt4 = Checkbutton(lf_order, text = "D - MILKY CHOCO: PHP 75", font = "fixedsys", variable = cb4, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt4.place(x=10, y = 85)
txtt4 = Entry(lf_order)
txtt4.place(x = 250, y = 85)

cbt5 = Checkbutton(lf_order, text = "A + FRIES (REG): PHP 75", font = "fixedsys", variable = cb5, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt5.place(x=10, y = 110)
txtt5 = Entry(lf_order)
txtt5.place(x = 250, y = 110)

cbt6 = Checkbutton(lf_order, text = "B + FRIES (REG):  PHP 95", font = "fixedsys", variable = cb6, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt6.place(x=10, y = 135)
txtt6 = Entry(lf_order)
txtt6.place(x = 250, y = 135)

cbt7 = Checkbutton(lf_order, text = "C + FRIES (REG):  PHP 95", font = "fixedsys", variable = cb7, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt7.place(x=10, y = 160)
txtt7 = Entry(lf_order)
txtt7.place(x = 250, y = 160)

cbt8 = Checkbutton(lf_order, text = "D + FRIES (REG):  PHP 95", font = "fixedsys", variable = cb8, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt8.place(x=10, y = 185)
txtt8 = Entry(lf_order)
txtt8.place(x = 250, y = 185)

cbt9 = Checkbutton(lf_order, text = "REGULAR FRIES:  PHP 25", font = "fixedsys", variable = cb9, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt9.place(x=10, y = 210)
txtt9 = Entry(lf_order)
txtt9.place(x = 250, y = 210)

cbt10 = Checkbutton(lf_order, text = "MEDIUM FRIES:  PHP 45", font = "fixedsys", variable = cb10, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt10.place(x=10, y = 235)
txtt10 = Entry(lf_order)
txtt10.place(x = 250, y = 235)

cbt11 = Checkbutton(lf_order, text = "LARGE FRIES:  PHP 65", font = "fixedsys", variable = cb11, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt11.place(x=10, y = 260)
txtt11 = Entry(lf_order)
txtt11.place(x = 250, y = 260)

cbt12 = Checkbutton(lf_order, text = "ADD ONS:  PHP 10", font = "fixedsys", variable = cb12, 
                      onvalue = 1, 
                      offvalue = 0, )
cbt12.place(x=10, y = 285)
txtt12 = Entry(lf_order)
txtt12.place(x = 250, y = 285)

#Button - OK/CLEAR +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#variableName = Button (master location, option,......command = button function name)

btnOrder_OK = Button(lf_order, text = "OK", width = 10, font = "bold", command = calculate)
btnOrder_OK.place(x=70,y=350)

btnOrder_CLEAR = Button(lf_order, text = "CLEAR", width = 10, font = "bold", command = clear)
btnOrder_CLEAR.place(x=230,y=350)

#Label Frame2 - ORDER PREVIEW **********************************************************
lf_orderPre = LabelFrame(lf_order, width = 375,height = 230, bd = 8,text = "ORDER PREVIEW")
lf_orderPre.place(x=3,y=400)

#Label - Order Preview +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lbt1 = Label(lf_orderPre, text = "A - CLASSIC:  ",font = "fixedsys 7")
lbt1.place(x=5, y = 10)
lbt2 = Label(lf_orderPre, text = "B - OREO: ",font = "fixedsys 7")
lbt2.place(x=5, y = 25)
lbt3 = Label(lf_orderPre, text = "C - YEMA: ",font = "fixedsys 7")
lbt3.place(x=5, y = 40)
lbt4 = Label(lf_orderPre, text = "D - MILKY CHOCO: ",font = "fixedsys 10")
lbt4.place(x=5, y = 55)
lbt4 = Label(lf_orderPre, text = "A + FRIES (REG): ",font = "fixedsys 10")
lbt4.place(x=5, y = 70)
lbt4 = Label(lf_orderPre, text = "B + FRIES (REG): ",font = "fixedsys 10")
lbt4.place(x=5, y = 85)
lbt4 = Label(lf_orderPre, text = "C + FRIES (REG): ",font = "fixedsys")
lbt4.place(x=5, y = 100)
lbt4 = Label(lf_orderPre, text = "D + FRIES (REG): ",font = "fixedsys")
lbt4.place(x=5, y = 115)
lbt4 = Label(lf_orderPre, text = "REG FRIES: ",font = "fixedsys")
lbt4.place(x=5, y = 130)
lbt4 = Label(lf_orderPre, text = "MED FRIES: ",font = "fixedsys")
lbt4.place(x=5, y = 145)
lbt4 = Label(lf_orderPre, text = "LRG FRIES: ",font = "fixedsys")
lbt4.place(x=5, y = 160)
lbt4 = Label(lf_orderPre, text = "ADD ONS (NATA & PEARL): ",font = "fixedsys")
lbt4.place(x=5, y = 175)

#Label Frame3 - PAYMENT******************************************************************
lf_payment = LabelFrame(window, width = 390,height = 660,bd= 8, text = "PAYMENT", font = "bold")
lf_payment.place(x=410,y=35)

#Label and Textbox ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lbTotal = Label(lf_payment, text = "TOTAL:", font = "fixedsys")
lbTotal.place(x=80, y = 50)
txtT = Entry(lf_payment)
txtT.place(x = 150, y = 50)

lbCash = Label(lf_payment, text = "CASH:", font = "fixedsys")
lbCash.place(x=80, y = 115)
txtCash = Entry(lf_payment)
txtCash.place(x = 150, y = 115)

lbChange = Label(lf_payment, text = "CHANGE:", font = "fixedsys")
lbChange.place(x = 80, y = 180)
txtChange = Entry(lf_payment)
txtChange.place(x = 150, y = 180)

btnPayment_OK = Button(lf_payment, text = "OK", font = "bold", width = 10, command = bill)
btnPayment_OK.place(x=50,y=260)

btnPayment_NEW = Button(lf_payment, text = "NEW ORDER", font = "bold", width = 12, command = newOrder)
btnPayment_NEW.place(x=200,y=260)


#Label Frame4 - BILL SUMMARY *******************************************************
lf_bill = LabelFrame(lf_payment, width = 365,height = 230, bd = 8)
lf_bill.place(x=3,y=400)

window.mainloop() #for infinite loop of main program





























