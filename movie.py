from connection import *

class movie:
    def getDetails(self):
        self.name = input("Enter the Movie Name : ")
        self.actor = input("Enter the Actor Name : ")
        self.actress = input("Enter the Actress Name : ")
        self.director = input("Enter the Director Name : ")
        self.year_of_release = input("Enter the Year Of Release : ")

    def insertDetails(self):
        con = movieConn()
        self.getDetails()
        con.insert(self.name,self.actor,self.actress,self.director,self.year_of_release)

    def displayDetails(self):
        con = movieConn()
        con.display()

    def displayDetails_2(self):
        con = movieConn()
        actor = input("Enter Actor Name : ")
        actress = input("Enter Actress Name : ")
        con.display_2(actor,actress)
        
#create object
obj = movie()

while(True):
    print("1 : Inserted Data")
    print("2 : Display Data")
    print("3 : Display Data Based on Actor Name")
    print("4 : Exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        obj.insertDetails()
    elif ch == 2:
        obj.displayDetails()
    elif ch == 3:
        obj.displayDetails_2()
    elif ch == 4:
        break
    else:
        print("Enter Valid Choice...")