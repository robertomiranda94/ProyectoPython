from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Roberto\Desktop\Nueva carpeta (8)\movie\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1091x832")
window.configure(bg = "#FFDBDB")


canvas = Canvas(
    window,
    bg = "#FFDBDB",
    height = 832,
    width = 1091,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    200.0,
    832.0,
    fill="#C4C4C4",
    outline="")

canvas.create_text(
    48.0,
    27.0,
    anchor="nw",
    text="Black Panther",
    fill="#FFFFFF",
    font=("Inika", 24 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_1_blue.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=21.0,
    y=23.0,
    width=157.0,
    height=71.0
)



button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=21.0,
    y=231.0,
    width=157.0,
    height=71.0
)

canvas.create_text(
    48.0,
    250.0,
    anchor="nw",
    text="Top Gun",
    fill="#FFFFFF",
    font=("Inika", 24 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=21.0,
    y=127.0,
    width=157.0,
    height=71.0
)

canvas.create_text(
    45.0,
    131.0,
    anchor="nw",
    text="Black Adams",
    fill="#FFFFFF",
    font=("Inika", 24 * -1)
)

canvas.create_rectangle(
    230.0,
    25.0,
    1066.0,
    807.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
