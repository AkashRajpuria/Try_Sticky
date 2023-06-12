#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox


# In[2]:


# Mainwindow = Tk()
# Mainwindow.geometry('1350x700')
# Mainwindow.title("Sticky Notes")
# Mainwindow.mainloop()#to run the tkinter window for in finte loop


# In[3]:


def white_on_black():
    color_fg = "white"
    color_bg = "black"
    change_apperance(color_bg,color_fg)
    
def Black_on_Orange():
    color_fg = "black"
    color_bg = "orange"
    menubar['bg'] = "green"
    change_apperance(color_bg,color_fg)  
    
    
def change_apperance(color_bg,color_fg):
    txt['bg'] = color_bg
    txt['fg'] = color_fg
    
def change_color(Name,textcolor):
    txt.tag_configure(f"{Name}",foreground=textcolor)
    try:
        txt.tag_add(f"{Name}","sel.first","sel.last")
    except:
        pass
def Color_green():
    Name = "green_color"
    textcolor = "Green"
    change_color(Name,textcolor)
def Color_blue():
    Name = "blue_color"
    textcolor = "blue"
    change_color(Name,textcolor)
def set_text(text):
    Note_Title_Entry.delete(0,END)
    Note_Title_Entry.insert(0,text)
    return


# In[4]:


def create_notes():
    """
    This function will be evoked everytime, “Create a Note” button is clicked. This will help us create a new note.

    """
    notes_title = Note_Title_Entry.get()
    notes = txt.get("1.0", "end-1c")
        #Raise a prompt for missing values
    if  (len(notes_title)<=0) & (len(notes)<=1):
            messagebox.showerror(message = "Enter Details" )
    else:
        import csv   
        fields=[notes_title,notes]
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        messagebox.showinfo(message="Note added")
    update()


def delete_notes():

    notes_title = Note_Title_Entry.get()

    if (len(notes_title)<=0):  
            #Raise error for no inputs
            messagebox.showerror(message = "Enter Details:" )
            return
    else:
            dic = read_data_to_dict()
            del dic[notes_title]
            save_csv(dic)
#             print("dic saved",dic)
#             print("Calling --- update")
            
#             print("--Done update")
#Execute the query
            messagebox.showinfo(message="Note(s) Deleted")
    update()

    
def read_data_to_dict():
    import csv

    reader = csv.DictReader(open('data.csv'))
    result = {}

    for row in reader:
        result[row['title']] = row['text']
    return result
def save_csv(result):
    import pandas as pd

    df = pd.DataFrame.from_dict(data=result, orient='index').reset_index()
    df.columns=['title','text']
    df.to_csv('data.csv',index=False)


# In[5]:


import functools
try:
    from tkinter import *

    import tkinter as tk
except ImportError: 
    from Tkinter import *
    import Tkinter as tk#


# # # #

# In[7]:


menu_bg_color = "black"


Mainwindow = Tk()
Mainwindow.geometry('1350x700')
Mainwindow.title("Sticky Notes")
#################################################
menubar = Menu(Mainwindow,bg= menu_bg_color)
appear = Menu(menubar)
#The goal of this widget is to allow us to create all kinds of menus that can be used by our applications. 
menubar.add_cascade(label='appear',menu=appear)
#Creates a new hierarchical menu by associating a given menu to a parent menu
appear.add_command(label = "white on black",command = white_on_black)
appear.add_command(label="Black on Orange",command=Black_on_Orange)

Text_color = Menu(menubar)#The goal of this widget is to allow us to create all kinds of menus that can be used by our applications. 
menubar.add_cascade(label="Text Color",menu=Text_color)#Creates a new hierarchical menu by associating a given menu to a parent menu
Text_color.add_command(label="Blue",command=Color_blue)
Text_color.add_command(label="Green",command=Color_green)
##########################################################


##################################################
frame = Frame(Mainwindow)
frame.place(x=320, y=80, relwidth=0.7, relheight=0.8)
notestitle = Label(frame,text="Writing area",font=('arial',40,'bold'),bd=7,relief=GROOVE).pack()
scrool_y = Scrollbar(frame,orient=VERTICAL)
scrool_y.pack(side=RIGHT, fill=Y)
txt = Text(frame,yscrollcommand=scrool_y.set,width = 40, height=4, font=("Helvetica", 32))
txt.insert(
    END, "Welcome to Home made Notes")
txt.pack(fill=BOTH, expand=1)
scrool_y.config(command=txt.yview)

######################################################

# titles = Frame(Mainwindow)
# titles.place(x=0, y=80, width=300, relheight=0.88)
# scrool_y2 = Scrollbar(titles,orient=VERTICAL)
# scrool_y2.pack(side=RIGHT, fill=Y)
# #scrool_y2.config(command=titles.yview)

frame_container=Frame(Mainwindow)
canvas_container=Canvas(frame_container,width=300,height=560)
frame2=Frame(canvas_container)
myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
canvas_container.create_window((0,0),window=frame2,anchor='nw')


canvas_container.pack(side=LEFT)
myscrollbar.pack(side=RIGHT, fill = Y)

frame_container.place(x=0,y=120)


def func(name):
    print (name)
# mylist = ['item1','item2','item3','item4','item5','item6','item7','item8','item9']
# for item in mylist:
#     button = Button(frame2,text=item,command=functools.partial(func,item))
#     button.pack()


def notes(event):
    #from datetime import date
    #today = str(date.today())
    key = event.widget.cget('text')
    
    txt.delete("1.0", END)

    d=read_data_to_dict()
    
    set_text(key)
    #txt.insert(END,today)
    #print(today)
    txt.insert(END, d[key])
def update():
    frame_container=Frame(Mainwindow)
    canvas_container=Canvas(frame_container,width=300,height=560)
    frame2=Frame(canvas_container)
    myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0,0),window=frame2,anchor='nw')


    canvas_container.pack(side=LEFT)
    myscrollbar.pack(side=RIGHT, fill = Y)

    frame_container.place(x=0,y=120)

    d=read_data_to_dict()
    title = list(d.keys())

    for i in range(len(title)):
        b = Button(frame2, text=title[i], width=20, bd=7, font="arial 15 bold")
        b.pack()
        b.bind('<Button-1>', notes)
        
    frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                            #in this case "x=0 y=0 width=0 height=frame2height"
           
update()


frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                            #in this case "x=0 y=0 width=0 height=frame2height"
                              


Note_Title_Label=Label(Mainwindow,text="Note Title:",width=20, bd=7, font="arial 15 bold").place(x=340,y=30) #Label() method helps us create a widget which will display a text on our window
Note_Title_Entry=Entry(Mainwindow,width = 40, font=("Helvetica", 32))# Entry() function helps us create an entry field on the window
Note_Title_Entry.place(width=400,height=50,x =550,y=20)

Button(Mainwindow, text="Save",width=20, bd=7, font="arial 15 bold",command=create_notes,bg='pink').place(x=650, y=635) 
#S.grid(row=-1, column=2, padx=10, pady=5)

#Button(MainWindow, text="Edit Notes",command=edit_notes,bg='yellow').pack()
Button(Mainwindow, text="Delete Notes",width=20, bd=7, font="arial 15 bold",command=delete_notes,bg='yellow').place(x=950, y=635)
 




#

Mainwindow.config(menu=menubar)
Mainwindow.mainloop()#to run the tkinter window for in finte loop




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




