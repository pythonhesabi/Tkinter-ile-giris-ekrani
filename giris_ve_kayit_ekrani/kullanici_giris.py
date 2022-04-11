import tkinter as tk
from tkinter_projeleri.giris_ve_kayit_ekrani import kayit_ol


def giris_yap():
    root = tk.Tk()
    root.title("Giris Yap Ekrani")
    root.geometry("300x300")
    root.grid()

    label1 = tk.Label(root,text="telefon no: ")
    label1.grid(row=0, column=1)

    text1 = tk.Text(root,width=15, height=1)
    text1.grid(row=0, column=2)

    buton1 = tk.Button(root,text="giriş yap", width=10, padx=10, command='clicked')
    buton1.grid(row=1, column=2)

    buton2 = tk.Button(root,text="kayıt Ol", bg="yellow", width=10, padx=10, command=kayit_ol.kayit_ol_func)
    buton2.grid(row=2, columns=3)
    root.mainloop()


giris_yap()
