from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("950x550")
root.title("Signup Page")

En1 = Entry(root, width=30 ,relief='groove')
En1.place(x=700, y=240)

En2 = Entry(root, width=30, relief='groove')
En2.place(x=700, y=280)

En3 = Entry(root, width=30, relief='groove')
En3.place(x=700, y=320)

En4 = Entry(root, width=30, relief='groove')
En4.place(x=700, y=360)

En5 = Entry(root, width=30, relief='groove')
En5.place(x=700, y=400)

En6 = Entry(root, width=200, bg="blue", relief='groove')
En6.place(x=0, y=0, height=80)

En7 = Entry(root, width=20, relief='groove')
En7.place(x=550, y=25)

En8 = Entry(root, width=2, relief='groove')
En8.place(x=550, y=47)

En9 = Entry(root, width=20, relief='groove')
En9.place(x=710, y=25)

Bt1 = Button(root, text="Sign Up", bg="green", fg="white", width=25, height=1, font="Arial 9", relief='groove')
Bt1.place(x=700, y=440)

Bt2 = Button(root, text="Login", bg="#000080", fg="white", width=5, height=0, font="Arial 9 bold", relief='groove')
Bt2.place(x=850, y=20)

lb1= Label(root, text="First Name", font=("arial 9 bold"))
lb1.place(x=630, y=240)

lb2= Label(root, text="Last Name", font=("arial 9 bold"))
lb2.place(x=630, y=280)

lb3= Label(root, text="Your Email", font=("arial 9 bold"))
lb3.place(x=630, y=320)

lb4= Label(root, text="Re-enter Email", font=("arial 9 bold"))
lb4.place(x=607, y=360)

lb5= Label(root, text="New password", font=("arial 9 bold"))
lb5.place(x=605, y=400)

Lb6 = Label(root, text="Create A Page For Celebrity, Brand Or Business", font='Arial 9 bold')
Lb6.place(x=650, y=500)

Lb7 = Label(root, text="facebook",foreground= "white", bg="blue", font="QUART 25 bold ")
Lb7.place(x=1, y=20)

Lb8 = Label(root, text="", font="Arial 17")
Lb8.place(x=100, y=130)

Lb9 = Label(root, text="Facebook helps us to connect and share with", fg="black", font="Arial 15 bold" )
Lb9.place(x=20, y=150)

Lb10 = Label(root, text="the people in your life.", fg="black", font="Arial 15 bold" )
Lb10.place(x=20, y=190)

Lb11 = Label(root, text="Sign Up", fg="black", font="Arial 20 bold" )
Lb11.place(x=520, y=150)

Lb12 = Label(root, text="it's free, and always will be.", fg="black", font="Arial 15 bold" )
Lb12.place(x=520, y=190)

lb13= Label(root, text="Email", foreground= "white", bg="blue",font=("arial 10 bold"))
lb13.place(x=550, y=3)

lb14= Label(root, text="Keep me logged In", foreground= "white", bg="blue",font=("arial 10 bold"))
lb14.place(x=565, y=45)

lb15= Label(root, text="Password", foreground= "white", bg="blue",font=("arial 10 bold"))
lb15.place(x=710, y=3)

lb16= Label(root, text="Forgetten yor password ID", foreground= "white", bg="blue",font=("arial 10 bold"))
lb16.place(x=710, y=46)

Image = Image.open("fb1.png")
Photo = ImageTk.PhotoImage(Image)
ImgLabel = Label(root, image=Photo)
ImgLabel.place(x=20, y=235)

root.mainloop()