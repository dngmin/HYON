from tkinter import*
import tkinter.ttk as ttk
root = Tk()
root.title("GUI name")
root.geometry("640x480")


value=[str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root,height=5,values=value)
combobox.pack()
combobox.set("day") #최초 제목 설정

readonly_combobox = ttk.Combobox(root,height=10,values=value,state="readonly")
readonly_combobox.pack()
readonly_combobox.current(0)  #0번째 인덱스 값 선택


def btncmd():
    c=combobox.get()
    # print(combobox.get())
    print(c)
    print(readonly_combobox.get())

Button(root,text="click",command=btncmd).pack()

root.mainloop()