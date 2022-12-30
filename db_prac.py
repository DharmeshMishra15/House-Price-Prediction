import mysql.connector



def run1(Location,Area,BHK):
    mydb=mysql.connector.connect(host="localhost",user="root",password="p0p0poke",database="mumbai")
    print(mydb)
    area=(str)(int(Area))
    Area1=(str)(int(Area)+200)
    bhk=(str)(BHK)
    mycursor=mydb.cursor()
    #mydata=(BHK,Area,Area+100)
#    q="select MAX(Price) from mytable where Location=%s and No_of_Bedrooms=%s and Area between %s and %s;",((Location,BHK,Area,Area+200))
    mycursor.execute("select MAX(Price) from mytable where Location=%s and No_of_Bedrooms=%s and Area between %s and %s;",((Location,BHK,Area,Area1)))
    price=mycursor.fetchone()
    Price=(str)(price[0])
    print(Price)
    return Price
