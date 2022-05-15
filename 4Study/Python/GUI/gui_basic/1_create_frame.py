from tkinter import*

root = Tk()
root.title("GUI name")
root.geometry("640x480") #가로x세로
# root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False,False) # x,y 값 변경불가 (창크기)

root.mainloop()