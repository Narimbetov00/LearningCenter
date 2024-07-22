import sqlite3

db = sqlite3.connect('texnopost.db')
cursor = db.cursor()

def db_start():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins(
                    chat_id INTEGER,
                    name  TEXT,
                    phone_number TEXT)
                ''')  
    db.commit()
def db_start():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
                    chat_id INTEGER,
                    name  TEXT)
                ''')  
    db.commit()    
def db_start():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS arzalar(
                name  TEXT,
                age   INTEGER,
                username  TEXT,
                phone_number TEXT)
            ''') 
    db.commit() 
cursor.execute('''
CREATE TABLE IF NOT EXISTS giltsozi(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT)
            ''')  
db.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                used_id INTEGER,
                username TEXT,
                mentori TEXT,
                ball TEXT,
                prinsipi TEXT,
                takrarlaw TEXT,
                adminjumisi TEXT,
                qosimsha TEXT
               )
            ''')  
db.commit()
def add_feedback(us_id,us_name,mentor,ball,prin,takr,adminW,qosimsha):
    cursor.execute('''
        INSERT INTO feedback(used_id,username,mentori,ball,prinsipi,takrarlaw,adminjumisi,qosimsha)
                   VALUES(?,?,?,?,?,?,?,?)
            ''',(us_id,us_name,mentor,ball,prin,takr,adminW,qosimsha))
    db.commit()
# cursor.execute('''
#     INSERT INTO giltsozi(name)
#                    VALUES("texnopost")
#                     ''')
# db.commit()
        
def add_datas(id,name,phone):
    cursor.execute('''
    INSERT INTO admins(chat_id,name,phone_number)
                   VALUES(?,?,?)
                    ''',(id,name,phone))
    db.commit()

               
def user_add_datas(id,name):
    cursor.execute('''
    INSERT INTO users(chat_id,name)
                   VALUES(?,?)
                    ''',(id,name))
    db.commit()
def arzalar_add_datas(ati,jasi,userati,nomeri):
    cursor.execute('''
    INSERT INTO arzalar(name,age,username,phone_number)
                   VALUES(?,?,?,?)
                    ''',(ati,jasi,userati,nomeri))
    db.commit()    


def get_admin_data():
    alls=cursor.execute('''
            SELECT chat_id FROM admins 
                                ''').fetchall()
    adminlist = []
    for i in alls:
        for j in i:
            adminlist.append(j)
    return adminlist
def get_admin_us_data():
    alls=cursor.execute('''
            SELECT chat_id FROM admins 
                                ''').fetchall()
    adminlist = []
    for i in alls:
        for j in i:
            adminlist.append(j)
    return adminlist


def get_users_id_name():
    ones = cursor.execute('''
            SELECT chat_id,name FROM users
                                ''').fetchall()
    userIdName = []
    for i in ones:
        for j in i:
            userIdName.append(j)
    return userIdName

def get_users_id():
    oneID = cursor.execute('''
            SELECT chat_id FROM users
                                ''').fetchall()
    userId = []
    for i in oneID:
        for j in i:
            userId.append(j)
    return userId   

def get_users_Arza():
    ones = cursor.execute('''
            SELECT * FROM arzalar
                                ''').fetchall()
    userArzalar = []
    for i in ones:
        for j in i:
            userArzalar.append(j)
    return userArzalar

def get_users_feedback():
    ones1 = cursor.execute('''
            SELECT * FROM feedback
                                ''').fetchall()

    userfeedback= []
    for i in ones1:
        for j in i:
            userfeedback.append(j)

    return userfeedback

     


def delete_admin(user_id):
    cursor.execute(f'''
    DELETE FROM admins
    WHERE chat_id = {user_id}
    ''')
    db.commit()



   
