import sqlite3 as sq


def send(username,Name,City,Phone,Gender,Answer,Password):
    conn = sq.connect('house.db')
    c = conn.cursor()
    c.execute("insert into users values(?,?,?,?,?,?,?)",(username,Name,City,Phone,Gender,Answer,Password))
    #print(c.fetchall())


    conn.commit()
    conn.close()

def authenticate(Username):
    conn = sq.connect('house.db')
    c = conn.cursor()
    c.execute("select password from users where username = ?",(Username,))
    l=(c.fetchone())
    Passwordex=(str)(l[0])
    print(Passwordex)
    conn.commit()
    conn.close()
    return Passwordex

def pred():
    pass