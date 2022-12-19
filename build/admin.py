from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="cinema")
mycursor = mydb.cursor()

# Agregar Película
def addMov():
    mov = tk.Tk()
    
    def goBack():
        mov.destroy()
        Admin()
        
    tk.Button(text="Atrás", command=goBack).pack()
    mov.title("Admin")
    
    frame = tk.LabelFrame(mov, padx=100, pady=100)
    frame.pack()
    
    # Crea etiquetas y widgets de entrada utilizando un bucle for. 
    fields = [
        ("Nombre", 1),
        ("Idioma", 2),
        ("Género", 3),
        ("Duración", 4),
    ]
    for i, (field, row) in enumerate(fields):
        tk.Label(frame, text=field).grid(row=row, column=1, padx=10, pady=15)
        e = tk.Entry(frame, width=35, borderwidth=5)
        e.grid(row=row, column=2, columnspan=3, padx=10, pady=15)
        # almacena el widget en una lista para que despues se pueda acceder
        fields[i] = e
    
    tk.Label(text="Ingresa la duración en el siguiente formato HH:MM:SS").pack()
    
    def callchk1():
        name = fields[0].get()
        language = fields[1].get()
        genre = fields[2].get()
        length = fields[3].get()
        mycursor.execute('''insert into movie(name,language,genre,length) values(%s,%s,%s,%s)''',(name,language,genre,length))
        mydb.commit()
        mov.destroy()
        messagebox.showinfo("Siguiente", "Película agregada")
        
    tk.Button(mov, text="Agregar", command=callchk1).pack(pady=30)
    tk.Button(mov, text="Atrás").pack()
    
    mov.mainloop()


# Agregar Cine
def addTh():
    th = Tk()
    def goBack():
        th.destroy()
        Admin()
    Button(text="Atrás", command=goBack).pack()
    th.title("Admin")
    frame = LabelFrame(th, padx=100,pady=100 )
    frame.pack()
    e1 = Entry(frame,width=35,borderwidth=5)
    e1.grid(row = 2,column=3,columnspan=3,padx=10,pady=15)
    e1.insert(0,"Nombre")
    e2 = Entry(frame, width=35, borderwidth=5)
    e2.grid(row=4, column=3, columnspan=3, padx=10, pady=15)
    e2.insert(0, "Código Postal")
    e3 = Entry(frame,width=35,borderwidth=5)
    e3.grid(row = 4,column=3,columnspan=3,padx=10,pady=15)
    e3.insert(0,"Ciudad")
    e4 = Entry(frame,width=35,borderwidth=5)
    e4.grid(row = 5,column=3,columnspan=3,padx=10,pady=15)
    e4.insert(0,"Código Postal")
    def callchk1():
        name = e1.get()
        road = e2.get()
        city = e3.get()
        pincode = e4.get()
        mycursor.execute('''insert into theatre(name,road,city,pincode) values(%s,%s,%s,%s)''',(name,road,city,pincode))
        mydb.commit()
        th.destroy()
    add = Button(th,text="Agregar",command=callchk1)
    add.pack(pady= 30)
    back = Button(th,text="Atrás")
    back.pack()
    th.mainloop()
    messagebox.showinfo("Siguiente", "Cine Agregado correctamente")

# Elegir Sala
def hallchooseTh():
    hallPg = Tk()
    def goBack():
        hallPg.destroy()
        Admin()
    Button(text="Atrás", command=goBack).pack()
    Label(text="Elegir Cine",font="70").pack()
    mycursor.execute('''select ID,name from theatre''') #muestra lista de cines disponibles
    th_info = mycursor.fetchall()
    f = Frame()
    f.pack(padx=200,pady=50)
    R = 1
    r = IntVar()
    for th in th_info:
        Radiobutton(f, font="50", variable=r, value=th[0]).grid(row=R, column=0)
        Label(f, text=th[1], font="50").grid(row=R, column=1)
        R = R + 1
    def clicked(ID):
        if(ID==0):
            print("Error", "Elige un Cine") # muestra mensaje de error si no selecciona un cine
        else:
            hallPg.destroy()
            hallchooseCap(ID) #Se abre una nueva ventana en donde se puede seleccionar una sala
    Button(text="Siguiente",command=lambda :clicked(r.get())).pack()
    hallPg.mainloop()

# Agregar Sala
def hallchooseCap(ID):
    hallPg = Tk()
    def goBack():
        hallPg.destroy()
        hallchooseTh()
    Button(text="Atrás", command=goBack).pack()
    Label(text="Ingresar capacidad de sala",font="100",padx=100,pady=100).pack()
    e = Entry()
    e.pack()
    def clicked():
        val = e.get()
        mycursor.execute('''insert into hall(theatre_ID,capacity) values(%s,%s)''',(ID,val))
        mydb.commit()
        hallPg.destroy()
    Button(text="Siguiente",font="50",command=clicked,padx=100,pady=20).pack()
    hallPg.mainloop()
    messagebox.showinfo("Siguiente", "Sala agregada correctamente")

def chooseShowMovie():
    movPg = Tk() #muestra una lista de películas disponibles
    def goBack():
        movPg.destroy()
        Admin()
        # se puede seleccionar una película de la lista haciendo clic
    Button(text="Atrás", command=goBack).pack()
    Label(text="Elegir Película",font="50").pack()
    frame = Frame(movPg)
    frame.pack()
    mycursor.execute('select ID,name from movie')
    lst = mycursor.fetchall()
    r = IntVar()
    for k in lst:
        rb = Radiobutton(frame, text=k[1], font="50", variable=r, value=k[0],padx=100).pack()
    def clicked(mov_ID):
        if (mov_ID == 0):
            messagebox.showinfo("Error", "Elegir una Película")
        else:
            movPg.destroy()
            chooseShowTheatre(mov_ID) # Si el usuario ha seleccionado una película,se abre una nueva ventana donde se pueden seleccionar los cines donde se proyectará la película seleccionada
    Button(text="Siguiente",font="50",command=lambda :clicked(r.get())).pack()
    movPg.mainloop()

def chooseShowTheatre(mov_ID):
    thtPg = Tk() # muestra una lista de cines disponibles
    def goBack():
    # se puede seleccionar un cine de la lista haciendo clic
        thtPg.destroy()
        chooseShowMovie()
    Button(text="Atrás", command=goBack).pack()
    Label(text="Elegir Cine", font="50").pack()
    frame = Frame(thtPg)
    frame.pack()
    mycursor.execute('select ID,name from theatre')
    lst = mycursor.fetchall()
    r = IntVar()
    for k in lst:
        rb = Radiobutton(frame, text=k[1], font="50", variable=r, value=k[0],padx=100).pack()
    def clicked(t_ID):
        if(t_ID==0):
            messagebox.showinfo("Error","Elegir un Cine")
        else:
        # si se selecciona un cine, se abre una ventana donde se pueden seleccionar las salas de cine disponibles.
            thtPg.destroy()
            chooseShowHall(mov_ID,t_ID)
    Button(text="Siguiente",command=lambda:clicked(r.get())).pack()
    thtPg.mainloop()

def chooseShowHall(mov_ID,t_ID):
    hallPg = Tk() # muestra una lista de salas de cine disponibles en el cine y pelicula especificada.
    def goBack():
        hallPg.destroy()
        chooseShowTheatre(mov_ID)

    Button(text="Atrás", command=goBack).pack()
    Label(text="Elegir Cine", font="50").pack()
    frame = Frame(hallPg)
    frame.pack()
    mycursor.execute('select ID,capacity from hall where theatre_ID=%s',(t_ID,))
    lst = mycursor.fetchall()
    r = IntVar()
    for k in lst:
        rb = Radiobutton(frame, text=str(k[0])+"  capacidad:"+str(k[1]), font="50", variable=r, value=k[0],padx=100).pack()
# se puede seleccionar una sala de cine de la lista
    def clicked(h_ID):
        if (h_ID == 0):
            messagebox.showinfo("Error", "Elegir una Sala")
        else:
        # se abre una nueva ventana donde se puede ingresar la hora de inicio de la proyección de la película.
            hallPg.destroy()
            enterStartTime(mov_ID,t_ID,h_ID)

    Button(text="Siguiente", command=lambda: clicked(r.get())).pack()
    hallPg.mainloop()

def enterStartTime(mov_ID,t_ID,h_ID):
    timePg = Tk() # permite ingresar la hora de inicio, la fecha y el precio de la proyección de la película
    def goBack():
        timePg.destroy()
        chooseShowHall(mov_ID,h_ID) # mov_ID especifica la pelicula, h_id la sala
    Button(text="Atrás",font="50",command=goBack).pack()
    Label(text="Ingresar hora de inicio(HH:MM:SS)",font="50").pack()
    e1 = Entry()
    e1.pack()
    Label(text="Ingresar fecha(YYYY-MM-DD)", font="50").pack()
    e2 = Entry()
    e2.pack()
    Label(text="Ingresar precio", font="50").pack()
    e3 = Entry()
    e3.pack()
    def clicked():
    # Se obtiene la hora de inicio. la fecha y el precio. Ademas calcula la hora en la que termina la pelicula
        val1 = e1.get()
        val2 = e2.get()
        val3 = e3.get()
        mycursor.execute('''select length from movie where ID=%s''',(mov_ID,))
        length = mycursor.fetchall()
        length = length[0][0]
        mycursor.execute('''select cast(%s as time)+cast(%s as time)''', (val1, length))
        chk = mycursor.fetchall()
        chk = chk[0][0]
        if(chk>=240000):
            chk=0
        else:
            chk=1
        mycursor.execute('''select cast(cast(%s as time)+cast(%s as time) as time)''',(val1,length))
        en_time = mycursor.fetchall()
        en_time = en_time[0][0]
        if(chk==0):
            messagebox.showinfo("Error","Horario inválido") # si el horario de la funcion es igual o mayor a 00:00:00 muestra un error.
        else:
            mycursor.execute('''select cast(%s as time)''',(val1,))
            val1 = mycursor.fetchall()
            val1 = val1[0][0]
            mycursor.execute('''select cast(%s as date)''', (val2,))
            val2 = mycursor.fetchall()
            val2 = val2[0][0]
            mycursor.execute('''select cast(%s as time)''', (en_time,))
            en_time = mycursor.fetchall()
            en_time = en_time[0][0]
            mycursor.execute('''select* from shows''')
            info = mycursor.fetchall()
            for i in info:
                if(mov_ID==i[1] and t_ID==i[2] and h_ID==i[3] and str(val2)==str(i[6])):
                    if((val1<=i[4] and i[4]<=en_time)or(val1<=i[5] and i[5]<=en_time)or
                        (i[4]<=val1 and val1<=i[5])or(i[4]<=en_time and en_time<=i[5])):
                        messagebox.showinfo("Error","Choque de horario") # Si el horario de una funcion coincide con otra, muestra un error.
                        chk=0
                        break
            if(chk==1):
                mycursor.execute('''insert into shows(movie_ID,hall_ID,theatre_ID,start_time,end_time,show_date,price) values
                                    (%s,%s,%s,%s,%s,%s,%s)''',(mov_ID,h_ID,t_ID,val1,en_time,val2,val3))
                mydb.commit()
                timePg.destroy()
                messagebox.showinfo("Siguiente","Función agregada")


    Button(text="Completar",font="50",command=clicked).pack()
    timePg.mainloop()

def Admin():
    root = Tk()
    def movie():
        root.destroy()
        addMov()
    def theatre():
        root.destroy()
        addTh()
    def hall():
        root.destroy()
        hallchooseTh()
    def show():
        root.destroy()
        chooseShowMovie()
        
    Button(
        text="Agregar Película",
        font="50",
        command=movie,
        padx=100,
        pady=50,
        bg="#1e9fff",
        fg="black",
        activebackground="white",
        activeforeground="black",
        borderwidth=5,
        relief="raised",
    ).pack()
    Button(
        text="Agregar Cine",
        font="50",
        command=theatre,
        padx=110,
        pady=50,
        bg="#1e9fff",
        fg="black",
        activebackground="white",
        activeforeground="black",
        borderwidth=5,
        relief="raised",
    ).pack()
    Button(
        text="Agregar Sala",
        font="50",
        command=hall,
        padx=110,
        pady=50,
        bg="#1e9fff",
        fg="black",
        activebackground="white",
        activeforeground="black",
        borderwidth=5,
        relief="raised",
    ).pack()
    Button(
        text="Agregar Función",
        font="50",
        command=show,
        padx=100,
        pady=50,
        bg="#1e9fff",
        fg="black",
        activebackground="white",
        activeforeground="black",
        borderwidth=5,
        relief="raised",
    ).pack()
    root.mainloop()