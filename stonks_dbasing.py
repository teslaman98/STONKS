import sqlite3

conn = sqlite3.connect('STONKS.db')
c = conn.cursor()



def create_table():
    c.execute("CREATE TABLE (Language VARCHAR, Version REAL, Skill TEXT)")

"""
def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 3.6, 'Beg')")
    c.execute("INSERT INTO example VALUES('Python', 3.7, 'Int')")
    c.execute("INSERT INTO example VALUES('Python', 3.8, 'Mast')")
    conn.commit()

def enter_dynamic_data():
    lang = input("What Lang?: ")
    version = float(input("What version?: "))
    skill = input("What skill level?: ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?,?,?)", (lang,version,skill))
    conn.commit()

def read_from_database():
    what_skill = input("What skill level are we looking for? ")
    what_language = input("What language?: ")

    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"

    for row in c.execute(sql, [(what_skill), (what_language)]):
        print (row)

def read_entire_dbase():
    #sql = "DELETE FROM example LIMIT 2"
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print (row)
    conn.commit()

def delete_from_dbase():
    sql = "DELETE FROM example"
    for row in c.execute(sql):
        print (row)
    conn.commit()

"""


#delete_from_dbase()
#read_from_database()
#enter_data()
#enter_dynamic_data()
#read_entire_dbase()
#conn.close()



"""def read_entire_dbase():
    sql = "SELECT * FROM example LIMIT 2"
    for row in c.execute(sql):
        print (row)
"""