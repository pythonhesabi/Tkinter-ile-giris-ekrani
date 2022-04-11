import tkinter
import tkinter.ttk


def kayit_ol_func():
    root = tkinter.Tk()
    form = tkinter.ttk.Frame(root, padding=230)
    root.title("Kayit Ol Ekrani")
    form.grid()

    tkinter.ttk.Label(form, text="Ad").grid(column=0, row=0)
    tkinter.Text(form, width=15,height=1).grid(column=1, row=0)

    tkinter.ttk.Label(form, text="Soyad ").grid(column=0, row=3)
    tkinter.Text(form, width=15,height=1).grid(column=1, row=3)

    tkinter.ttk.Label(form, text="TEL NO ").grid(column=0, row=5)
    tkinter.Text(form, width=15,height=1).grid(column=1, row=5)

    tkinter.Button(form, text="Kayıt Ol", fg="white", bg="black").grid(column=6, row=6)
    root.mainloop()
