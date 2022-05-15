from tkinter import*
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI name")
root.geometry("640x480")

#like popup

def info():
    msgbox.showinfo("알림","정상적으로 작동중")
def warn():
    msgbox.showinfo("경고","경고함")
def error():
    msgbox.showerror("에러","에러에러")
def okcancel():
    msgbox.askokcancel("확인/취소","Yes or no")
def retrycancel():
    response=msgbox.askretrycancel("재시도/취소","re?")
    if response ==1: # retry
        print("Retry")
    elif response==0: #No
        print("No")
def yesno():
    msgbox.askyesno("yes no","yes no")
def yesnocancel():
    response=msgbox.askyesnocancel(title=None,message="yes no cancel")
    print(response)  # True, False, None
    if response ==1: # Yes
        print("Yes")
    elif response==0: # No
        print("No")
    else:
        print("Cancel")

Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="에러").pack()

Button(root,command=okcancel,text="확인 취소").pack()
Button(root,command=retrycancel,text="재시도").pack()
Button(root,command=yesno,text="yes no").pack()
Button(root,command=yesnocancel,text="yes no cancel").pack()

root.mainloop()