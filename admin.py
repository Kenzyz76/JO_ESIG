import class
import class2
from mysql.connector import connect

class ActeurDAO:
    def connection():
        bdd=connect(host="localhost",user="root",
                    password="root",database="Olympiques")
        return(bdd)