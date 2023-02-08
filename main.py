import Tkinter as tk
from eulexistdb import db

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = ''
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/mp03uf6"
db = db.ExistDB(server_url=EXISTDB_SERVER_URL, username='admin', password='')


def ferQuary():
    try:
        query =ent_nom.get()
        res = db.executeQuery(query)
        hits = db.getHits(res)
        text = ""
        for i in range(hits):
            text += str(db.retrieve(res, i))+"\n"
        lbl_nom.config(text=text)
        print(text)
    except (Exception ) as error:
        lbl_nom.config(text="T'has equivocat amb la busqueda")


window = tk.Tk()
window.title('AleixC')

lbl_nom = tk.Label(master=window,
    text="",
    foreground="#00FF00",  # Set the text color to white
    background="black",  # Set the background color to black
    width="80",
    justify=tk.LEFT
)

ent_nom = tk.Entry(master=window, width="45")

btn_entrarNom = tk.Button(master=window, text="Submit", command=ferQuary)

ent_nom.pack()
btn_entrarNom.pack()
lbl_nom.pack()

window.mainloop()
