from tkinter import*
import tkinter.ttk as ttk
from time import*

root = Tk()
root.title("GUI name")
root.geometry("640x480")


# progessbar=ttk.Progressbar(root,maximum=100, mode="indeterminate")
progessbar=ttk.Progressbar(root,maximum=100, mode="determinate")
progessbar.start(10) #10ms 마다 움직임
progessbar.pack()

def btncmd():
    progessbar.stop() #작동 중지

Button(root,text="stop",command=btncmd).pack()

# p_var2=DoubleVar()
# progressbar2=ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
# progressbar2.pack()

# def btncmd2():
#     for i in range(1,101):
#         sleep(0.01)

#         p_var2.set(i)
#         progressbar2.update() #업데이트
#         print(p_var2.get())

# Button(root,text="start",command=btncmd2).pack()

root.mainloop()