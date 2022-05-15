from tkinter import*

root = Tk()
root.title("GUI name")

lable1= Label(root,text="안녕하세요")
lable1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2=Label(root,image=photo)
label2.pack()

def change():
    lable1.config(text="잘가요")
    
    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root,image=photo,command=change)
btn.pack()

root.mainloop()