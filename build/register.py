

from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

from cliente import movies


mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="cinema")
mycursor = mydb.cursor()

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Roberto\Desktop\lucas proyecto\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("577x730")
window.configure(bg = "#3C91E6")



def callchk():
        email = entry_1.get()
        password = entry_2.get()
        mycursor.execute('''select case when (%s in (select distinct email from customer) and 
                                    %s in (select distinct password from customer)) then 1 else 0 end as val''',
                                   (email,password))
        sql_qry = mycursor.fetchone()
        if (sql_qry[0] == 0):
            messagebox.showinfo("Error", "Contraseña o Email incorrectos \n Intentar otra vez...")
        else:
            window.destroy()
            mycursor.execute('''select ID from customer where email=%s and password=%s''',(email,password))
            custId = mycursor.fetchall()
            custId = custId[0][0]
            movies(custId)




canvas = Canvas(
    window,
    bg = "#3C91E6",
    height = 730,
    width = 577,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    42.999999999999886,
    83.0,
    anchor="nw",
    text="Cinemar 1000Programadores - UNSa",
    fill="#FAFFFD",
    font=("Arial BoldMT", 30 * -1)
)

canvas.create_text(
    42.999999999999886,
    167.0,
    anchor="nw",
    text="Ingresa tus datos para iniciar sesión",
    fill="#FAFFFD",
    font=("ArialMT", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    224.9999999999999,
    304.0,
    image=entry_image_1
)
entry_1 = Entry(
    window,
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=50.999999999999886,
    y=281.0,
    width=348.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    224.9999999999999,
    418.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=50.999999999999886,
    y=395.0,
    width=348.0,
    height=44.0
)

canvas.create_text(
    42.999999999999886,
    251.0,
    anchor="nw",
    text="E-mail",
    fill="#FAFFFD",
    font=("Arial BoldMT", 18 * -1)
)

canvas.create_text(
    42.999999999999886,
    365.0,
    anchor="nw",
    text="Password",
    fill="#FAFFFD",
    font=("Arial BoldMT", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=callchk,
    relief="flat"
)
button_1.place(
    x=42.999999999999886,
    y=509.0,
    width=158.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()
