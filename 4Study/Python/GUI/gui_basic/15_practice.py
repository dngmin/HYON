from tkinter import*
import os.path as path
from tkinter import messagebox

root=Tk()
root.title("無題-メモ帳")
root.geometry("800x600+500+200")
root.resizable(True,True)

menu=Menu(root)

#text box,scrollbar

scrollbar=Scrollbar(root)
scrollbar.pack(side="right",fill="y")

txt=Text(root,yscrollcommand=scrollbar.set)
txt.pack(fill="both",expand=True)
scrollbar.config(command=txt.yview)
root.config(menu=menu)

# ファイル
menu_file=Menu(menu,tearoff=0)

def op():
    if path.exists('new_file.txt'):
        root.title("new_file")
        nf_file=open("new_file.txt","r",encoding="utf8")
        txt.delete(0.0,END)
        txt.insert(0.0,nf_file.read())
        nf_file.close()
    else:
        messagebox.showerror("エラー","ファイルがありません。")
        
def sa():
    root.title("new_file")
    nf_file=open("new_file.txt","w",encoding="utf8")
    print(txt.get(0.0,END),file=nf_file)
    nf_file.close()
    

menu_file.add_command(label="開く",command=op)
menu_file.add_command(label="上書き保存",command=sa)
menu_file.add_separator()
menu_file.add_command(label="メモ帳の終了",command=root.quit)
menu.add_cascade(label="ファイル",menu=menu_file)


# etc
menu.add_cascade(label="編集")
menu.add_cascade(label="書式")
menu.add_cascade(label="表示")
menu.add_cascade(label="ヘルプ")





root.mainloop()