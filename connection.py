import sqlite3

class movieConn:
    def __init__(self):
        self.con = sqlite3.connect("movies.db")
        #for create table
        self.con.execute("create table if not exists movie(name text, actor text, actress text, director text, year_of_release int)")
        
    def insert(self,name,actor,actress,director,year_of_release):
        #for insert data
        self.con.execute("insert into movie(name,actor,actress,director,year_of_release) values (?,?,?,?,?)",(name,actor,actress,director,year_of_release))
        self.con.commit()
        print("----------------------------------")
        print("Record Inserted Successfully")
    
    def display(self):
        #for display data
        data = self.con.execute("select * from movie")
        for row in data:
            print("-------------------------")
            print("Movie Name is : {}".format(row[0]))
            print("Movie Actor is : {}".format(row[1]))
            print("Movie Actress is : {}".format(row[2]))
            print("Movie Director is : {}".format(row[3]))
            print("Movie Year of Release is : {}".format(row[4]))
        
    def display_2(self,actor,actress):
        data = self.con.execute("select name from movie where actor=? and actress=?",(actor,actress))
        for row in data:
            print("-------------------------")
            print("Movie Name is : {}".format(row[0]))