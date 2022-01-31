from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as msg
import random as rd
import pymysql as sql
import time

def close_root15():
    root15.destroy()

def close_root14():
    root14.destroy()

def close_root13():
    root13.destroy()

def close_root12():
    root12.destroy()

def close_root11():
    root11.destroy()

def close_root10():
    root10.destroy()

def close_root9():
    root9.destroy()

def close_root8():
    root8.destroy()

def close_root6():
    root6.destroy()

def close_root5():
    root5.destroy()

def close_root4():
    root4.destroy()

def close_root3():
    root3.destroy()

def close_root2():
    root2.destroy()

def close_root1():
    root1.destroy()

def close_root():
    root.destroy()

def create_database():
    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()

    fullname = create_entry1.get()
    accountno = create_entry2
    aadharno = create_entry3.get()
    panno = create_entry4.get()
    address = create_entry5.get()
    password = create_entry6.get()
    balance = '0'

    if fullname == '' or accountno == '' or aadharno == '' or panno == '' or address == '' or password == '':
        msg.showerror('Error', 'All fields are required')
    else:
        query1 = "INSERT INTO accounts (name, account_no, aadhar_no, pan_no, address, password) VALUES(%s,%s,%s,%s,%s,%s)"
        value1 = (fullname, accountno, aadharno, panno, address, password)

        query2 = "INSERT INTO login_table (name, account_no, password, balance) VALUES(%s,%s,%s,%s)"
        value2 = (fullname, accountno, password, balance)

        c.execute(query1, value1)
        c.execute(query2, value2)

        conn.commit()
        msg.showinfo('Success', 'Account has been created successfully')
        add_balance()
        conn.close()

def add_amount():
    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()

    amount = add_balance.get()
    add_account_no = customer_account_number

    if amount == '':
        showerror('Error', 'Adding amount is Compulsory')
    else:
        query = "UPDATE login_table SET balance = %s WHERE account_no = %s"
        value = (amount, add_account_no)

        c.execute(query, value)
        
        conn.commit()
        msg.showinfo('Success', f'Rs.{amount} has been added to your account.')
        conn.close()
   
def add_balance():
    global root3
    global add_balance
    global customer_account_number

    customer_name = create_entry1.get()
    
    customer_full_name = customer_name.split()
    
    customer_f_name = customer_full_name[0]
    customer_m_name = customer_full_name[1]
    customer_l_name = customer_full_name[2]

    customer_first_name = customer_f_name.capitalize()
    customer_middle_name = customer_m_name.capitalize()
    customer_last_name = customer_l_name.capitalize()
    
    customer_account_number = create_entry2

    add_balance = StringVar()

    root3 = Toplevel(root)
    root3.geometry("700x500+200+50")
    root3.title('Add Balance To Your Account | Sikandar Singh')
    root3.resizable(False, False)
    root3.config(bg  = 'black')

    frame3 = Frame(root3, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame3.place(x = 5, y = 5)

    Label(frame3, text = f'WelCome - {customer_first_name} - {customer_account_number}', font = ('times', 30, 'bold'), bg = 'white', fg = 'green').place(x = 40, y = 10)

    Label(frame3, text = 'Add Balance to your Account', font = ('times', 30), bg = 'white', fg = 'red').place(x = 100, y = 80)

    Label(frame3, text = 'Add Amount', font = ('times', 20, 'bold'), bg = 'white', fg = 'red').place(x = 240, y = 160)
    Label(frame3, text = 'Rs', font = ('times', 20, 'bold'), bg = 'white', fg = 'red').place(x = 215, y = 220)
    entry1 = Entry(frame3, textvariable = add_balance, font = ('calibri', 20), width = 10, bg = 'yellow').place(x = 255, y = 220)

    Button(frame3, text = 'Add Amount', command = add_amount, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 205, y = 300)
    Button(frame3, text = 'Cancel', command = close_root3, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 205, y = 380)

def create_account():

    global root1
    global create_entry1
    global create_entry2
    global create_entry3
    global create_entry4
    global create_entry5
    global create_entry6

    create_entry1 = StringVar()
    create_entry3 = StringVar()
    create_entry4 = StringVar()
    create_entry5 = StringVar()
    create_entry6 = StringVar()

    root1 = Toplevel(root)
    root1.geometry("700x500+200+50")
    root1.title('Create Your Account Here | Sikandar Singh')
    root1.resizable(False, False)
    root1.config(bg  = 'black')

    frame1 = Frame(root1, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame1.place(x = 5, y = 5)

    Label(frame1, text = 'Create Your Account Here', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 10, y = 10)

    Label(frame1, text = 'Full Name', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 90)
    entry1 = Entry(frame1,textvariable = create_entry1, font = ('calibri', 14), width = 53, bg = 'yellow').place(x = 120, y = 90)

    create_entry2 = rd.randint(00000, 99999)
    Label(frame1, text = 'Account No     - ', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 150, y = 140)
    Label(frame1, text = create_entry2, font = ('times', 15, 'bold'), bg = 'white', fg = 'green').place(x = 350, y = 140)

    Label(frame1, text = 'Aadhar No', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 190)
    entry3 = Entry(frame1,textvariable = create_entry3, font = ('calibri', 14), width = 20, bg = 'yellow').place(x = 120, y = 190)

    Label(frame1, text = 'Pan No', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 370, y = 190)
    entry4 = Entry(frame1,textvariable = create_entry4, font = ('calibri', 14), width = 20, bg = 'yellow').place(x = 450, y = 190)
    
    Label(frame1, text = 'Address', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 270)
    entry5 = Entry(frame1,textvariable = create_entry5, font = ('calibri', 14), width = 53, bg = 'yellow').place(x = 120, y = 270)

    Label(frame1, text = 'Password', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 350)
    entry6 = Entry(frame1,textvariable = create_entry6, font = ('calibri', 14), width = 20, bg = 'yellow',show = '*').place(x = 120, y = 350)

    Label(frame1, text = 'Already have an account?', font = ('times', 14), bg = 'white', fg = 'maroon').place(x = 365, y = 350)
    Button(frame1, text = 'Login here', command = login_account, font = ('times', 14, 'bold'), bg = 'white', fg = 'green', bd = 0, activeforeground = 'maroon', activebackground = 'white').place(x = 560, y = 346)

    Button(frame1, text = 'Create Account', command = create_database, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 120, y = 420)
    Button(frame1, text = 'Cancel', command = close_root1, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 420, y = 420)

def withdrawl_verify():
    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()
    
    account_no_withdrawl = withdrawl_account_number
    amount_withdrawl = withdrawl_amount.get()
    status = 'withdrawl'
    reference = rd.randint(0000000000, 9999999999)

    query = "SELECT balance FROM login_table WHERE account_no = %s"
    value = (account_no_withdrawl)

    c.execute(query, value)
    results = c.fetchone()

    for result in results:
        bank_balance = result

    update_balance = int(bank_balance) - int(amount_withdrawl)
    updated_balance = str(update_balance)

    if amount_withdrawl > bank_balance:
        msg.showerror('Error','Your have insufficient balance in your account')
    else:
        query1 = "UPDATE login_table SET balance = %s WHERE account_no = %s"
        value1 = (updated_balance, account_no_withdrawl)

        c.execute(query1, value1)

        query2 = "INSERT INTO transactions_details (account_no, status, transfer_amount, reference_id) VALUES(%s,%s,%s,%s)"
        value2 = (account_no_withdrawl, status, amount_withdrawl, reference)

        c.execute(query2, value2)

        msg.showinfo('Success', f'Rs.{amount_withdrawl} has been withdrawl from your account')

    conn.commit()
    conn.close()

def withdrawl():
    global root5
    global withdrawl_amount
    global withdrawl_account_number
    
    withdrawl_account_number = dashboard_account_no
    
    withdrawl_amount = StringVar()

    root5 = Toplevel(root)
    root5.geometry("700x500+200+50")
    root5.title('Money Withdrawl | Sikandar Singh')
    root5.resizable(False, False)
    root5.config(bg  = 'black')

    frame5 = Frame(root5, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame5.place(x = 5, y = 5)

    Label(frame5, text = f'Withdrawl from Account No - {withdrawl_account_number}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 5, y = 10)

    Label(frame5, text = 'Withdrawl Amount', font = ('times', 20, 'bold'), bg = 'white', fg = 'red').place(x = 210, y = 160)
    Label(frame5, text = 'Rs', font = ('times', 20, 'bold'), bg = 'white', fg = 'red').place(x = 215, y = 220)
    entry1 = Entry(frame5, textvariable = withdrawl_amount, font = ('calibri', 20), width = 10, bg = 'yellow').place(x = 255, y = 220)

    Button(frame5, text = 'Withdrawl Amount',command = withdrawl_verify, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 205, y = 300)
    Button(frame5, text = 'Cancel', command = close_root5, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 205, y = 380)

def deposit_verify():
    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()
    
    account_no_deposit = deposit_account_number
    amount_deposit = deposit_amount.get()
    status = 'deposit'
    reference = rd.randint(0000000000,9999999999)

    query = "SELECT balance FROM login_table WHERE account_no = %s"
    value = (account_no_deposit)

    c.execute(query, value)
    results = c.fetchone()

    for result in results:
        bank_balance = result

    update_balance = int(bank_balance) + int(amount_deposit)
    updated_balance = str(update_balance)
    
    query1 = "UPDATE login_table SET balance = %s WHERE account_no = %s"
    value1 = (updated_balance, account_no_deposit)

    c.execute(query1, value1)

    query2 = "INSERT INTO transactions_details (account_no, status, transfer_amount, reference_id) VALUES(%s,%s,%s,%s)"
    value2 = (account_no_deposit, status, amount_deposit, reference)

    c.execute(query2, value2)

    conn.commit()
    msg.showinfo('Success', f'Rs.{amount_deposit} has been deposited from your account')
    conn.close()

def deposit():
    global root6
    global deposit_amount
    global deposit_account_number
    
    deposit_account_number = dashboard_account_no

    deposit_amount = StringVar()

    root6 = Toplevel(root)
    root6.geometry("700x500+200+50")
    root6.title('Money Deposit | Sikandar Singh')
    root6.resizable(False, False)
    root6.config(bg  = 'black')

    frame6 = Frame(root6, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame6.place(x = 5, y = 5)

    Label(frame6, text = f'Deposit from Account No - {deposit_account_number}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 5, y = 10)

    Label(frame6, text = 'Deposit Amount', font = ('times', 20, 'bold'), bg = 'white', fg = 'red').place(x = 210, y = 160)
    Label(frame6, text = 'Rs', font = ('times', 20, 'bold'), bg = 'white', fg = 'red').place(x = 215, y = 220)
    entry1 = Entry(frame6, textvariable = deposit_amount, font = ('calibri', 20), width = 10, bg = 'yellow').place(x = 255, y = 220)

    Button(frame6, text = 'Deposit Amount',command = deposit_verify, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 205, y = 300)
    Button(frame6, text = 'Cancel', command = close_root6, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 205, y = 380)

def check_balance():
    global root7
    global check_balance_account_number
    
    check_balance_account_number = dashboard_account_no
    
    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()

    query = "SELECT balance FROM login_table WHERE account_no = %s"
    value = (check_balance_account_number)

    c.execute(query, value)

    results = c.fetchone()
    for result in results:
        check_balance = result

    conn.commit()
    conn.close()

    root7 = Toplevel(root)
    root7.geometry("700x500+200+50")
    root7.title('Check your Account Balance | Sikandar Singh')
    root7.resizable(False, False)
    root7.config(bg  = 'black')

    frame7 = Frame(root7, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame7.place(x = 5, y = 5)

    frame0 = Frame(frame7, width = 200, height = 200, bg = 'yellow', bd = 0, relief = 'groove')
    frame0.place(x = 240, y = 150)

    Label(frame7, text = f'Check Balance for Account No - {check_balance_account_number}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 5, y = 10)

    Label(frame0, text = 'Balance', font = ('times', 20, 'bold'), bg = 'yellow', fg = 'red').place(x = 50, y = 25)

    Label(frame0, text =f'Rs.{check_balance}' , font = ('times', 20, 'bold'), width = 10, bg = 'yellow', fg = 'red').place(x = 20, y = 85)

def confirm_change_password():
    password_new = new_password.get()
    password_new_confirm = confirm_new_password.get()
    password_change_account_number = change_password_account_number
    
    if password_new == '' or password_new_confirm == '':
        msg.showerror('Error', 'Password fields are required')
    else:
        if password_new == password_new_confirm:
            conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
            c = conn.cursor()

            query = "UPDATE login_table SET password = %s WHERE account_no = %s"
            value = (password_new_confirm, password_change_account_number)

            query1 = "UPDATE accounts SET password = %s WHERE account_no = %s"
            value1 = (password_new_confirm, password_change_account_number)

            c.execute(query, value)
            c.execute(query1, value1)
            
            conn.commit()
            msg.showinfo('Success', 'Password has been Changed Successfully')
            conn.close()
        else:
            msg.showerror('Error','Password does not matched')

def change_password():
    global root8
    global change_password_account_number
    global new_password
    global confirm_new_password

    new_password = StringVar()
    confirm_new_password = StringVar()
    
    change_password_account_number = dashboard_account_no
    
    root8 = Toplevel(root)
    root8.geometry("700x500+200+50")
    root8.title('Change Password of your Account | Sikandar Singh')
    root8.resizable(False, False)
    root8.config(bg  = 'black')

    frame8 = Frame(root8, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame8.place(x = 5, y = 5)

    Label(frame8, text = f'Change Password of Account No - {change_password_account_number}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 0, y = 10)

    Label(frame8, text = 'New Password', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 120)
    entry1 = Entry(frame8, textvariable = new_password, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 125)
    
    Label(frame8, text = 'Confirm New Password', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 240)
    entry2 = Entry(frame8, textvariable = confirm_new_password, font = ('calibri', 14), width = 24, bg = 'yellow', show = '*').place(x = 340, y = 245)

    Button(frame8, text = 'Change Password', command = confirm_change_password, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 350)
    Button(frame8, text = 'Cancel', command = close_root8, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 350, y = 350)

def money_transfer_success():
    beneficiary_send_account_no = beneficiary_account_number
    beneficiary_receiver_account_no = beneficiary_account_no.get()
    beneficiary_receiver_name = beneficiary_name.get()
    beneficiary_receive_amount = beneficiary_amount.get()
    status = 'Money Transfer'
    reference = rd.randint(000000000000, 999999999999)

    if beneficiary_receiver_account_no == '' or beneficiary_receiver_name == '' or beneficiary_receive_amount == '':
        msg.showerror('Error', 'Name and Account No of Receiver is Mandatory')
    else:
        conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
        c = conn.cursor()

        query = "SELECT balance FROM login_table WHERE account_no = %s"
        value = (beneficiary_send_account_no)

        c.execute(query, value)

        results = c.fetchone()
        for result in results:
            sender_balance = result

        main_balance = int(sender_balance) - int(beneficiary_receive_amount)
        update_balance = str(main_balance)

        query1 = "UPDATE login_table SET balance = %s WHERE account_no = %s"
        value1 = (update_balance, beneficiary_send_account_no)

        c.execute(query1, value1)

        query2= "SELECT balance FROM login_table WHERE account_no = %s"
        value2 = (beneficiary_receiver_account_no)

        c.execute(query2, value2)

        results1 = c.fetchone()
        for result1 in results1:
            receiver_balance = result1

        main_balance2 = int(receiver_balance) + int(beneficiary_receive_amount)
        update_receiver_balance = str(main_balance2)

        query3 = "UPDATE login_table SET balance = %s WHERE account_no = %s"
        value3 = (update_receiver_balance, beneficiary_receiver_account_no)

        c.execute(query3, value3)

        query4 = "INSERT INTO money_transfer_details(to_name, from_account, to_account, transfer_amount, status, reference_id) VALUES (%s,%s,%s,%s,%s,%s)"
        value4 = (beneficiary_receiver_name, beneficiary_send_account_no, beneficiary_receiver_account_no, beneficiary_receive_amount, status, reference)

        c.execute(query4, value4)

        conn.commit()
        msg.showinfo('Success',f'Rs.{beneficiary_receive_amount} has been transfered successfully!')
        conn.close()
        

def money_transfer():
    global root9
    global beneficiary_account_no
    global beneficiary_name
    global beneficiary_account_number
    global beneficiary_amount

    beneficiary_account_number = dashboard_account_no

    beneficiary_account_no = StringVar()
    beneficiary_name = StringVar()
    beneficiary_amount = StringVar()
    
    root9 = Toplevel(root)
    root9.geometry("700x500+200+50")
    root9.title('Transfer Money from Account | Sikandar Singh')
    root9.resizable(False, False)
    root9.config(bg  = 'black')

    frame9 = Frame(root9, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame9.place(x = 5, y = 5)

    Label(frame9, text = 'Transfer Money to Beneficiary Account', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 0, y = 10)

    Label(frame9, text = 'Beneficiary Account No', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 120)
    entry1 = Entry(frame9, textvariable = beneficiary_account_no, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 125)
    
    Label(frame9, text = 'Beneficiary Name', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 190)
    entry2 = Entry(frame9, textvariable = beneficiary_name, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 195)

    Label(frame9, text = 'Beneficial Amount', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 260)
    entry2 = Entry(frame9, textvariable = beneficiary_amount, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 265)

    Button(frame9, text = 'Transfer', command = money_transfer_success, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 350)
    Button(frame9, text = 'Cancel', command = close_root9, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 350, y = 350)

def update_name_success():
    update_success_name = new_name.get()
    update_new_name = confirm_new_name.get()
    update_success_account = update_name_account_no
    
    if update_success_name == '' or update_new_name == '':
        msg.showerror('Error', 'Name fields are required')
    else:
        if update_success_name == update_new_name:
            
            conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
            c = conn.cursor()

            query = "UPDATE accounts SET name = %s WHERE account_no = %s"
            value = (update_success_name, update_success_account)

            c.execute(query, value)

            query1 = "UPDATE login_table SET name = %s WHERE account_no = %s"
            value1 = (update_success_name, update_success_account)

            c.execute(query1, value1)

            conn.commit()
            msg.showinfo('Success','Your name has been updated successfully')
            conn.close()

def update_name():
    global root11
    global new_name
    global confirm_new_name
    global update_name_account_no

    new_name = StringVar()
    confirm_new_name = StringVar()
    
    update_name_account_no = update_details_account_no

    root11 = Toplevel(root)
    root11.geometry("700x500+200+50")
    root11.title('Update Name of your Account | Sikandar Singh')
    root11.resizable(False, False)
    root11.config(bg  = 'black')

    frame11 = Frame(root11, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame11.place(x = 5, y = 5)

    Label(frame11, text = f'Update Name of Account No - {update_name_account_no}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 0, y = 10)

    Label(frame11, text = 'New Name', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 120)
    entry1 = Entry(frame11, textvariable = new_name, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 125)
    
    Label(frame11, text = 'Confirm New Name', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 240)
    entry2 = Entry(frame11, textvariable = confirm_new_name, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 245)

    Button(frame11, text = 'Change Name',command = update_name_success, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 350)
    Button(frame11, text = 'Cancel', command = close_root11, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 350, y = 350)

def update_aadhar_success():
    update_success_aadhar = new_aadhar.get()
    update_new_aadhar = confirm_new_aadhar.get()
    update_aadhar_success_account = update_aadhar_account_no

    if update_success_aadhar == '' or update_new_aadhar == '':
        msg.showerror('Error', 'Aadhar fields are required')
    else:
        if update_success_aadhar == update_new_aadhar:
            
            conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
            c = conn.cursor()

            query = "UPDATE accounts SET aadhar_no = %s WHERE account_no = %s"
            value = (update_success_aadhar, update_aadhar_success_account)

            c.execute(query, value)

            conn.commit()
            msg.showinfo('Success','Your aadhar has been updated successfully')
            conn.close()

def update_aadhar():
    global root12
    global new_aadhar
    global confirm_new_aadhar
    global update_aadhar_account_no

    new_aadhar = StringVar()
    confirm_new_aadhar = StringVar()
    
    update_aadhar_account_no = update_details_account_no

    root12 = Toplevel(root)
    root12.geometry("700x500+200+50")
    root12.title('Update Aadhar of your Account | Sikandar Singh')
    root12.resizable(False, False)
    root12.config(bg  = 'black')

    frame12 = Frame(root12, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame12.place(x = 5, y = 5)

    Label(frame12, text = f'Update Aadhar of Account No - {update_aadhar_account_no}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 0, y = 10)

    Label(frame12, text = 'New Aadhar', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 120)
    entry1 = Entry(frame12, textvariable = new_aadhar, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 125)
    
    Label(frame12, text = 'Confirm New Aadhar', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 240)
    entry2 = Entry(frame12, textvariable = confirm_new_aadhar, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 245)

    Button(frame12, text = 'Change Aadhar',command = update_aadhar_success, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 350)
    Button(frame12, text = 'Cancel', command = close_root12, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 350, y = 350)

def update_pan_success():
    update_success_pan = new_pan.get()
    update_new_pan = confirm_new_pan.get()
    update_pan_success_account = update_pan_account_no

    if update_success_pan == '' or update_new_pan == '':
        msg.showerror('Error', 'Pan Details fields are required')
    else:
        if update_success_pan == update_new_pan:
            
            conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
            c = conn.cursor()

            query = "UPDATE accounts SET pan_no = %s WHERE account_no = %s"
            value = (update_success_pan, update_pan_success_account)

            c.execute(query, value)

            conn.commit()
            msg.showinfo('Success','Your Pan details has been updated successfully')
            conn.close()

def update_pan():
    global root13
    global new_pan
    global confirm_new_pan
    global update_pan_account_no

    new_pan = StringVar()
    confirm_new_pan = StringVar()
    
    update_pan_account_no = update_details_account_no

    root13 = Toplevel(root)
    root13.geometry("700x500+200+50")
    root13.title('Update Pan of your Account | Sikandar Singh')
    root13.resizable(False, False)
    root13.config(bg  = 'black')

    frame13 = Frame(root13, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame13.place(x = 5, y = 5)

    Label(frame13, text = f'Update Pan of Account No - {update_pan_account_no}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 0, y = 10)

    Label(frame13, text = 'New Pan Number', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 120)
    entry1 = Entry(frame13, textvariable = new_pan, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 125)
    
    Label(frame13, text = 'Confirm New Pan', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 240)
    entry2 = Entry(frame13, textvariable = confirm_new_pan, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 245)

    Button(frame13, text = 'Change Pan',command = update_pan_success, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 350)
    Button(frame13, text = 'Cancel', command = close_root13, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 350, y = 350)

def update_address_success():
    update_success_address = new_address.get()
    update_new_address = confirm_new_address.get()
    update_address_success_account = update_address_account_no

    if update_success_address == '' or update_new_address == '':
        msg.showerror('Error', 'Address fields are required')
    else:
        if update_success_address == update_new_address:
            
            conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
            c = conn.cursor()

            query = "UPDATE accounts SET address = %s WHERE account_no = %s"
            value = (update_success_address, update_address_success_account)

            c.execute(query, value)

            conn.commit()
            msg.showinfo('Success','Your Address has been updated successfully')
            conn.close()

def update_address():
    global root14
    global new_address
    global confirm_new_address
    global update_address_account_no

    new_address = StringVar()
    confirm_new_address = StringVar()
    
    update_address_account_no = update_details_account_no

    root14 = Toplevel(root)
    root14.geometry("700x500+200+50")
    root14.title('Update Address of your Account | Sikandar Singh')
    root14.resizable(False, False)
    root14.config(bg  = 'black')

    frame14 = Frame(root14, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame14.place(x = 5, y = 5)

    Label(frame14, text = f'Update Address of Account No - {update_address_account_no}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 0, y = 10)

    Label(frame14, text = 'New Address Number', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 120)
    entry1 = Entry(frame14, textvariable = new_address, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 125)
    
    Label(frame14, text = 'Confirm New Address', font = ('times', 20, 'bold'), bg = 'white', fg = 'green').place(x = 20, y = 240)
    entry2 = Entry(frame14, textvariable = confirm_new_address, font = ('calibri', 14), width = 24, bg = 'yellow').place(x = 340, y = 245)

    Button(frame14, text = 'Change Address',command = update_address_success, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 350)
    Button(frame14, text = 'Cancel', command = close_root14, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 350, y = 350)

def check_details():
    global check_details_account_no
    global root15
    global check_entry_name
    global check_entry_account_no
    global check_entry_aadhar_no
    global check_entry_pan_no
    global check_entry_address
    global check_entry_password

    check_entry_name = StringVar()
    check_entry_aadhar_no = StringVar()
    check_entry_pan_no = StringVar()
    check_entry_address = StringVar()
    check_entry_password = StringVar()
    
    check_details_account_no = update_details_account_no

    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()

    query = "SELECT * FROM accounts WHERE account_no = %s"
    value = (check_details_account_no)

    c.execute(query, value)

    results = c.fetchall()
    for result in results:
        user_id = result[0]
        user_name = result[1]
        user_account_no = result[2]
        user_aadhar_no = result[3]
        user_pan_no = result[4]
        user_address = result[5]
        user_password = result[6]

    check_entry_name.set(user_name)
    check_entry_aadhar_no.set(user_aadhar_no)
    check_entry_pan_no.set(user_pan_no)
    check_entry_address.set(user_address)
    check_entry_password.set(user_password)

    conn.commit()
    conn.close()

    root15 = Toplevel(root)
    root15.geometry("700x500+200+50")
    root15.title('View Account Details Here | Sikandar Singh')
    root15.resizable(False, False)
    root15.config(bg  = 'black')

    frame15 = Frame(root15, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame15.place(x = 5, y = 5)

    Label(frame15, text = f'Views Account Details Here - {check_details_account_no}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 10, y = 10)
    Label(frame15, text = f'User Unique ID - {user_id}', font = ('times', 14, 'bold'), bg = 'yellow', fg = 'red', bd = 0, width = 18).place(x = 450, y = 350)

    Label(frame15, text = 'Full Name', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 90)
    entry1 = Entry(frame15,textvariable = check_entry_name, font = ('calibri', 14), width = 53, bg = 'yellow').place(x = 120, y = 90)

    Label(frame15, text = 'Account No     - ', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 150, y = 140)
    Label(frame15, text = user_account_no, font = ('times', 15, 'bold'), bg = 'white', fg = 'green').place(x = 350, y = 140)

    Label(frame15, text = 'Aadhar No', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 190)
    entry3 = Entry(frame15,textvariable = check_entry_aadhar_no, font = ('calibri', 14), width = 20, bg = 'yellow').place(x = 120, y = 190)

    Label(frame15, text = 'Pan No', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 370, y = 190)
    entry4 = Entry(frame15,textvariable = check_entry_pan_no, font = ('calibri', 14), width = 20, bg = 'yellow').place(x = 450, y = 190)
    
    Label(frame15, text = 'Address', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 270)
    entry5 = Entry(frame15,textvariable = check_entry_address, font = ('calibri', 14), width = 53, bg = 'yellow').place(x = 120, y = 270)

    Label(frame15, text = 'Password', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 350)
    entry6 = Entry(frame15,textvariable = check_entry_password, font = ('calibri', 14), width = 20, bg = 'yellow',show = '*').place(x = 120, y = 350)

    Button(frame15, text = 'Update Details', command = update_details, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 120, y = 420)
    Button(frame15, text = 'Cancel', command = close_root15, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 420, y = 420)


def update_details():
    
    global root10
    global update_details_account_no

    update_details_account_no = dashboard_account_no

    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()

    query = "SELECT name FROM accounts WHERE account_no = %s"
    value = (update_details_account_no)

    c.execute(query, value)

    results = c.fetchone()
    for result in results:
        customer_details_name = result

    customer_name_details = customer_details_name.split()
    customer_first_details = customer_name_details[0].capitalize()
    customer_middle_details = customer_name_details[1].capitalize()
    customer_last_details = customer_name_details[2].capitalize()

    conn.commit()
    conn.close()

    root10 = Toplevel(root)
    root10.geometry("700x500+200+50")
    root10.title('Welcome to Dashboard | Sikandar Singh')
    root10.resizable(False, False)
    root10.config(bg  = 'black')

    frame10 = Frame(root10, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame10.place(x = 5, y = 5)

    Label(frame10, text = f'Update Account Details {customer_first_details} {customer_last_details}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 5, y = 10)

    Label(frame10, text = 'Menu', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 300, y = 70)

    Button(frame10, text = 'Update Name', command = update_name, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'red', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 70, y = 180)
    Button(frame10, text = 'Update Aadhar Number', command = update_aadhar, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'green', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 360, y = 180)
    Button(frame10, text = 'Update Pan Number', command = update_pan, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 70, y = 240)
    Button(frame10, text = 'Update Address',command = update_address, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 360, y = 240)
    Button(frame10, text = 'Check Details', command = check_details, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'red', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 70, y = 300)
    Button(frame10, text = 'Cancel', command = close_root10, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'red', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 360, y = 300)


def dashboard():
    global dashboard_account_no
    
    dashboard_account_no = login_account_no

    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()

    query = "SELECT * FROM accounts WHERE account_no = %s"
    value = (dashboard_account_no)

    c.execute(query, value)

    results = c.fetchall()
    for result in results:
        c_id = result[0]
        c_name = result[1]
        c_account_no = result[2]
        c_adhar_no = result[3]
        c_pan_no = result[4]
        c_address = result[5]

    conn.commit()
    conn.close()
    
    customerName = c_name.split()
    c_f_name = customerName[0].capitalize()
    c_m_name = customerName[1].capitalize()
    c_l_name = customerName[2].capitalize()
    
    global root4

    root4 = Toplevel(root)
    root4.geometry("700x500+200+50")
    root4.title('Welcome to Dashboard | Sikandar Singh')
    root4.resizable(False, False)
    root4.config(bg  = 'black')

    frame4 = Frame(root4, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame4.place(x = 5, y = 5)

    Label(frame4, text = f'WelCome - {c_f_name} {c_l_name} - {c_account_no}', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 5, y = 10)

    Label(frame4, text = 'Menu', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 300, y = 70)

    Button(frame4, text = 'Withdrawl', command = withdrawl, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'red', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 70, y = 180)
    Button(frame4, text = 'Deposit', command = deposit, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'green', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 360, y = 180)
    Button(frame4, text = 'Check Balance',command = check_balance, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 70, y = 240)
    Button(frame4, text = 'Change Password', command = change_password, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 360, y = 240)
    Button(frame4, text = 'Money Transfer', command = money_transfer, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'red', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 70, y = 300)
    Button(frame4, text = 'Update Details', command = update_details, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 360, y = 300)
    Button(frame4, text = 'Cancel',command = close_root4, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'red', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 210, y = 360)

def login_database():
    conn = sql.connect(host = 'localhost', user = 'root', password = '', db = 'bank1')
    c = conn.cursor()
    
    global customer_name
    global login_account_no

    login_account_no = login_entry1.get()
    login_password = login_entry2.get()

    if login_account_no == '' or login_password == '':
        msg.showerror('Error', 'All fields are required')
    else:
        query = "SELECT * FROM login_table WHERE account_no = %s"
        value = (login_account_no)

        c.execute(query, value)

        results = c.fetchall()

        for result in results:
            customer_id = result[0]
            customer_name = result[1]
            customer_account_no = result[2]
            customer_password = result[3]
            customer_balance = result[4]
            
        if login_account_no == customer_account_no:
            if login_password == customer_password:
                dashboard()
            else:
                msg.showerror('Error', 'Invalid password try again!')
        else:
            msg.showerror('Error', 'Customer not found')

        conn.commit()
        conn.close()

def login_account():
    global root2
    global login_entry1
    global login_entry2

    login_entry1 = StringVar()
    login_entry2 = StringVar()

    root2 = Toplevel(root)
    root2.geometry("700x500+200+50")
    root2.title('Login To Your Account | Sikandar Singh')
    root2.resizable(False, False)
    root2.config(bg  = 'black')

    frame2 = Frame(root2, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame2.place(x = 5, y = 5)

    Label(frame2, text = 'Login To Your Account', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 10, y = 10)

    Label(frame2, text = 'Account Number', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 90)
    entry1 = Entry(frame2, textvariable = login_entry1, font = ('calibri', 14), width = 53, bg = 'yellow').place(x = 20, y = 130)

    Label(frame2, text = 'Password (4 digit pin)', font = ('times', 15, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 230)
    entry2 = Entry(frame2, textvariable = login_entry2, font = ('calibri', 14), width = 53, bg = 'yellow', show = '*').place(x = 20, y = 270)

    Button(frame2, text = 'Login Account', command = login_database, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 20, y = 380)
    Button(frame2, text = 'Cancel', command = close_root2, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19).place(x = 310, y = 380)

def times():
    current_time = time.strftime('%I:%M:%S %p')
    clock.config(text = 'Time : '+current_time, fg = 'green')
    clock.after(200, times)

def main_screen():
    global root
    global clock
    
    root = Tk()
    root.geometry("700x500+200+50")
    root.title('Bank Management System | Sikandar Singh')
    root.resizable(False, False)
    root.config(bg  = 'black')

    frame = Frame(root, width = 690, height = 490, bg = 'white', bd = 0, relief = 'groove')
    frame.place(x = 5, y = 5)

    Label(frame, text = 'Bank Management System', font = ('times', 30, 'bold'), bg = 'white', fg = 'red').place(x = 20, y = 10)

    clock = Label(frame, font = ('times new roman', 15,'bold'), bg = 'white')
    clock.place(x = 515, y = 0)
    times()

    load1 = Image.open("ProjectImages/bank_images.jpg")        
    render1 = ImageTk.PhotoImage( load1)        
    img1 = Label(frame, image=render1, bg = 'black', bd = 1, relief = 'raised')
    img1.image = render1
    img1.place(x = 20, y = 80, width = 410, height = 250)

    Button(frame, text = 'Create Account', command = create_account, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19, height = 2).place(x = 440, y = 80)
    Button(frame, text = 'Login Account', command = login_account, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19, height = 2).place(x = 440, y = 170)
    Button(frame, text = 'Cancel', command = close_root, bd = 1, font = ('times', 16, 'bold'), bg = 'white', fg = 'blue', activeforeground = 'black', activebackground = 'lightyellow', width = 19, height = 2).place(x = 440, y = 260)

    Label(frame, text = 'Ward no 06, Chhatrapati Shahu Maharaj Colony', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 350, y = 340)
    Label(frame, text = 'Nandafata, Tah : Korpana, Dist : Chandrapur 442917', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 350, y = 370)
    Label(frame, text = 'Phone no. +91-7057525359, +91-6201406484', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 350, y = 400)
    Label(frame, text = 'E-mail : sikandarsingh2210@gmail.com', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 350, y = 430)

    Label(frame, text = 'Facebook | @Singh_S_Sikandar', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 20, y = 340)
    Label(frame, text = 'Instagram | @singh_saheb_official__', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 20, y = 370)
    Label(frame, text = 'WhatsApp | +916201406484', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 20, y = 400)
    Label(frame, text = 'Yahoo | sikandarsingh60@yahoo.com', font = ('times new roman', 12), bg = 'white', fg = 'grey').place(x = 20, y = 430)

    root.mainloop()
main_screen()