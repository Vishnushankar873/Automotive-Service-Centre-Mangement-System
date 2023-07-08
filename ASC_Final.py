# Connecting SQL and Python

import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='achanamma873',database='AutomobileServiceCentre')
cursor=con.cursor()
#cursor.execute('create database AutomobileServiceCentre')
cursor.execute("use AutomobileServiceCentre")
"""
if con.is_connected():
  print ("Connection Successful")  
"""

#Importing modules

from tabulate import tabulate

from PIL import Image

import numpy as np

import matplotlib.pyplot as plt

import random


# Tables used

# Vehiles
# PartsList
# USER_Purschases
# Vehicle_date
# VehicleOut_Date

#Other def()

def ADMIN_WheelAlignment():
    text ="""       
        Wheel Alignment Tool        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""       
        Is the Wheel placed in the TOOL?     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input Y/N: ')   
    if ch=='Y':
        for i in range (4):
            text ="""       
                Alignment for wheel       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
            for i in range(1, 2):
                y = random.randrange(-10,10)
                print(y)
    elif ch=='N':
        print ('Please Place your vehicle on the tool')
        ADMIN_WheelAlignment()
    
    else:
        print ('Wrong Input')
        
    text ="""        
        Do you want to back to PERVIOUS Menu
    Yes     [Y]
    No      [N]
    Repeat  [R]        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
        ADMINfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMIN_WheelAlignment()



        
    
   


def Metallic_Red():
    
    im = Image.open(r"Porsche Metallic Red.jpeg")

 
    im.show()  

def Metallic_Magenta():
    im = Image.open(r"Porsche Metallic Magenta 1.jpeg")
    

    im.show()

def Metallic_Yellow():
    im = Image.open(r"Porsche Metallic Yellow 1.jpeg")

 
    im.show()

def Metallic_Blue():
    im = Image.open(r"Porsche Metallic Blue 1.jpeg")
 
    im.show()



def USERColour_Graph():
    
    barWidth = 0.15
    fig = plt.subplots(figsize =(12, 8))
    
    
    Metallic_Red = [12, 30, 1, 8, 22]
    Metallic_Magenta = [28, 6, 16, 5, 10]
    Metallic_Yellow = [29, 3, 24, 25, 17]
    Metallic_Blue = [34, 6, 23, 30, 13]
    
    
    br1 = np.arange(len(Metallic_Red))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    
    
    plt.bar(br1, Metallic_Red, color ='r', width = barWidth,
            edgecolor ='grey', label ='Metallic_Red')
    plt.bar(br2, Metallic_Magenta, color ='m', width = barWidth,
            edgecolor ='grey', label ='Metallic_Magenta')
    plt.bar(br3, Metallic_Yellow, color ='y', width = barWidth,
            edgecolor ='grey', label ='Metallic_Yellow')
    plt.bar(br4, Metallic_Blue, color ='b', width = barWidth,
            edgecolor ='grey', label ='Metallic_Blue')
            
    
    plt.xlabel('Customers', fontweight ='bold', fontsize = 15)
    plt.ylabel('Top Reccomendation', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Metallic_Red))],
            ['2015', '2016', '2017', '2018', '2019'])
    
    plt.legend()
    plt.show()

def USERColour_Choice():
    text ="""        
           Colour Pallete        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)    
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. Metallic Red\n2. Metallic Magenta\n3. Metallic Yellow\n4. Metallic Blue\n5. Recommendations\n6. Go back to the previous menu.     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=int(input('Input: '))
    if ch==1:
       Metallic_Red()
       USERColour_Choice()

    elif ch==2:
       Metallic_Magenta()
       USERColour_Choice()

    elif ch==3:
        Metallic_Yellow()
        USERColour_Choice()

    elif ch==4:
        Metallic_Blue()
        USERColour_Choice()

    elif ch==5:
        USERColour_Graph()
        USERColour_Choice()
    
    elif ch==6:
        USERfuntion_menu()

    else:
        print('Wrong input')


def ADMINforgotpass():
    text ="""        
            Did you forget you password?
        Yes     [Y]
        No      [N]       
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Select Y/N: ')
    if ch=='Y':
        text ="""        
                Do you want to make a new account?
            Yes     [Y]
            No      [N]       
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        newch=input('Input Y/N: ')
        if newch=='Y':
            admin_signup()
        elif newch=='N':
           with open('USEREmail.csv', mode='a', newline='') as file:
            write_csv=csv.writer(file,delimiter=',')
            newusername=input('Enter your username: ')
            email=input('Enter your email ID: ')
            conemail=input('Re-enter your email for confirmation: ')
            if email == conemail:
                write_csv.writerow([newusername,email])
            text ="""       
                Please Choose an Option        
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
            text ="""       
                The Other Admin will send a confirmation message to your email soon        
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            print('Wrong input')
    else:
        admin_signin()

def USERforgotpass():
    text ="""        
            Did you forget you password?
        Yes     [Y]
        No      [N]       
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
        text ="""        
                Do you want to make a new account?
            Yes     [Y]
            No      [N]       
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        newch=input('Input Y/N: ')
        if newch=='Y':
            user_signup()
        elif newch=='N':
           with open('USEREmail.csv', mode='a', newline='') as file:
            write_csv=csv.writer(file,delimiter=',')
            newusername=input('Enter your username: ')
            email=input('Enter your email ID: ')
            conemail=input('Re-enter your email for confirmation: ')
            if email == conemail:
                write_csv.writerow([newusername,email])
            text ="""       
                Please Choose an Option        
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
            text ="""       
                The Admin will send a confirmation message to your email soon        
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            print('Wrong input')
    else:
        user_signup()
    

def USER_date():
    text ="""       
           Add Date when giving the vehicle       
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)   
    vehicleno=input("Enter Vehicle number: ")
    vehiclein=input("Enter the date (YYYY-MM-DD): ")
    query1="insert into Vehicle_date values(%s,%s)"
    val1=(vehicleno, vehiclein,)
    cursor.execute(query1, val1)
    con.commit()
    text ="""       
           Record inserted successfully       
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            USERfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        USER_date()
    
    

def ADMIN_date():
    text ="""       
           Add Date when giving back the vehicle        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)   
    vehicleno=input("Enter Vehicle number: ")
    vehicleout=input("Enter the date (YYYY-MM-DD): ")
    query1="insert into VehicleOut_Date values(%s,%s)"
    val1=(vehicleno,vehicleout)
    cursor.execute(query1, val1)
    con.commit()
    text ="""       
           Record inserted successfully       
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            ADMINfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMIN_date()

def EXIT():
    print("Thank you...")

def USERsearch_parts():
    text ="""        
           Search the parts you want        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ptname=input('Input the name of the part: ')
    query='select * from partslist where Parts_name=%s'
    val=(ptname,)
    cursor.execute(query,val)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers=columns, tablefmt='rounded_grid'))
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            USERfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        USERsearch_parts()

def USERpurchases():
    text ="""       
           Purschases       
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    username=input("Enter your User Name: ")
    purschases=input("Enter Parts you purschased: ")
    listedpartprice=int(input("Listed Part Price: "))
    totalprice=listedpartprice+120
    print("Your Total Price with Service is: ",totalprice)
    query2="insert into USER_Purschases values(%s,%s,%s,%s)"
    val2=(username, purschases, listedpartprice, totalprice)
    cursor.execute(query2, val2)
    con.commit()
    print(cursor.rowcount,"\nDetails inserted")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers=columns, tablefmt='rounded_grid'))
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Do you want to BACK to Menu Y/N/R: ')
    if ch=='Y':
            USERfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        USERpurchases()

def USERpurchases_update():
    text ="""       
           Update your purschase        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""       
           Enter the no of details you want to update 
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    updtno=int(input("Input: "))
    print('Choices')
    text ="""       
           \n2. Parts Purschased by you.\n3. Discounted Part price.          
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)   
    for x in range(updtno):
            updtcol=int(input("Input: "))
            if updtcol==2:
                username=input("Enter user name: ")
                updtpartname=input("Enter purschased part name for updating: ")
                query="update USER_Purschases set USER_Name=%s where Parts_Purchased=%s"
                val=(updtpartname,username)
                cursor.execute(query,val)
                con.commit()
                cursor.execute("select * from USER_Purschases")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))
            elif updtcol==3:
                username=input("Enter user name: ")
                updtpartname=input("Enter purschased part price for updating: ")
                query="update USER_Purschases set USER_Name=%s where Part_Price=%s"
                val=(updtpartname,username)
                cursor.execute(query,val)
                con.commit()
                cursor.execute("select * from USER_Purschases")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))
            else:
                text ="""       
                    Wrong Input       
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)

    text ="""        
            Do you want to back to PERVIOUS Menu
            Yes     [Y]
            No      [N]
            Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Do you want to BACK to Menu Y/N/R: ')
    if ch=='Y':
            USERfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        USERpurchases_update()
       
def USERfuntions():
    text ="""        
            Add your NEW Vehicle      
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)    
    Vehicle_no=input("Input vechicle number plate: ")
    make_and_model=input("Input Vehicle Make and Model: ")
    service=input("Service needed for the vehicle: ")
    model_year=int(input("Input vehicle model year: "))
    query1="insert into Vehicles values(%s,%s,%s,%s)"
    val1=(Vehicle_no, make_and_model, service, model_year)
    cursor.execute(query1, val1)
    con.commit()
    print(cursor.rowcount)
    USER_date()
    text ="""        
            Data has been added Successfully       
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
            Do you want to back to PERVIOUS Menu
            Yes     [Y]
            No      [N]
            Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Do you want to BACK to Menu Y/N/R: ')
    if ch=='Y':
            USERfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        USERfuntions()
    
def ADMINUpdating():
    text ="""     
           Update Service Centre Database        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. Vehicle database\n2. Parts list database     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    updt=input("Input: ")
    text ="""     
           No: of details you want to update        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)   
    updtno=int(input("Input: "))
    for i in range(updtno):
        if updt=='1':
            text ="""     
                2. Make and Model\n3. Service\n4. Model Year       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)            
            updtcol=int(input("Input column to update "))
            if updtcol == 2:
                text ="""     
                    Updating Make and Model of cutomer's vehicle        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)                
                updtno = input("Enter Vehicle Number Plate: ")
                updtPart_Price = input("Enter Vehicle Model and Make: ")
                query = "UPDATE Vehicles SET make_and_model = %s WHERE Vehicle_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Vehicles")
                cursor.execute("select * from Vehicles")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))

                
            elif updtcol==3:
                text ="""     
                    Updating Service type of cutomer's vehicle        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)                
                updtno = input("Enter Vehicle Number Plate: ")
                updtvehicleservice = input("Enter Vehicle Service Type: ")
                query = "UPDATE Vehicles SET service = %s WHERE Vehicle_no = %s"
                val2 = (updtvehicleservice, updtno)
                cursor.execute(query, val2)
                con.commit()
                cursor.execute("SELECT * FROM Vehicles")
                data = cursor.fetchall()
                cursor.execute("select * from Vehicles")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))

            elif updtcol==4:
                text ="""     
                    Updating Model year of cutomer's vehicle        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)                
                updtno = input("Enter Vehicle Number Plate: ")
                updtvehiclemodelyear = int(input("Enter Vehicle Model Year: "))
                query = "UPDATE Vehicles SET model_year = %s WHERE Vehicle_no = %s"
                val3 = (updtvehiclemodelyear, updtno)
                cursor.execute(query, val3)
                con.commit()
                cursor.execute("SELECT * FROM Vehicles")
                data = cursor.fetchall()
                cursor.execute("select * from Vehicles")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))

            else:
                print("Wrong Input")


        if updt=='2':
            text ="""     
                2. Parts name\n3. Service type \n4. For which model\n5. Part brand\n6. Vehicle year\n7. Part price       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)            
            updtcol=int(input("Enter column to update "))
            if updtcol == 2:
                text ="""     
                    Updating part name        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)               
                updtno = input("Enter Part Number: ")
                updtPart_Price = input("Enter Part Model: ")
                query = "UPDATE Partslist SET Parts_name = %s WHERE Parts_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Partslist")
                data = cursor.fetchall()
                cursor.execute("select * from Partslist")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))


            elif updtcol == 3:
                text ="""     
                    Updating service type        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)
                updtno = input("Enter Part Number: ")
                updtPart_Price = input("Enter Service Type: ")
                query = "UPDATE Partslist SET Service_Type = %s WHERE Parts_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Partslist")
                data = cursor.fetchall()
                cursor.execute("select * from Partslist")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))

            elif updtcol == 4:
                text ="""     
                    Updating part designated for which vehicle model       
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)
                updtno = input("Enter Part Number: ")
                updtPart_Price = input("Enter Part Brand: ")
                query = "UPDATE Partslist SET Part_Brand = %s WHERE Parts_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Partslist")
                data = cursor.fetchall()
                cursor.execute("select * from Partslist")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))

            elif updtcol == 5:
                text ="""     
                    Updating part brand        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)
                updtno = input("Enter Part Number: ")
                updtPart_Price = input("Enter Vehicle Year: ")
                query = "UPDATE Partslist SET Vehicle_Year = %s WHERE Parts_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Partslist")
                data = cursor.fetchall()
                cursor.execute("select * from Partslist")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))


            elif updtcol == 6:
                text ="""     
                    Updating vehicle year for which the part is for        
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)
                updtno = input("Enter Part Number: ")
                updtPart_Price = input("Enter Vehicle Model: ")
                query = "UPDATE Partslist SET For_Model = %s WHERE Parts_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Partslist")
                data = cursor.fetchall()
                cursor.execute("select * from Partslist")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))

            elif updtcol == 7:
                text ="""     
                    Updating part price       
                """
                table = [[text]]
                output = tabulate(table, tablefmt='rounded_grid')
                print(output)
                updtno = input("Enter Part Number: ")
                updtPart_Price = input("Enter Part Price with Currency: ")
                query = "UPDATE Partslist SET Part_Price = %s WHERE Parts_no = %s"
                val1 = (updtPart_Price, updtno)
                cursor.execute(query, val1)
                con.commit()
                cursor.execute("SELECT * FROM Partslist")
                data = cursor.fetchall()
                cursor.execute("select * from Partslist")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(rows, headers=columns, tablefmt='double_outline'))
    text ="""        
        Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            ADMINfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMINUpdating()
                
def ADMINDeleting_Vehicles():
    text ="""        
           Choose what you want to delete        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    print('\nChoice: ')
    text ="""        
           1. Vehicle No.\n2. Vehicle Make and Model\n3. Service record\n4. Vehicle Model Year    
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    chtodelete=int(input("\nInput: "))
    if chtodelete==1:
        cursor.execute("select * from Vehicles")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Vehicles where Vehicle_no=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Vehicles()
        
    elif chtodelete==2:
        cursor.execute("select * from Vehicles")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Vehicles where make_and_model=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Vehicles()
    
    elif chtodelete==3:
        cursor.execute("select * from Vehicles")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Vehicles where service=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Vehicles()
    
    elif chtodelete==4:
        cursor.execute("select * from Vehicles")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Vehicles where model_year=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Vehicles()
        
    else:
        print('Wrong input')
        ADMINDeleting_Vehicles()

def ADMINDeleting_Partslist():
    text ="""        
           Choose what you want to delete        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    print('\nChoice: ')
    text ="""        
           1. Part No.\n2. Part's name\n3. Service type\n4. For which Vehicle\n5. Part Brand\n6. Vehicle year\n7. Part price    
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    chtodelete=int(input("\nInput your choice: "))
    
    if chtodelete==1:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where Parts_no=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist()
        

    
    elif chtodelete==2:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where Parts_name=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist()

    elif chtodelete==3:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where Service_Type=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist() 
        
    elif chtodelete==4:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where For_Model=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist()
    
    elif chtodelete==5:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where Part_Brand=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist()
    
    elif chtodelete==6:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where Vehicle_Year=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
            Yes     [Y]
            No      [N]
            Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist()
    
    elif chtodelete==7:
        cursor.execute("select * from Partslist")
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        print("\n choose data you want to delete: ")
        nod=input("Enter the number of records you want to delete: ")
        query3='delete from Partslist where Part_Price=%s'
        value3=(nod,)
        cursor.execute(query3, value3)
        con.commit()
        data=cursor.fetchall()
        table1=tabulate(data)
        print(table1)
        text ="""       
           Record Deleted Successfully        
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)    
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                ADMINfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            ADMINDeleting_Partslist()
    
    else:
        print("Wrong input")
        ADMINDeleting_Partslist()
    
            
def ADMINAddingParts():
    text ="""       
           Adding Parts to the database        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    partsno=input("Enter Part number: ")
    partsname=input("Enter Part name: ")
    servicetype=input("Enter the service needed for part replacement: ")
    vehiclemodel=input("Enter Vehicle Model: ")
    partbrand=input("Enter Part's brand: ")
    vehicleyear=int(input("Enter Vehicle Model Year: "))
    partprice=input("Parts Price and Currency: ")
    query1="insert into Partslist values(%s,%s,%s,%s,%s,%s,%s)"
    val1=(partsno, partsname, servicetype, vehiclemodel, partbrand, vehicleyear, partprice)
    cursor.execute(query1, val1)
    con.commit()
    print(cursor.rowcount)
    text ="""       
        Record Added Successfully        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    data=cursor.fetchall()
    for i in data:
        print(i)    
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            ADMINfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMINAddingParts()
    

                
def ADMINtable_print():
    cursor.execute("select * from Partslist")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers=columns, tablefmt='double_outline'))
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            ADMINfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMINtable_print()

def ADMINtotalrecords():
    query="select * from Vehicles"
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers=columns, tablefmt='double_outline'))
    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            ADMINfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMINtotalrecords()
    
def ADMINcustomerrecord():
    with open('USERlogin.csv', 'r') as file:
        reader = csv.reader(file, delimiter = '\n')
        for row in reader:
            print(row)
    text ="""        
        Do you want to back to PERVIOUS Menu
    Yes     [Y]
    No      [N]
    Repeat  [R]        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            ADMINfuntion_menu()
    elif ch=='N': 
        text="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        ADMINcustomerrecord()
   

#CSV Sign in and Sign up codes for USER and ADMIN

import csv

def admin_signup():
    with open('ADMINlogin.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        username = input('Input username: ')
        password = input('Input password: ')
        con_password=input('Enter you password again: ')
        if password==con_password:
            writer.writerow([username, password])
            text ="""        
                Registeration Successful
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)     
            ADMINfuntion_menu()
            return True
            
        else:
            text ="""        
                Login Failed
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
    ADMINforgotpass()
    return False

def admin_signin():
    with open('ADMINlogin.csv', mode='r') as file:
        read_csv = csv.reader(file, delimiter=',')
        items = dict(read_csv)

    for i in range(3):
        username = input("Input your name: ")
        password = input("Input your password: ")

        if username in items and password == items[username]:
            text ="""        
                Login Successful
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
            ADMINfuntion_menu()
            return True
        else:
            text ="""        
                Login Failed
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
    ADMINforgotpass()
    return False
    
def user_signup():
    with open('USERlogin.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        text ="""        
            Enter your user name and password
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)       
        username = input('Input username: ')
        password = input('Input password: ')
        con_password=input('Enter you password again: ')
        if password==con_password:
            writer.writerow([username, password])
            text ="""        
                Registeration Successful
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)             
            USERfuntion_menu()
            return True
            
        else:
            text ="""        
                Enter your user name and password
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
    USERforgotpass()
    return False
            
def user_signin():
    with open('USERlogin.csv', mode='r') as file:
        read_csv = csv.reader(file, delimiter=',')
        items = dict(read_csv)

    for i in range(3):
        username = input("Input your name: ")
        password = input("Input your password: ")

        if username in items and password == items[username]:
            text ="""        
                Login Successful
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)     
            USERfuntion_menu()
            return True
        
        else:
            text ="""        
                Login Failed
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
    USERforgotpass()
    return False
    



# Menu for ADMIN

def ADMINdelete_menu():
    text ="""        
                Admin Delete
        Menu      
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. Delete record of the Vehicle\n2. Delete parts\n3. Go back to previous menu
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)    
    ch=int(input("Input: "))
    if ch == 1:
        ADMINDeleting_Vehicles()
    
    elif ch == 2:
        ADMINDeleting_Partslist()
    
    elif ch == 3:
        ADMINfuntion_menu()

    else:
        print("Wrong input")
        
        
        

def ADMINfuntion_menu():
    text ="""        
                Admin Funtion
        Menu      
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. Updating customer's vehicle record\n2. Deleting vehicle record\n3. Adding parts stock\n4. Stock parts list and pricing\n5. Total vehicle records\n6. Total customer record\n7. Adding Date when Vehicle is given back\n8. Vehicle Wheel Alignment Tool\n9. Go back to previous menu
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch = int(input("Input: "))
    if ch == 1:
        ADMINUpdating()    
    
    elif ch == 2:
        ADMINdelete_menu()
        
    elif ch == 3:
        ADMINAddingParts()
        
    elif ch == 4:
        ADMINtable_print()
    
    elif ch == 5:
        ADMINtotalrecords()
    
    elif ch == 6:
        ADMINcustomerrecord()
    
    elif ch == 7:
        ADMIN_date()
    
    elif ch == 8:
        ADMIN_WheelAlignment()
    
    elif ch == 9:
        ADMINmenu()
         
    else:
        print("Wrong input")
    
    
def ADMINmenu():
    text ="""        
                Admin Signin or Signup
        Menu      
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. Admin signup\n2. Admin signin\n3. Go back to Main Menu     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)    
    ch=int(input("Input: "))
    if ch==1:
        admin_signup()
        
    elif ch==2:
        admin_signin()

    else:
        MAINmenu()
    

# Menu for USER

    
def USERpurchases_menu():
    text ="""        
           User Purschase Menu
         
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)    
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1.Buy parts\n2.Update your purschase\n3.Go back
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch= int(input('Input: '))
    if ch==1:
        USERpurchases()
    elif ch==2:
        USERpurchases_update()
    else:
        USERfuntion_menu()

    text ="""        
            Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
        """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=input('Input: ')
    if ch=='Y':
            USERfuntion_menu()
    elif ch=='N': 
        text ="""        
                Logging Out       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
    else:
        USERpurchases_menu()


def USERfuntion_menu():
    text ="""        
                User Funtion
    Menu      
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. Add new Vehicle\n2. Add new service record for current Vehicle\n3. Current Purschases\n4. Search Parts and Prices\n5. Do you want a new Colour for your Vehicle\n6. Go back to USER Menu     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch = int(input("Input: "))
    if ch == 1:
        USERfuntions()

    elif ch == 2:
        text ='''        
                Update your Vehicle Service Record       
        '''
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)        
        vehicleno = input("Input Vehicle no plate: ")
        updatedservice = input("Input new service: ")
        cursor.execute(f"UPDATE Vehicles SET service = '{updatedservice}' WHERE Vehicle_no = '{vehicleno}'")
        con.commit()
        text ="""        
            Record has been Updated       
        """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        text ="""        
                Do you want to back to PERVIOUS Menu
        Yes     [Y]
        No      [N]
        Repeat  [R]        
            """
        table = [[text]]
        output = tabulate(table, tablefmt='rounded_grid')
        print(output)
        ch=input('Input: ')
        if ch=='Y':
                USERfuntion_menu()
        elif ch=='N': 
            text ="""        
                    Logging Out       
            """
            table = [[text]]
            output = tabulate(table, tablefmt='rounded_grid')
            print(output)
        else:
            USERfuntion_menu()

    elif ch == 3:
        USERpurchases_menu() 

    elif ch==4:
        USERsearch_parts()
    
    elif ch==5:

        USERColour_Choice()
    
    elif ch==6:
        USERmenu()
    
    else:
        print("Wrong input")
    

def USERmenu():
    text ="""        
                User Signin or Signup
        Menu      
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. User signup\n2. User signin\n3. Go back to Main Menu     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)    
    ch=int(input("Input: "))
    if ch==1:
        user_signup()
    elif ch==2:
        user_signin()
    else:
        MAINmenu()
        
# Main menu for ADMIN and USER

def MAINmenu():
    text ="""        
            Welcome to Automobile 
    Service Centre       
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           Please Choose an Option        
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    text ="""        
           1. User\n2. Admin.\n3. Exit     
    """
    table = [[text]]
    output = tabulate(table, tablefmt='rounded_grid')
    print(output)
    ch=int(input("Input: "))
    if ch==1:
        USERmenu()
    elif ch==2:
        ADMINmenu()
    else:
        EXIT()

MAINmenu()





