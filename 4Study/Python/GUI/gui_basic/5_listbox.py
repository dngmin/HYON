from tkinter import*

root = Tk()
root.title("GUI name")
root.geometry("640x480")

# 여러줄에 걸쳐서 목록을 관리하는 위젯

listbox=Listbox(root,selectmode="extended",height=0) #selectmode="singe"
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    #삭제
    # listbox.delete(END)  #맨 뒤 항목을 삭제
    # listbox.delete(0) #맨 앞 항목을 삭제

    #갯수 확인
    # print("in list",listbox.size())

    #항목 확인 (시작 idx, 끝idx)
    # print("1번째부터 3번째까지의 항목 : ",listbox.get(0,2))

    #선택된 항목 확인 (위치로 반환 (ex) (1,2,3) )
    print("선택된 항목 : ",listbox.curselection())

btn=Button(root,text="click",command=btncmd)
btn.pack()

root.mainloop()