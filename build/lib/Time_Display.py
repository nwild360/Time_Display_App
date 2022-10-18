#usr/bin/env python

author = "Nick Wild"

from datetime import datetime
import pytz
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title("US Times")
GUI.configure(bg='#3750c8')

def get_time():
    get_hawaii = datetime.now(pytz.timezone('Pacific/Honolulu'))
    time_hawaii = get_hawaii.strftime("Hawaii: %I:%M %p\nStates:HI")

    get_us_alaska = datetime.now(pytz.timezone('US/Alaska'))
    time_us_alaska = get_us_alaska.strftime("\n\nAlaska: %I:%M %p\nStates:AK")

    get_us_pacific = datetime.now(pytz.timezone('America/Tijuana'))
    time_us_pacific = get_us_pacific.strftime("\n\nPacific: %I:%M %p\nStates:WA,OR,CA,NV")

    get_us_mountain = datetime.now(pytz.timezone('America/Chihuahua'))
    time_us_mountain = get_us_mountain.strftime("\n\nMountain: %I:%M %p\nStates:MT,ID,UT,AZ,WY,CO,NM")

    get_us_central = datetime.now(pytz.timezone('America/Mexico_City'))
    time_us_central = get_us_central.strftime("\n\nCentral: %I:%M %p\nStates:ND,SD,NE,KS,OK,TX,MN\nIA,MO,AR,LA,WI,IL,West KY\nWest TN,MS,AL")

    get_us_eastern = datetime.now(pytz.timezone('America/New_York'))
    time_us_eastern = get_us_eastern.strftime("\n\nEastern: %I:%M %p\nStates:MI,IN,East KY,East TN,GA,FL\nOH,WV,VA,NC,SC,PA,NY,VT\nNH,MA,RI,CT,NJ,DE,MD,DC")

    l1.config(text=time_hawaii+time_us_alaska+time_us_pacific+time_us_mountain+time_us_central+time_us_eastern)
    l1.after(1000,get_time)

my_font=('Verdana',10,'bold')

l1=Label(GUI,font=my_font, bg='#dee2f6')
l1.grid(row=1,column=1,padx=5,pady=10)

get_time()
GUI.mainloop()
