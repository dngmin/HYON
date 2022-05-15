from tkinter import*
from math import*
import numpy as np
import pandas as pd
from tkinter.font import Font
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox

#savepath
def save_path():
    folder_selected=filedialog.askdirectory()
    if folder_selected=='':
        return
    savepath_text.delete(0,END)
    savepath_text.insert(0,folder_selected)


#run
def run():
    try:
        # set

        X_Cd=(float(X_Cd_val.get()))
        Y_Cd=float(Y_Cd_val.get())
        X_area=float(X_area_val.get())
        Y_area=float(Y_area_val.get())
        launch_angle_deg=float(launch_angle_deg_val.get())
        wind_V=float(wind_V_val.get())
        wind_angle_yz_deg=float(wind_angle_yz_deg_val.get())
        Tem0_C=float(Tem0_C_val.get())
        P0_hpa=float(P0_hpa_val.get())
        h0=float(h0_val.get())
        mass_i=float(mass_i_val.get())
        mass_f=float(mass_f_val.get())
        t_com=float(t_com_val.get())
        t_act=float(t_act_val.get())
        T_com=float(T_com_val.get())
        T_total=float(T_total_val.get())
        k=float(k_val.get())



        # Fixed value

        L= 0.0065       
        M= 0.028966
        g0=9.80665
        T_com_s=T_com/t_com
        T_act_s=(T_total-T_com)/(t_act-t_com)
        launch_rad=launch_angle_deg*pi/180
        P0_pa=P0_hpa*100
        Tem0_K=Tem0_C+273.15
        wind_rad_yz = wind_angle_yz_deg *pi / 180
        wind_Vx = -wind_V * cos(wind_rad_yz) #進行方向がプラス
        wind_Vy = -wind_V * sin(wind_rad_yz)
        Δm_per_s=(mass_i-mass_f)/t_com



        # Initial Value

        m=mass_i
        y=0
        g=g0
        Tem_K=Tem0_K
        R=287
        h=h0
        atm= P0_pa 
        ρ = atm * M / R / Tem_K
        Vx=0
        Vy=0
        x=0
        y=0
        Pvx = 0.5 * ρ * pow((Vx+wind_Vx),2)
        Pvy = 0.5 * ρ * pow((Vy+wind_Vy),2)

        Dx = X_Cd * Pvx * X_area
        Dy = Y_Cd * Pvy * Y_area



        # Set list

        simulate_result={
            "t [s]" : [0],
            "x [m]" : [0],
            "y [m]" : [0],
            "vx" : [0],
            "vy" : [0]
        }



        # Chart

        for t in np.arange(0.0+k,100.0,k):

            if t<=t_com:
                T=T_com_s
            elif t_com<t<=t_act:
                T=T_act_s
            else:
                T=0
            
            if t<=t_com:
                m=mass_i-Δm_per_s*k
            else:
                m=mass_f

            Dx = X_Cd * Pvx * X_area
            Dy = Y_Cd * Pvy * Y_area

            Pvx = 0.5 * ρ * pow((Vx+wind_Vx),2)
            Pvy = 0.5 * ρ * pow((Vy+wind_Vy),2)
            h=h0+y
            atm= P0_pa * pow((1-(L*h)/Tem0_K),(g*M/R/L))
            g=pow((6371000),2)/pow((6371000+h),2)*g0
            Tem_K=Tem0_K-0.6*0.001*h
            ρ = atm * M / R / Tem_K
            R=atm*(22.4+Tem_K-273.15/273.15)

            #加速度
            ax= (T*cos(launch_rad)-Dx)/m
            if t>=t_act:
                ay=-9.8
            else:
                ay= (T*sin(launch_rad)-Dy)/m-g

            #速度
            Vx=Vx+ax*k
            Vy=Vy+ay*k

            #位置
            x=x+Vx*k
            y=y+Vy*k

            #配列化
            simulate_result["t [s]"].append(t)
            simulate_result["x [m]"].append(x)
            simulate_result["y [m]"].append(y)
            simulate_result["vx"].append(Vx)
            simulate_result["vy"].append(Vy)

            if simulate_result["y [m]"][-1]<simulate_result["y [m]"][-2]:
                break

        data=pd.DataFrame(simulate_result)
        data.to_csv("{}/simulate_result_data.csv".format(savepath_text.get()),encoding='utf-8-sig',index=False)

        msgbox.showwarning(title="clear",message="!!!")
    except (ValueError,ZeroDivisionError):
        msgbox.showerror(title="Erorr!",message="Something typing error!")
    except PermissionError:
        msgbox.showinfo(title="Error!",message="Where is the savepath?")


# history
def show_history():
    history=Tk()
    history.title("History")
    history.geometry("480x180+400+350")
    history.resizable(False,False)

    history_Text=Text(history)
    history_Text.pack(expand=True)

    hstry=open("C:\\Users\\h\\OneDrive\\바탕 화면\\PythonWorkspace\\hyon\\simulator\\シミュレーター沿革.txt","r",encoding='utf-8')

    history_Text.insert(END,"{}".format(hstry.read()))
    hstry.close()

    history_Text.configure(state=DISABLED,font=("Kristen ITC",13,"bold"))


    history.mainloop()


# instructions
def show_instructions():
    instructions=Tk()
    instructions.title("Instruction")
    instructions.geometry("205x100+400+350")
    instructions.resizable(False,False)

    instructions_Text=Text(instructions)
    instructions_Text.pack(expand=True)

    instrction=open("C:\\Users\\h\\OneDrive\\바탕 화면\\PythonWorkspace\\hyon\\simulator\\シミュレーター説明書.txt","r",encoding='utf-8')

    instructions_Text.insert(END,"{}".format(instrction.read()))
    instrction.close()

    instructions_Text.configure(state=DISABLED,font=("Kristen ITC",13,"bold"))

    instructions.mainloop()


#gui

# gui basic________________________________________________________________________________
simul=Tk()
simul.title("Rocket Simulator 0.4")
simul.geometry("750x520+300+300")
simul.resizable(False,False)


# Function________________________________________________________________________________








# font________________________________________________________________________________
Maintitle_font=Font(family="Kristen ITC",size=25,weight="bold")
# input_text_font=Font(family="Lucida Grande",size=10,weight="bold")


# Maintitle________________________________________________________________________________
Maintitle=Label(text="Roccket Simulator",font=Maintitle_font)
Maintitle.pack(pady=5)


# Input________________________________________________________________________________
input_frame=LabelFrame(simul,text="Input value")
input_frame.pack(pady=5)


# Input label
input_text_frame=Frame(input_frame)
input_text_frame.pack(side="left",padx=10)



X_Cd_text=Label(input_text_frame,text="X Cd [-]")
Y_Cd_text=Label(input_text_frame,text="Y Cd [-]")
X_area_text=Label(input_text_frame,text="X area [m^2]")
Y_area_text=Label(input_text_frame,text="Y area [m^2]")
launch_angle_deg_text=Label(input_text_frame,text="Launch angle [deg]")
wind_V_text=Label(input_text_frame,text="Wind speed [m/s]")
wind_angle_yz_deg_text=Label(input_text_frame,text="Wind angle (xy) [deg]")
Tem0_C_text=Label(input_text_frame,text="Surface temperature [℃]")
P0_hpa_text=Label(input_text_frame,text="See level pressure [hpa]")
h0_text=Label(input_text_frame,text="Altitude [m]")
mass_i_text=Label(input_text_frame,text="Initial mass [kg]")
mass_f_text=Label(input_text_frame,text="Final mass [kg]")
t_com_text=Label(input_text_frame,text="Combustion time [s]")
t_act_text=Label(input_text_frame,text="Actuation time [s]")
T_com_text=Label(input_text_frame,text="Combustion Thrust [N]")
T_total_text=Label(input_text_frame,text="Total Thrust [N]")
k_text=Label(input_text_frame,text="Time step")


X_Cd_text.pack()
Y_Cd_text.pack()
X_area_text.pack()
Y_area_text.pack()
launch_angle_deg_text.pack()
wind_V_text.pack()
wind_angle_yz_deg_text.pack()
Tem0_C_text.pack()
P0_hpa_text.pack()
h0_text.pack()
mass_i_text.pack()
mass_f_text.pack()
t_com_text.pack()
t_act_text.pack()
T_com_text.pack()
T_total_text.pack()
k_text.pack()

# Input value
input_value_frame=Frame(input_frame)
input_value_frame.pack(side="right",padx=10)



X_Cd_val=Entry(input_value_frame,width=30)
Y_Cd_val=Entry(input_value_frame,width=30)
X_area_val=Entry(input_value_frame,width=30)
Y_area_val=Entry(input_value_frame,width=30)
launch_angle_deg_val=Entry(input_value_frame,width=30)
wind_V_val=Entry(input_value_frame,width=30)
wind_angle_yz_deg_val=Entry(input_value_frame,width=30)
Tem0_C_val=Entry(input_value_frame,width=30)
P0_hpa_val=Entry(input_value_frame,width=30)
h0_val=Entry(input_value_frame,width=30)
mass_i_val=Entry(input_value_frame,width=30)
mass_f_val=Entry(input_value_frame,width=30)
t_com_val=Entry(input_value_frame,width=30)
t_act_val=Entry(input_value_frame,width=30)
T_com_val=Entry(input_value_frame,width=30)
T_total_val=Entry(input_value_frame,width=30)
k_val=Entry(input_value_frame,width=30)



X_Cd_val.pack(pady=1)
Y_Cd_val.pack(pady=1)
X_area_val.pack(pady=1)
Y_area_val.pack(pady=1)
launch_angle_deg_val.pack(pady=1)
wind_V_val.pack(pady=1)
wind_angle_yz_deg_val.pack(pady=1)
Tem0_C_val.pack(pady=1)
P0_hpa_val.pack(pady=1)
h0_val.pack(pady=1)
mass_i_val.pack(pady=1)
mass_f_val.pack(pady=1)
t_com_val.pack(pady=1)
t_act_val.pack(pady=1)
T_com_val.pack(pady=1)
T_total_val.pack(pady=1)
k_val.pack(pady=1)


# Save path________________________________________________________________________________
savepath_frame=LabelFrame(simul,text="save path")
savepath_frame.pack(ipady=3)

savepath_text=Entry(savepath_frame,width=50)
savepath_button=Button(savepath_frame,text="名前変えな",command=save_path)

savepath_text.pack(side="left",padx=3)
savepath_button.pack(side="right",padx=3)


# Menu________________________________________________________________________________
menu=Menu(simul)

menu_Main=Menu(menu,tearoff=0)
menu_Main.add_command(label="History",command=show_history)
menu_Main.add_command(label="Instructions",command=show_instructions)
menu.add_cascade(label="Menu",menu=menu_Main)

simul.config(menu=menu)


# Run botton________________________________________________________________________________
aa=Button(simul,text="run",command=run)
aa.pack()


#________________________________________________________________________________
simul.mainloop()