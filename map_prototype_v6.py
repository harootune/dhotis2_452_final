#Import Statements
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json

#JSON
#creates a fun dictionary from the json file
with open("deckinfo.json", "rt") as infile:
    deck_info = json.load(infile)

#Roots
#Creates, names, and titles root window
root = Tk()
root.title('Map v0.5')

#Switch
#Handles screen switching and calls icons()
def switch():
    val = str(deck_number.get())
    if val in deck_info["decks"]:
        width = deck_info["decks"][val]["resize"][0]
        height = deck_info["decks"][val]["resize"][1]
        deck_image_temp = Image.open(deck_info["decks"][val]["file"])
        deck_image_temp = deck_image_temp.resize((width, height), Image.ANTIALIAS)
        global deck_image
        deck_image = ImageTk.PhotoImage(deck_image_temp)

        display_1.delete('obj')
        display_1.create_image(width/2, height/2, anchor=CENTER, image=deck_image, tags='obj')

        icons(val)

    else:
        info_2.delete(1.0, 'end')
        info_2.insert(1.0, "Something went wrong.")

#icons
def icons(val):
    if "icons" in deck_info["decks"][val]:
        count = 0
        for icon in deck_info["decks"][val]["icons"]:
            count += 1
            tag_name = "icon"+str(count)
            display_1.create_image(int(icon["coordinates"][0]), int(icon["coordinates"][1]),
                                   image=icon_image, tags=(tag_name, 'obj'))


            display_1.tag_bind(tag_name, '<Button-1>', lambda x, icon=icon: textswitch(icon)) #I gotta buy dinner for Vel for this one
            info_2.delete(1.0, 'end')
            info_2.insert(1.0, "Click stars for more info.")
            deck_text_title.set("")
    else:
        pass

def textswitch(icon):
        info_2.delete(1.0, 'end')
        info_2.insert(1.0, icon["info"])
        deck_text_title.set(icon["name"])

#Images
#Creates an image object and global reference for POI icons
icon_image_temp = Image.open("icons/star.png")
icon_image_temp = icon_image_temp.resize((25, 25), Image.ANTIALIAS)
icon_image = ImageTk.PhotoImage(icon_image_temp)

#Variables
#inits some useful variables for later (text and float)
deck_number = DoubleVar()
deck_number.set(5.0)

deck_text_title = StringVar()
deck_text_title.set("Intro")

#Widgets
#Creates widgets
#Frames
frame_1 = ttk.Frame(root, borderwidth=5, relief='groove')
dframe_1 = ttk.Frame(frame_1, borderwidth=3, relief="ridge", padding=0)
dframe_2 = ttk.Frame(frame_1, borderwidth=3, relief='ridge', padding=0)
dframe_3 = ttk.Frame(frame_1, borderwidth=3, relief='ridge', padding=0)


#Labels
label_1 = ttk.Label(dframe_1, text="Info")
label_2 = ttk.Label(dframe_3,text="Deck Select")

info_1 = ttk.Label(dframe_2, textvariable=deck_text_title)
info_2 = Text(dframe_2, width=20, height=15)
info_2.insert(1.0, "Select a deck number to begin.")

#Canvas
display_1 = Canvas(frame_1, borderwidth=5, relief='sunken', width=500, height=800)

#Dropdown
options_1 = ttk.Combobox(dframe_3, textvariable=deck_number, values=(
    -1.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 9.5))

#Button
button_1 = ttk.Button(dframe_3, text='Go', command=switch)


#Grid
#grid placement information
frame_1.grid(column=0, row=0, sticky=N+S+E+W)
dframe_1.grid(column=0, row=0, sticky=N+S+E+W, rowspan=1)
dframe_2.grid(column=0, row=1, sticky=N+S+E+W, rowspan=2)
dframe_3.grid(column=0, row=3, sticky=N+S+E+W, rowspan=3)

label_1.grid(column=0, row=0, sticky=S+W)
label_2.grid(column=0, row=0, sticky=S+W)

info_1.grid(column=0, row=0, sticky=S+W)
info_2.grid(column=0, row=1, sticky=E+W)

options_1.grid(column=0, row=1)

button_1.grid(column=0, row=2)

display_1.grid(column=1, row=0, rowspan=6, sticky=N+S+E+W)

#Resizing
#configure resizing behavior
'''
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame_1.columnconfigure(0, weight=3)
frame_1.columnconfigure(1, weight=2)
frame_1.rowconfigure(0, weight=2)
frame_1.rowconfigure(1, weight=2)
'''

#Mainloop
root.mainloop()
