import mysql.connector
import tkinter as tk
import tkinter.messagebox

connection = mysql.connector.connect(user = 'root', database = 'banktable', password='0924Alexander')

cursor = connection.cursor()

testQuery = ("SELECT * FROM bankinfo")

cursor.execute(testQuery)

for item in cursor:

    print(item)

cursor.close()

connection.close()

###############################################

def HomePage():
    root=tk.Tk()
    root.geometry("300x300")
    root.title("Account Login")
    User_var= tk.StringVar()
    PIN_var= tk.StringVar()
    Bal_var= tk.StringVar()

    titlelabel = tk.Label(root, text="Welcome", font=('NewTimes Roman', 18, 'bold'))

    def submit():
        global Username
        global Balance
 
        Username=User_var.get()
        PIN=PIN_var.get()
        Balance=Bal_var.get()
     
        print("The name is : " + Username)
        print("The password is : " + PIN)
        print("Starting Balance is " + Balance)
     
        User_var.set("")
        PIN_var.set("")
        Bal_var.set("")
        AccountPage()
        return Username, PIN, Balance

    UserEntry= tk.Entry(root, textvariable= User_var)
    UserLabel= tk.Label(root, text='Username:', font=('Arial', 12))

    PINLabel= tk.Label(root, text='PIN (4 digits)', font=('Arial', 12))
    PINEntry= tk.Entry(root, textvariable=PIN_var)

    BalLabel= tk.Label(root, text='Starting Balance: ', font=('Arial', 12))
    BalEntry= tk.Entry(root, textvariable=Bal_var)

    sub_btn= tk.Button(root, text="Submit", command=submit, font=('Arial', 10))

    titlelabel.grid(row=0, column=1)
    UserEntry.grid(row=1, column=1)
    UserLabel.grid(row=1, column=0)
    PINEntry.grid(row=2, column=1)
    PINLabel.grid(row=2, column=0)
    BalLabel.grid(row=3, column=0)
    BalEntry.grid(row=3, column=1)
    sub_btn.grid(row=4, column=1)


    root.mainloop()


def AccountPage():
    AccP=tk.Tk()
    AccP.geometry("300x300")
    AccP.title("Account Page")
    With_var= tk.StringVar()
    Depo_var= tk.StringVar()

    def DepositBtn():
        global Deposit
 
        Deposit=Depo_var.get()
     
        print("Amount Deposited : " + Deposit)
        tk.messagebox.showinfo("INFO", (f'You Deposited ${Deposit}'))
     
        Depo_var.set("")
        return Deposit

    def WithdrawBtn():
        global Withdraw
 
        Withdraw=With_var.get()
     
        print("Amount Withdrawn : " + Withdraw)
        tk.messagebox.showinfo("INFO", (f'You Withdrew ${Withdraw}'))
     
        With_var.set("")
        return Withdraw


    WelcLabel=tk.Label(AccP, text=(f'Welcome {Username}'), font=('Arial', 10, 'bold'))

    WithD_btn= tk.Button(AccP, text='Withdraw', command=WithdrawBtn, font=('Arial', 12))
    WithDLabel= tk.Label(AccP, text="Withdraw $", font=('Arial', 12))
    WithDEntry= tk.Entry(AccP, textvariable=With_var)

    Depos_btn= tk.Button(AccP, text="Deposit", command=DepositBtn, font=('Arial', 12))
    DeposLabel= tk.Label(AccP, text='Deposit $', font=('Arial', 12))
    DeposEntry= tk.Entry(AccP, textvariable=Depo_var)

    BalLabel= tk.Label(AccP, text=(f'Current Balance: {Balance}'))
    BalLabel.pack(padx=10, pady=10)

    def Delete():
        tk.messagebox.showinfo("INFO", "Your account is deleted")

    Del_btn=tk.Button(AccP, text='Delete',command=Delete, font=('Arial', 12))
    
    WelcLabel.pack(padx=10, pady=10)
    WithDLabel.place(x= 0, y= 90)
    WithDEntry.pack(padx=10, pady= 10)
    WithD_btn.pack()
    
    DeposEntry.pack(padx=20, pady=10)
    Depos_btn.pack(padx=20, pady=10)
    DeposLabel.place(x=0, y=160)

    Del_btn.pack(padx=20, pady=20)

    AccP.mainloop()


HomePage()