import tkinter
class MyGUI:

    def __init__(self):

        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("350x300")
        self.frame1 = tkinter.Frame(self.mainWindow)
        self.frame2 = tkinter.Frame(self.mainWindow)
        self.frame3 = tkinter.Frame(self.mainWindow)

        self.label1 = tkinter.Label(
            self.frame1, bg="white", fg="blue", font=("Ariel", 30), text="ATM Machine", padx=8, pady=8, width=100)

        self.label1.pack()

        self.radioVar = tkinter.IntVar()
        self.accountType = tkinter.IntVar()
        self.radioVar.set(1)
        self.accountType.set(1)

        # create 6 cb
        self.Radiobutton1 = tkinter.Radiobutton(self.frame2, fg="blue", font=(
            "Ariel", 15), text="Withdraw", variable=self.radioVar, value=1, padx=8, pady=8)
        self.Radiobutton2 = tkinter.Radiobutton(self.frame2, fg="blue", font=(
            "Ariel", 15), text="Deposit", variable=self.radioVar, value=2, padx=8, pady=8)
        self.Radiobutton3 = tkinter.Radiobutton(self.frame2, fg="blue", font=(
            "Ariel", 15), text="Check Balance", variable=self.radioVar, value=3, padx=8, pady=8)
        self.Radiobutton4 = tkinter.Radiobutton(self.frame2, fg="blue", font=(
            "Ariel", 15), text="Transfer Funds", variable=self.radioVar, value=4, padx=8, pady=8)

        # pack
        self.Radiobutton1.pack()
        self.Radiobutton2.pack()
        self.Radiobutton3.pack()
        self.Radiobutton4.pack()

        self.button1 = tkinter.Button(
            self.frame3, text="Proceed Transaction", command=self.getAccountType, padx=8, pady=8)
        self.button2 = tkinter.Button(
            self.frame3, text="Quit", command=self.mainWindow.destroy, padx=8, pady=8)

        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        self.checkingsBalance = 1000
        self.savingsBalance = 800
        tkinter.mainloop()

    def getAccountType(self):
        self.Radiobutton1.pack_forget()
        self.Radiobutton2.pack_forget()
        self.Radiobutton3.pack_forget()
        self.Radiobutton4.pack_forget()

        self.checkingsRadiobutton = tkinter.Radiobutton(self.frame2, fg="blue", font=(
            "Ariel", 15), text="Checkings", variable=self.accountType, value=1, padx=8, pady=8)

        self.savingsRadiobutton = tkinter.Radiobutton(self.frame2, fg="blue", font=(
            "Ariel", 15), text="Savings", variable=self.accountType, value=2, padx=8, pady=8)

        self.label1['text'] = "Account Type"

        self.checkingsRadiobutton.pack()
        self.savingsRadiobutton.pack()

        self.button1['command'] = self.process

    def process(self):
        self.checkingsRadiobutton.pack_forget()
        self.savingsRadiobutton.pack_forget()

        self.msg = tkinter.Message(self.frame2, width=500, padx=8, pady=8)
        self.amount = tkinter.StringVar()
        self.entryBox1 = tkinter.Entry(
            self.frame2, width=10, textvariable=self.amount, bd=2)

        if self.accountType.get() == 1:
            if self.radioVar.get() == 1:
                self.label1['text'] = "Withdraw"
                self.msg['text'] = "Enter Amount to withdraw"
            elif self.radioVar.get() == 2:
                self.label1['text'] = "Deposit"
                self.msg['text'] = "Enter Amount to deposit"
            elif self.radioVar.get() == 3:
                self.label1['text'] = "Thank You!"

                self.msg['text'] = "Available Balance: $" + \
                    str(self.checkingsBalance)
                self.button1.pack_forget()
            else:
                self.label1['text'] = "Transfer Funds"
                self.msg['text'] = "Enter Amount to transfer to savings account"
        else:
            if self.radioVar.get() == 1:
                self.label1['text'] = "Withdraw"
                self.msg['text'] = "Enter Amount to withdraw"
            elif self.radioVar.get() == 2:
                self.label1['text'] = "Deposit"
                self.msg['text'] = "Enter Amount to deposit"
            elif self.radioVar.get() == 3:
                self.label1['text'] = "Thank You!"
                self.msg['text'] = "Available Balance: $" + \
                    str(self.savingsBalance)
                self.button1.pack_forget()
            else:
                self.label1['text'] = "Transfer Funds"
                self.msg['text'] = "Enter Amount to transfer to checkings account"

        self.msg.pack()

        if self.radioVar.get() != 3:
            self.entryBox1.pack()
            self.button1['command'] = self.finish

    def finish(self):
        flag = True
        if self.accountType.get() == 1:
            if self.radioVar.get() == 1:
                if int(self.amount.get()) <= self.checkingsBalance:
                    self.checkingsBalance -= int(self.amount.get())
                    self.msg['text'] = "Withdrawn: $" + str(self.amount.get(
                    )) + "\nAvailable Balance: $" + str(self.checkingsBalance)
                else:
                    flag = False
                    self.msg['text'] = "Balance not available! Try again with smaller amount"
            elif self.radioVar.get() == 2:
                self.checkingsBalance += int(self.amount.get())
                self.msg['text'] = "Deposited: $" + str(self.amount.get(
                )) + "\nAvailable Balance: $" + str(self.checkingsBalance)
            else:
                if int(self.amount.get()) <= self.checkingsBalance:
                    self.checkingsBalance -= int(self.amount.get())
                    self.savingsBalance += int(self.amount.get())
                    self.msg['text'] = "Transferred: $" + str(self.amount.get(
                    )) + "\nAvailable Balance: $" + str(self.checkingsBalance)
                else:
                    flag = False
                    self.msg['text'] = "Balance not available! Try again with smaller amount"
        else:
            if self.radioVar.get() == 1:
                if int(self.amount.get()) <= self.savingsBalance:
                    self.savingsBalance -= int(self.amount.get())
                    self.msg['text'] = "Withdrawn: $" + str(self.amount.get(
                    )) + "\nAvailable Balance: $" + str(self.savingsBalance)
                else:
                    flag = False
                    self.msg['text'] = "Balance not available! Try again with smaller amount"
            elif self.radioVar.get() == 2:
                self.savingsBalance += int(self.amount.get())
                self.msg['text'] = "Deposited: $" + str(self.amount.get(
                )) + "\nAvailable Balance: $" + str(self.savingsBalance)
            else:
                if int(self.amount.get()) <= self.savingsBalance:
                    self.savingsBalance -= int(self.amount.get())
                    self.checkingsBalance += int(self.amount.get())
                    self.msg['text'] = "Transferred: $" + str(self.amount.get(
                    )) + "\nAvailable Balance: $" + str(self.savingsBalance)
                else:
                    flag = False
                    self.msg['text'] = "Balance not available! Try again with smaller amount"
        if flag == True:
            self.button1.pack_forget()
            self.label1['text'] = "Thank You!"
            self.entryBox1.pack_forget()


MyGUI = MyGUI()