from tkinter import *
import random
import math

def mulai():
    global angka_acak, maksimal_percobaan
    bawah = int(angka1_field.get())
    atas = int(angka2_field.get())
    angka_acak = random.randint(bawah, atas)
    maksimal_percobaan = round(math.log(atas - bawah + 1, 2))
    label5.config(text=f"Permainan dimulai! Anda memiliki {maksimal_percobaan} percobaan.")

def tebak():
    global maksimal_percobaan
    tebakkan = int(tebak_field.get())
    if tebakkan == angka_acak:
        label5.config(text=f"Selamat! Anda menebak angka dengan benar, angka-nya adalah {angka_acak}!")
    elif tebakkan < angka_acak:
        maksimal_percobaan -= 1
        label5.config(text=f"Tebakkan Anda Terlalu Kecil. Coba Lagi! Sisa Percobaan {maksimal_percobaan} lagi")
    elif tebakkan > angka_acak:
        maksimal_percobaan -= 1
        label5.config(text=f"Tebakkan Anda Terlalu Besar. Coba Lagi! Sisa Percobaan {maksimal_percobaan} lagi")
    if maksimal_percobaan == 0:
        label5.config(text=f"Anda kehabisan percobaan. Angka yang benar adalah {angka_acak}.")
        tebak_button["state"] = DISABLED

def reset():
    global angka_acak, maksimal_percobaan
    angka_acak = 0
    maksimal_percobaan = 0
    angka1_field.delete(0, END)
    angka2_field.delete(0, END)
    tebak_field.delete(0, END)
    label5.config(text="")
    tebak_button["state"] = NORMAL

root = Tk()
root.configure(background='light blue')
root.geometry("450x230")
root.title("Tebak Angka")

headlabel = Label(root, text='Selamat Datang di Permainan Tebak Angka!', fg='black', bg='light blue')

label1 = Label(root, text="Batas Bawah", fg='black', bg='light blue')
label2 = Label(root, text="Batas Atas", fg='black', bg='light blue')
label3 = Label(root, text="Tebak Angka-Nya!", fg='black', bg='light blue')
label4 = Label(root, text="Tebakkan:", fg='black', bg='light blue')
label5 = Label(root, text="", fg='black', bg='light blue')
label6 = Label(root, text="Dibuat oleh Kelompok 7 SG IMV", fg='black', bg='light blue')

headlabel.grid(row=0, column=1)
label1.grid(row=1, column=0, sticky="E")
label2.grid(row=2, column=0, sticky="E")
label3.grid(row=4, column=1)
label4.grid(row=5, column=0, sticky="E")
label5.grid(row=6, column=1)
label6.grid(row=9, column=1)

angka1_field = Entry(root)
angka2_field = Entry(root)
tebak_field = Entry(root)

angka1_field.grid(row=1, column=1, ipadx="100")
angka2_field.grid(row=2, column=1, ipadx="100")
tebak_field.grid(row=5, column=1, ipadx="100")

mulai_button = Button(root, text="Mulai", bg="white", fg="black", command=mulai)
tebak_button = Button(root, text="Tebak", bg="white", fg="black", command=tebak)
reset_button = Button(root, text="Reset", bg="white", fg="black", command=reset)

mulai_button.grid(row=3, column=1)
tebak_button.grid(row=7, column=1)
reset_button.grid(row=8, column=1)

root.mainloop()
