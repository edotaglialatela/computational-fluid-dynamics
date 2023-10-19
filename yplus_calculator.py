# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:22:43 2023
Computation of y+ based on flat-plate BL theory
@author: felice edoardo taglialatela
"""

import tkinter
from tkinter import messagebox
import math
def enter_data():
    uinf = float(uinf_entry.get())
    yplus = float(yplus_entry.get())
    rho = float(rho_entry.get())
    mi = float(mi_entry.get())
    length = float(length_entry.get())
    reynolds = (rho*uinf*length)/(mi)
    reynolds_s = "{:.2e}".format(reynolds)
    
    if reynolds > 5e5 and reynolds < 1e7: #eqn 21.12 in "Boundary Layer Theory", Schlichting
        Cf = 0.0592*(reynolds**(-0.2))
        tau_wall = (Cf*rho*(uinf**2))/(2)
        u_tau = math.sqrt(tau_wall/rho)
        deltas = (yplus*mi)/(u_tau*rho)
        deltas_s = "{:.2e}".format(deltas)
        tkinter.messagebox.showinfo(title="y+ calculator", message="Reynolds number=" + str(reynolds_s) + "\n Wall spacing=" + str(deltas_s) + "m")
    elif reynolds > 1e7 and reynolds < 1e9: #eqn 21.16 footnote in "Boundary Layer Theory", Schlichting
        Cf = (2*math.log(reynolds)-0.65)**(-2.3)
        tau_wall = (Cf*rho*(uinf**2))/(2)
        u_tau = math.sqrt(tau_wall/rho)
        deltas = (yplus*mi)/(u_tau*rho)
        deltas_s = "{:.2e}".format(deltas)
        tkinter.messagebox.showinfo(title="y+ calculator", message="Reynolds number=" + str(reynolds_s) + "\n Wall spacing=" + str(deltas_s) + "m")
    else:
        tkinter.messagebox.showwarning(title= "Error",message= "Reynolds outside of the correlation range.")
    
    
window = tkinter.Tk()
window.title("y+ calculator")

frame = tkinter.Frame(window)
frame.pack()

infoframe = tkinter.LabelFrame(frame, text="Informations")
infoframe.grid(row=0, column=0, sticky="news", padx=20, pady=8)
first_name_label = tkinter.Label(infoframe, text="y+ calculator based on flat-plate boundary layer theory, by Felice Edoardo Taglialatela")
first_name_label.grid(row=0, column=0)

dataentry = tkinter.LabelFrame(frame, text="Data entry")
dataentry.grid(row=1, column=0, sticky="ns", padx= 20, pady=8)
uinf_label = tkinter.Label(dataentry, text="Freestream velocity, U∞ [m/s]")
uinf_label.grid(row=2, column=0)
uinf_entry = tkinter.Entry(dataentry)
uinf_entry.insert(0, "1.0")
uinf_entry.grid(row=2, column=1)
yplus_label = tkinter.Label(dataentry, text="Desidred y+, y+")
yplus_label.grid(row=3, column=0)
yplus_entry = tkinter.Entry(dataentry)
yplus_entry.insert(0, "1.0")
yplus_entry.grid(row=3, column=1)
rho_label = tkinter.Label(dataentry, text="Freestream density, ρ [kg/m^3]")
rho_label.grid(row=4, column=0)
rho_entry = tkinter.Entry(dataentry)
rho_entry.insert(0, "1.225")
rho_entry.grid(row=4, column=1)
mi_label = tkinter.Label(dataentry, text="Dynamic viscosity, μ [kg/m s]")
mi_label.grid(row=6, column=0)
mi_entry = tkinter.Entry(dataentry)
mi_entry.insert(0, "0.000017894")
mi_entry.grid(row=6, column=1)
length_label = tkinter.Label(dataentry, text="Reference length, L [m]")
length_label.grid(row=7, column=0)
length_entry = tkinter.Entry(dataentry)
length_entry.insert(0, "1.0")
length_entry.grid(row=7, column=1)

button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=2, column=0, pady=8)


window.mainloop()
