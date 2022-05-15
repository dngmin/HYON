from tkinter import*

root = Tk()
root.title("GUI name")
root.geometry("640x480")

# btn1=Button(root,text="버튼1")
# btn2=Button(root,text="버튼2")

# #pack 쌓는 느낌  grid 배치

# btn1.grid(row=0,column=0)
# btn2.grid(row=1,column=1)

btn_insert=Button(root,text="insert",width=5,height=2)
btn_delete=Button(root,text="delete",width=5,height=2)
btn_pgup=Button(root,text="pgup",width=5,height=2)
btn_pgdn=Button(root,text="pgdn",width=5,height=2)

btn_insert.grid(row=0,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_delete.grid(row=0,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_pgup.grid(row=0,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_pgdn.grid(row=0,column=3,sticky=N+E+W+S,padx=3,pady=3)

btn_num=Button(root,text="num",width=5,height=2)
btn_dev=Button(root,text="/",width=5,height=2)
btn_mul=Button(root,text="*",width=5,height=2)
btn_hy=Button(root,text="-",width=5,height=2)

btn_num.grid(row=1,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_dev.grid(row=1,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_mul.grid(row=1,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_hy.grid(row=1,column=3,sticky=N+E+W+S,padx=3,pady=3)

btn_7=Button(root,text="7",width=5,height=2)
btn_8=Button(root,text="8",width=5,height=2)
btn_9=Button(root,text="9",width=5,height=2)
btn_pl=Button(root,text="-",width=5,height=2) #세로로 합쳐짐

btn_7.grid(row=2,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_8.grid(row=2,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_9.grid(row=2,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_pl.grid(row=2,column=3,rowspan=2,sticky=N+E+W+S,padx=3,pady=3) #row 2개를 합침

btn_4=Button(root,text="4",width=5,height=2)
btn_5=Button(root,text="5",width=5,height=2)
btn_6=Button(root,text="6",width=5,height=2)

btn_4.grid(row=3,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_5.grid(row=3,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_6.grid(row=3,column=2,sticky=N+E+W+S,padx=3,pady=3)

btn_1=Button(root,text="1",width=5,height=2)
btn_2=Button(root,text="2",width=5,height=2)
btn_3=Button(root,text="3",width=5,height=2)
btn_ent=Button(root,text="enter",width=5,height=2)

btn_1.grid(row=4,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_2.grid(row=4,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_3.grid(row=4,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_ent.grid(row=4,column=3,rowspan=2,sticky=N+E+W+S,padx=3,pady=3)

btn_0=Button(root,text="0",width=5,height=2)
btn_dot=Button(root,text=".",width=5,height=2)

btn_0.grid(row=5,column=0,columnspan=2,sticky=N+E+W+S,padx=3,pady=3) #column 3개를 합침
btn_dot.grid(row=5,column=2,sticky=N+E+W+S,padx=3,pady=3)

root.mainloop()