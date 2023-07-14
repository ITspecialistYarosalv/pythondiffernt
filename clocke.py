from tkinter import Label,Tk
import time

window = Tk()
window.title('Digital clock')
window.geometry("420x150")
window.resizable(1,1)


text_font = ('Boulder',68,'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(window,font=text_font,background=background,foreground=foreground,border=border_width)
label.grid(row=0,column=1)
def digital_clock():
    time_live = time.strftime('%H:%M:%S')
    label.config(text=time_live)
    label.after(200,digital_clock)

digital_clock()
window.mainloop()