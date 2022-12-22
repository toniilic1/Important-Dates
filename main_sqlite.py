import sqlite3

conn = sqlite3.connect('date_library.db')
c = conn.cursor()

c.execute("""CREATE TABLE if not exists dates(
    name text,
    date1 text,
    date2 text
) """)

conn.commit()
conn.close()

class CRUD:
    def create(inname, indate1, indate2):
        conn = sqlite3.connect('date_library.db')
        c = conn.cursor()
        c.execute("INSERT INTO dates VALUES (:name, :date1, :date2)",
        {
            "name" : inname,
            "date1" : indate1,
            "date2" : indate2
        }
        )
        conn.commit()
        conn.close()

    def read(one_all):

        if one_all == 'l':
            conn = sqlite3.connect('date_library.db')
            c = conn.cursor()
            all_query = "SELECT *, oid FROM dates"
            c.execute(all_query)
            records_all = c.fetchall()
            for record in records_all:
                print(record[3], record[0], record[1], record[2])
            c.close()

        elif one_all == 'o':
            inid = input("Input person ID: ")
            conn = sqlite3.connect('date_library.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM dates WHERE oid= " + inid)
            records_one = c.fetchall()
            for record in records_one:
                print(record[3], record[0], record[1], record[2])
            c.close()



    def update(upid, upname, up_date1, up_date2):
        conn = sqlite3.connect('date_library.db')
        c = conn.cursor()
        c.execute(f"UPDATE dates SET name = ?, date1 = ?, date2 = ? WHERE oid = ?", (upname, up_date1, up_date2, upid))
        conn.commit()
        conn.close()

    def delete(indel):
        conn = sqlite3.connect('date_library.db')
        c = conn.cursor()
        c.execute("DELETE from dates WHERE oid=" + indel)
        conn.commit()
        conn.close()
        print("ID Sucessfully deleted.")

def msg():
    global prompt
    prompt = input('Create(c), Read(r), Update(u), Delete(d) or Quit(q)?: ')

    while prompt not in('c', 'r', 'u', 'd', 'q'):
        print('Answer must be (c), (r), (u), (d) or (q), try again')
        prompt = input('Create(c), Read(r), Update(u), Delete(d) or Quit(q)?: ')

msg()

while True:
    if prompt == 'c':
        p_name = input("Input a name: ")
        p_date1 = input("Input a date: ")
        p_date2 = input("Input a second date: ")
        CRUD.create(p_name, p_date1, p_date2)
        msg()

    elif prompt == 'r':
        one_all = input('List(l) or One(o): ')
        CRUD.read(one_all)
        msg()

    elif prompt == 'u':
        upid = input('Update ID: ')
        upname = input('Update Name: ')
        up_date1 = input('Update Date 1 = ')
        up_date2 = input('Update Date 2 = ')
        CRUD.update(upid, upname, up_date1, up_date2)
        msg()

    elif prompt == 'd':
        deletion = input("Delete ID: ")
        CRUD.delete(deletion)
        msg()

    elif prompt == 'q':
        break