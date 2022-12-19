from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="cinema")
mycursor = mydb.cursor()

""" Registro de usuario """
def signuppge():
    signuppg = Tk()
    signuppg.title("Cinemar 1000Programadores - UNSa")
    signuppg.configure(bg="#3C91E6")

    # Función que cierra la ventana de registro y vuelve a la página de inicio
    def goBack():
        signuppg.destroy()
        welcomePage()

    # Botón para volver a la página de inicio
    Button(signuppg, text="Atrás", command=goBack, cursor="hand2", bg="#3C91E6", relief="flat").pack(side="top", anchor="w")

    # Frame para contener los widgets de la página de registro
    frame = LabelFrame(signuppg, padx=100, pady=100, bg="#3C91E6", relief="flat", bd=0)
    frame.pack(side="top", anchor="center")

    # Título de la página de registro
    Label(frame, text="Registrarse", fg="white", bg="#3C91E6", padx=15, pady=15, font=("Helvetica", 24)).pack(side="top")

    # Campo de entrada para ingresar el nombre
    e = Entry(frame, width=35, borderwidth=5, bg="white", relief="flat")
    e.pack(side="top", pady=15)
    e.insert(0, "Nombre")

    # Campo de entrada para ingresar el email
    e1 = Entry(frame, width=35, borderwidth=5, bg="white", relief="flat")
    e1.pack(side="top", pady=15)
    e1.insert(0, "Email")

    # Campo de entrada para ingresar la contraseña
    e2 = Entry(frame, width=35, borderwidth=5, bg="white", relief="flat", show="*")
    e2.pack(side="top", pady=15)

    # Botón para mostrar contraseña oculta
    def showPassword(entry):
        if entry["show"] == "*":
            entry["show"] = ""
        else:
            entry["show"] = "*"

    buttonShowPass = Button(
    frame,
    text="Mostrar contraseña",
    command=lambda: showPassword(e2),
    cursor="hand2",
    bg="#3C91E6",
    relief="flat"
)

    # Establecer un tamaño de fuente más grande para el texto del botón
    buttonShowPass.config(font=("Arial", 12))

    # Establecer un borde más grueso para el botón
    buttonShowPass.config(bd=5)

    # Establecer un color de fondo diferente para cuando el mouse está sobre el botón
    buttonShowPass.config(activebackground="#3C91E6")

    # Empaquetar el botón y anclarlo al lado izquierdo
    buttonShowPass.pack(side="top", anchor="w")



    def callupdate():
        name = e.get()
        email = e1.get()
        password = e2.get()
        # La función comprueba si el email ya está registrado ejecutando una consulta SQL.
        mycursor.execute('''select case when exists(select email from customer where email=%s) 
                            then 0 else 1 end as val''',(email,))
        sql_query = mycursor.fetchall()
        sql_query = sql_query[0][0]
        print(sql_query)
        if(sql_query==0): # mensaje de error por si el email ya esta registrado
            messagebox.showinfo("Error", "Email registrado,\nusar otro")
        else: # si el email no esta registrado inserta los nuevos datos a la DB
            mycursor.execute("insert into customer(name,email,password) values(%s,%s,%s)", (name, email, password))
            mydb.commit()
            mycursor.execute('''select max(ID) from customer''')
            custId = mycursor.fetchall()
            custId = custId[0][0]
            signuppg.destroy()
            movies(custId)

    signup1 = Button(frame, text="Registrarse", command=callupdate, cursor="hand2", bg="white", relief="flat").pack(side="top", pady=15)


def loginpge():
    loginpg = Tk()
    loginpg.title("Cinemar 1000Programadores - UNSa")
    def goBack():
        loginpg.destroy()
        welcomePage()
    Button(text="Atrás",command=goBack, cursor="hand2").pack()
    frame = LabelFrame(loginpg, padx=100, pady=100)
    frame.pack()
    lable = Label(frame, text="Login", fg="white", bg="blue", padx=15, pady=15).grid(row=0, column=4)
    e1 = Entry(frame, width=35, borderwidth=5)
    e1.grid(row=2, column=3, columnspan=3, padx=10, pady=15)
    e1.insert(0, "Ingresa tu Email")
    e2 = Entry(frame, width=35, borderwidth=5)
    e2.grid(row=3, column=3, columnspan=3, padx=10, pady=15)
    e2.insert(0, "Ingresar Contraseña")

    def callchk():
        email = e1.get()
        password = e2.get()
        mycursor.execute('''select case when (%s in (select distinct email from customer) and 
                                    %s in (select distinct password from customer)) then 1 else 0 end as val''',
                                   (email,password))
        sql_qry = mycursor.fetchone()
        if (sql_qry[0] == 0):
            messagebox.showinfo("Error", "Contraseña o Email incorrectos \n Intentar otra vez...")
        else:
            loginpg.destroy()
            mycursor.execute('''select ID from customer where email=%s and password=%s''',(email,password))
            custId = mycursor.fetchall()
            custId = custId[0][0]
            movies(custId)

    login1 = Button(frame, text="Iniciar Sesion", command=callchk, bg='blue', fg='white', cursor="hand2").grid(row=5, column=4, pady=30)


""" Seleccionar función """
def callTheatrePage(movie_id, custId):
    thtpg = tk.Tk()
    thtpg.title("Cinemar 1000Programadores - UNSa")
    thtpg.geometry("600x400")
    thtpg.configure(background="#3C91E6")
    
    def goBack():
        thtpg.destroy()
        movies(custId)
    
    query = '''select s.ID,t.name,start_time,show_date,hall_ID
               from shows s,theatre t
               where s.movie_ID=%s and s.theatre_ID=t.ID
               order by show_date,start_time'''
    mycursor.execute(query,(movie_id,))
    shows = mycursor.fetchall()
    mycursor.execute('select name from movie where ID=%s',(movie_id,))
    movie_name = mycursor.fetchall()
    movie_name = movie_name[0][0]
    r = tk.IntVar()
    
    lbl_title = tk.Label(thtpg, text=movie_name, font=("Helvetica", 20), background="#342E37", foreground="#FFFFFF")
    lbl_title.pack(pady=20)
    
    f = tk.Frame(thtpg)
    f.pack(pady=20)
    f.configure(background="#3C91E6")
    
    lbl_theatre = tk.Label(f, text="Teatro", font=("Helvetica", 14), background="#FA824C")
    lbl_time = tk.Label(f, text="Hora", font=("Helvetica", 14), background="#FA824C")
    lbl_date = tk.Label(f, text="Fecha", font=("Helvetica", 14), background="#FA824C")
    lbl_hall = tk.Label(f, text="Sala", font=("Helvetica", 14), background="#FA824C")
    lbl_theatre.grid(row=0, column=1)
    lbl_time.grid(row=0, column=2)
    lbl_date.grid(row=0, column=3)
    lbl_hall.grid(row=0, column=4)
    
    def clicked(show_ID):
        if show_ID == 0:
            messagebox.showinfo("Error", "Elige una función")
        else:
            thtpg.destroy()
            seats(show_ID, custId)
    
    R = 1
    for sh in shows:
        rb = tk.Radiobutton(f, variable=r, value=sh[0], font=("Helvetica", 14), background="#3C91E6", activebackground="#FFFFFF", cursor="hand2")
        rb.grid(row=R, column=0)
        lbl_theatre_name = tk.Label(f, text=str(sh[1]), font=("Helvetica", 14), background="#3C91E6")
        lbl_time_value = tk.Label(f, text=str(sh[2]), font=("Helvetica", 14), background="#3C91E6")
        lbl_date_value = tk.Label(f, text=str(sh[3]), font=("Helvetica", 14), background="#3C91E6")
        lbl_hall_value = tk.Label(f, text="Sala: " + str(sh[4]), font=("Helvetica", 14), background="#3C91E6")
        lbl_theatre_name.grid(row=R, column=1)
        lbl_time_value.grid(row=R, column=2)
        lbl_date_value.grid(row=R, column=3)
        lbl_hall_value.grid(row=R, column=4)
        R = R + 1
    
    btn_back = tk.Button(thtpg, text="Atrás", command=goBack, font=("Helvetica", 14), background="#FFFFFF", cursor="hand2")
    btn_back.pack(side=tk.LEFT, padx=20, pady=20)
    
    btn_confirm = tk.Button(thtpg, text="Confirmar", command=lambda: clicked(r.get()), font=("Helvetica", 14), background="#FFFFFF", cursor="hand2")
    btn_confirm.pack(side=tk.RIGHT, padx=20, pady=20)
    
    thtpg.mainloop()

""" Selecciona pelicula """
def movies(custID):
    movie = tk.Tk()
    movie.title("Cinemar 1000Programadores - UNSa")
    movie.geometry("600x600")
    movie.configure(background="#3C91E6")
    
    def goBack():
        movie.destroy()
        mycursor.execute('''select max(ID) from customer''')
        maxID = mycursor.fetchall()
        maxID = maxID[0][0]
        if custID == maxID:
            signuppge()
        else:
            loginpge()
    
    frame = tk.LabelFrame(movie, padx=100, pady=100, background="#3C91E6")
    frame.pack()
    
    mycursor.execute('select ID,name from movie')
    lst = mycursor.fetchall()
    
    lbl_title = tk.Label(frame, text="Seleccionar Película", font=("Helvetica", 20), fg="#FFFFFF", bg="#342E37", padx=15, pady=15)
    lbl_title.pack()
    
    def clicked(id):
        if id == 0:
            messagebox.showinfo("Error", "Por favor elige una película")
        else:
            movie.destroy()
            callTheatrePage(id, custID)
    
    r = tk.IntVar()
    for k in lst:
        rb = tk.Radiobutton(frame, text=k[1], font=("Helvetica", 14), variable=r, value=k[0], background="#3C91E6", activebackground="#FFFFFF", cursor="hand2")
        rb.pack()
    
    btn_select = tk.Button(frame, text="Seleccionar", font=("Helvetica", 14), background="#FFFFFF", cursor="hand2", command=lambda: clicked(r.get()))
    btn_select.pack()
    
    btn_back = tk.Button(movie, text="Atrás", font=("Helvetica", 14), background="#FFFFFF", cursor="hand2", command=goBack)
    btn_back.pack(side=tk.LEFT, padx=20, pady=20)
    
    movie.mainloop()


def welcomePage():
    root = Tk()
    root.title("Cinemar 1000Programadores - UNSa")
    frame = LabelFrame(root, padx=100, pady=100)
    frame.pack()
    lable = Label(frame, text="Regístrate o ingresa a tu cuenta", pady=30, font='Helvetica 10 bold').grid(row=0, column=4)
    def signupbtn():
        root.destroy()
        signuppge()

    def loginbtn():
        root.destroy()
        loginpge()
    login = Button(frame, text="Iniciar Sesion", command=loginbtn, bg='blue', fg='white', cursor="hand2").grid(row=5, column=0)
    signup = Button(frame, text="Registrarse", command=signupbtn, bg='blue', fg='white', cursor="hand2").grid(row=5, column=8)
    root.mainloop()


""" Seleccionar asiento """
def seats(show_ID,custId): #show_ID id de las peliculas
    mycursor.execute('''select hall_ID,theatre_ID from shows where ID=%s''',(show_ID,))
    info = mycursor.fetchall()
    h_ID = info[0][0]
    t_ID = info[0][1]
    mycursor.execute('''select capacity from hall where ID=%s and theatre_ID=%s''',(info[0][0],info[0][1]))
    info = mycursor.fetchall()
    info = info[0][0]
    seatPage = Tk()
    def goBack():
        seatPage.destroy()
        mycursor.execute('''select movie_ID from shows where ID=%s''',(show_ID,))
        movie_ID = mycursor.fetchall()
        movie_ID = movie_ID[0][0]
        callTheatrePage(movie_ID,custId)
    Button(text="Atrás",command=goBack, cursor="hand2").pack()
    Label(text="Seleccionar un asiento",font="200",pady=10).pack()
    Label(text="Verde=Disponible",font="100",padx=50).pack()
    f = Frame(seatPage,padx=100,pady=20,bg="#3C91E6")
    f.pack()
    status = []
    chkbtn = []
    mycursor.execute('''select seat_ID from books where show_ID=%s''',(show_ID,))
    data = mycursor.fetchall()

    # Asientos 
    booked = [] # Se crea una lista vacia para guardar los asientos reservados
    for i in data:
        # itera sobre los resultados de una consulta SQL de asientos reservados
        booked.append(i[0])
    mycursor.execute('''SELECT seat_ID from seatinline where show_ID=%s and book_date=curdate() 
                        and (cast(curtime() as time)-cast(book_time as time))<=1000''',(show_ID,))
    data = mycursor.fetchall() # fetchall() devuelve todas las filas.
    for i in data:
        booked.append(i[0])
        # Crea una matriz de botones de verificación para cada uno de los asientos disponibles en el cine.
    for i in range(0,info):
        var = IntVar()
        chk = Checkbutton(f,variable=var,onvalue=1,offvalue=0,padx=40,pady=40,selectcolor="green",fg="white",bg="#6ECC80", cursor="hand2")
        chkbtn.append(chk) # se crean checkbox para cada uno de los asientos disponibles en el cine. 
        status.append(var) # agregra la variable var (instancia de IntVar. tipo de variable de tkinter)
    for i in booked: #se recorre la lista de asientos reservados y se deshabilitan los checkbox anteriormente clickeados.
        chkbtn[i-1] = Checkbutton(f,state="disabled",padx=10,pady=10,selectcolor="red",bg="white")
    R = 0
    C = 0
    for i in range(0,info):
        chkbtn[i].grid(row=R,column=C)
        C = C+1
        if(C>=10): #se usa una matriz con 10 columnas con un número de filas suficiente.
            C = 0
            R = R+1
    def clicked():
        newBooked = []
        chk = 0
        for i in range(0,len(status)):
            if(status[i].get()==1):
                chk=1
                newBooked.append(i+1)
        if(chk==0):
            messagebox.showinfo("Error", "Selecciona un asiento")
        else:
            seatPage.destroy()
            callPaymentPage(show_ID,newBooked,custId)
    Label(pady=20,text="_________________________________________________________________________________________").pack()
    Button(text="Confirmar",padx=50,pady=10,font="100",command=clicked, cursor="hand2").pack()
    seatPage.mainloop()

def callPaymentPage(show_ID,newBooked,custId):
    for i in newBooked:
        mycursor.execute('''insert into seatinline(seat_ID,show_ID,book_time,book_date) values
                            (%s,%s,curtime(),curdate())''',(i,show_ID))
    mydb.commit()
    payPage = Tk()
    def goBack():
        payPage.destroy()
        seats(show_ID,custId)
    Button(text="Atrás",command=goBack, cursor="hand2").pack()
    mycursor.execute('''select* from shows where ID=%s''',(show_ID,))
    show_info = mycursor.fetchall()
    mycursor.execute('''select name from movie where ID=%s''', (show_info[0][1],))
    movie_name = mycursor.fetchall()
    movie_name = movie_name[0][0]
    mycursor.execute('''select name from theatre where ID=%s''', (show_info[0][3],))
    theatre_name = mycursor.fetchall()
    theatre_name = theatre_name[0][0]
    Label(text="Pagar",font="500",padx=200,bg="green",fg="white").pack()
    f = Frame(payPage,bg="grey")
    f.pack()
    fl_amt = int(show_info[0][7])*len(newBooked)
    amt = str(fl_amt)
    def clicked():
        payPage.destroy()
        mycursor.execute('''insert into payment(amt,pay_time,pay_date)
                            values(%s,curtime(),curdate())''',(fl_amt,))
        mydb.commit()
        mycursor.execute('''select max(ID) from payment''')
        pay_ID = mycursor.fetchall()
        pay_ID = pay_ID[0][0]
        for i in newBooked:
            mycursor.execute('''insert into books
                                 values(%s,%s,%s,%s)''',(custId,i,show_ID,pay_ID))
        mydb.commit()
        messagebox.showinfo("Aviso","Pago completado")
        for i in newBooked:
            mycursor.execute('''delete from seatinline where seat_ID=%s and show_ID=%s''',(i,show_ID))
        mydb.commit()
    Label(f,text="Película:",font="50",padx=200,bg="grey").grid(row=1)
    Label(f,text="Sala:",font="50",padx=200,bg="grey").grid(row=2)
    Label(f,text="Cine:",font="50",padx=200,bg="grey").grid(row=3)
    Label(f,text="Hora de inicio:", font="50", padx=200,bg="grey").grid(row=4)
    Label(f,text="Hora de finalización:", font="50", padx=200,bg="grey").grid(row=5)
    Label(f,text="Fecha:", font="50", padx=200,bg="grey").grid(row=6)
    Label(f,text="Precio:", font="50", padx=200,bg="grey").grid(row=7)
    Label(f,text="Asientos:",font="50", padx=200,bg="grey").grid(row=8)
    Label(f,text=movie_name, font="50", padx=200,bg="grey").grid(row=1,column=1)
    Label(f,text=show_info[0][2], font="50", padx=200,bg="grey").grid(row=2,column=1)
    Label(f,text=theatre_name, font="50", padx=200,bg="grey").grid(row=3,column=1)
    Label(f,text=show_info[0][4], font="50", padx=200,bg="grey").grid(row=4,column=1)
    Label(f,text=show_info[0][5], font="50", padx=200,bg="grey").grid(row=5,column=1)
    Label(f,text=show_info[0][6], font="50", padx=200,bg="grey").grid(row=6,column=1)
    Label(f,text=amt, font="50", padx=200,bg="grey").grid(row=7,column=1)
    desc = ""
    for i in newBooked:
        desc += "  "+str(i)
    Label(f, text=desc, font="50", padx=200, bg="grey").grid(row=8, column=1)
    b = Button(payPage,command = clicked,text="Pagar",font="50",bg="#3C91E6",fg="white", cursor="hand2")
    b.pack()
    payPage.mainloop()


# export like module movies



