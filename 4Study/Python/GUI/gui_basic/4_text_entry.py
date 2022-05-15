from tkinter import*

root = Tk()
root.title("GUI name")
root.geometry("640x480")

txt=Text(root,width=30,height=5)
txt.pack()

txt.insert(END,"글자를 입력하세요")



e=Entry(root,width=30)
e.pack()
e.insert(0,"한 줄만 입력하세요") #현재 값이 비어있으므로 ENd를 써도 동일

def btncmd():
    #내용 출력
    print(txt.get("1.0",END))  # 1: 첫번쨰 라인 0: 0번쨰 column
    print(e.get())

    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn=Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()