import sqlite3
from flask import Flask, render_template, request, redirect
from datetime import datetime
import  time, threading
import sqlite3
import  json, socket

"""
Whats new in 1.2?
-home page with buttons
-new page that show the last update of the differente sensers,
a sort of resume of what is going on
-working connection to receive data from Hugo le bg de la street
"""
def application():
    def get_db_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn
    print("love yaa")


    app = Flask(__name__)
#actualisation
    @app.route('/ajax', methods = ['GET'])
    def temp():
        conn = get_db_connection()
        #conn.row_factory = sqlite3.Row
        posts = conn.execute('SELECT * FROM capteurUn').fetchall()
        posts = json.dumps([tuple(row) for row in posts]) 
        conn.close()
        
        return dict(capteurUn = posts)#'{}'.format(capteurUn) 
#---------------------------------------- 

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/capt1')
    def capt1():
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM capteurUn').fetchall()  
        conn.close()
        date = datetime.utcnow()
        return render_template('un.html', capteurUn=posts, launchdate = date) 
    
    @app.route('/Tout')
    def tout():
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM globale').fetchall()
        conn.close()
        return render_template('global.html', globale = posts)
    
    @app.route('/test',methods=["GET","POST"])
    def test():
        if request.method == 'POST':
            req = request.form
            
            min = req['minutes']
            print(min)
            return(redirect(request.url))
        return render_template('un.html')

    app.run(host='0.0.0.0')   
#******************************************************************************************************************************
def database():
    HOST = '172.19.66.163'
    PORT = 50000


    #création du socket
    #mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                                ####################################

    #try:
    #    mySocket.connect((HOST, PORT))
    #except socket.error:
    #    print("La connection a échoué")
    #    sys.exit()
    #print("Connexion réussi avec Hugo le bg de la street")



    connection = sqlite3.connect('database.db')
    
    with open('schema.sql') as f:
        connection.executescript(f.read())

    while True:
        
        print("DATABASE")
        
        connection = sqlite3.connect('database.db') 
        cur = connection.cursor()
        
        try:
            #msgServeur = mySocket.recv(1024).decode("utf-8")
            #print("recu")
            #data = json.loads(msgServeur)
            dict = {"salle": ["F001", "F001"], "seuil": ["144", "84"]}
            jdict = json.dumps(dict)
            data = json.loads(jdict)

            seuil = data["seuil"]
            salle = data["salle"]
            print(seuil)
            print(salle)
            listee = []
            for i in range (len(seuil)):
                listee.append((seuil[i], salle[i]))
            print("liste envoyé dans BDD -->",listee)
            
            print("Listee :   ",listee)

            cur.executemany("INSERT INTO capteurUn (seuil, salle) VALUES (?, ?);", listee)

            cur.executescript("DELETE * FROM globale;")
            cur.executescript("INSERT INTO globale (seuil, salle, temps) SELECT seuil, salle, MAX(time) FROM capteurUn;")

            connection.commit()
            connection.close()
        except:
            print("database : message non recu et non transféré")
        time.sleep(15)                                                                                          #####################
#--------------------------------------------------------------------------------------------------------------------------



x = threading.Thread(target=application)  
y = threading.Thread(target=database)

try:
    x.start()
    y.start()

except:
    print("Unable to start threads") 