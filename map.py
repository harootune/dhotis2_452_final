#Import Statements
from tkinter import *
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk
import json

#JSON
#creates a fun dictionary from the json file
with open('deckinfo.json', 'rt') as infile:
    deck_info = json.load(infile)

#Roots
#Creates, names, and titles root window
root = Tk()
root.title('Stacks Map')

#Switch
#Handles screen switching and calls icon rendering functions
def switch():
    val = deck_number.get()
    if val in deck_info['decks']:
        width = deck_info['decks'][val]['resize'][0]
        height = deck_info['decks'][val]['resize'][1]
        deck_image_temp = Image.open(Path(deck_info['decks'][val]['file']))
        deck_image_temp = deck_image_temp.resize((width, height), Image.ANTIALIAS)
        global deck_image
        deck_image = ImageTk.PhotoImage(deck_image_temp)

        display_1.delete('obj')
        display_1.create_image(width/2, height/2, anchor=CENTER, image=deck_image, tags='obj')

        info_2.delete(1.0, 'end')
        info_2.insert(1.0, 'Click stars for more info, arrows to switch between East and West decks, exits for exit info.')
        deck_text_title.set('')

        icons(val)
        exits(val)
        eastwest(val)

    else:
        info_2.delete(1.0, 'end')
        info_2.insert(1.0, 'Something went wrong.')

#this is a slight variation on the switch() function which allows for switching
#using tag_bind functions
def ew_switch(target):
    deck_number.set(target)
    switch()

#renders POI icons
def icons(val):
    if 'icons' in deck_info['decks'][val]:
        count = 0
        for icon in deck_info['decks'][val]['icons']:
            count += 1
            tag_name = 'icon'+str(count)
            display_1.create_image(int(icon['coordinates'][0]), int(icon['coordinates'][1]),
                                   image=icon_image, tags=(tag_name, 'obj'))
            display_1.tag_bind(tag_name, '<Button-1>', lambda x, icon=icon: textswitch(icon)) #I gotta buy dinner for Vel for this one

 #this and following line need to be relocated for more consistent performance


#renders emergency exits
def exits(val):
    if 'exits' in deck_info['decks'][val]:
        count = 0
        for exit in deck_info['decks'][val]['exits']:
            count += 1
            tag_name = 'exit'+str(count)
            display_1.create_image(int(exit['coordinates'][0]), int(exit['coordinates'][1]),
                                   image=exit_image, tags=(tag_name, 'obj'))
            display_1.tag_bind(tag_name, '<Button-1>', lambda x, exit=exit: textswitch(exit))

#renders east-west switches
def eastwest(val):
    if 'eastwest' in deck_info['decks'][val]:
        count = 0
        for eastwest in deck_info['decks'][val]['eastwest']:
            count += 1
            tag_name = 'eastwest'+str(count)
            display_1.create_image(int(eastwest['coordinates'][0]), int(eastwest['coordinates'][1]),
                                   image=eastwest_image, tags=(tag_name, 'obj'))
            display_1.tag_bind(tag_name, '<Button-1>', lambda x, target=eastwest['target']: ew_switch (target)) #bind to different function

#updates info boxes with relevant information
def textswitch(icon):
        info_2.delete(1.0, 'end')
        info_2.insert(1.0, icon['info'])
        deck_text_title.set(icon['name'])

#Images
#Creates an image object and global reference for POI icons
icon_image_temp = Image.open(Path('icons/star.png'))
icon_image_temp = icon_image_temp.resize((25, 25), Image.ANTIALIAS)
icon_image = ImageTk.PhotoImage(icon_image_temp)

exit_image_temp = Image.open(Path('icons/exit.png')) #temp
exit_image_temp = exit_image_temp.resize((25, 25), Image.ANTIALIAS)
exit_image = ImageTk.PhotoImage(exit_image_temp)

eastwest_image_temp = Image.open(Path('icons/eastwest.png')) #temp
eastwest_image_temp = eastwest_image_temp.resize((25, 25), Image.ANTIALIAS)
eastwest_image = ImageTk.PhotoImage(eastwest_image_temp)

#Variables
#inits some useful variables for later
deck_number = StringVar()
deck_number.set('5 East')

deck_text_title = StringVar()
deck_text_title.set('Intro')

#Widgets
#Creates widgets
#Frames
frame_1 = ttk.Frame(root, borderwidth=5, relief='groove')
dframe_1 = ttk.Frame(frame_1, borderwidth=3, relief='ridge')
dframe_2 = ttk.Frame(frame_1, borderwidth=3, relief='flat')
dframe_3 = ttk.Frame(frame_1, borderwidth=3, relief='ridge')


#Labels
label_1 = ttk.Label(dframe_1, text='Info:')
label_2 = ttk.Label(dframe_3,text='Deck Select')

info_1 = ttk.Label(dframe_1, textvariable=deck_text_title)
info_2 = Text(dframe_2, width=20, height=15)
info_2.insert(1.0, 'Select a deck number to begin.')

#Canvas
display_1 = Canvas(frame_1, borderwidth=5, relief='sunken', width=600, height=600)

#Dropdown
options_1 = ttk.Combobox(dframe_3, textvariable=deck_number, values=(
    'Basement West', '1 East', '2 East', '2 West', '3 East', '3.5 West', '4 East',
    '5 East', '5 West', '6 East', '7 East', '8 East', '9 East', '9.5 West'))

#Button
button_1 = ttk.Button(dframe_3, text='Go', command=switch)


#Grid
#grid placement information
frame_1.grid(column=0, row=0, sticky=N+S+E+W)
dframe_1.grid(column=0, row=0, sticky=N+S+E+W, rowspan=1)
dframe_2.grid(column=0, row=1, sticky=N+S+E+W, rowspan=2)
dframe_3.grid(column=0, row=3, sticky=N+S+E+W, rowspan=2)


label_1.grid(column=0, row=0, sticky=N+S+E+W, padx=5)
label_2.grid(column=0, row=0, sticky=S+W, padx=5, pady=12)

info_1.grid(column=0, row=1, sticky=N+S+E+W, padx=5)
info_2.grid(column=0, row=0, sticky=E+W)

options_1.grid(column=0, row=1, padx=5, pady=12)

button_1.grid(column=0, row=2, padx=5, pady=12)

display_1.grid(column=1, row=0, rowspan=5, sticky=N+S+E+W)

#Resizing
#configure resizing behavior
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame_1.columnconfigure((0, 1), weight=2)
frame_1.rowconfigure((0, 1, 2, 3, 4), weight=2)
dframe_1.columnconfigure(0, weight=3)
dframe_1.rowconfigure((0, 1), weight=3)
dframe_2.columnconfigure(0, weight=3)
dframe_2.rowconfigure((0), weight=3)
dframe_3.columnconfigure(0, weight=3)
dframe_3.rowconfigure((0, 1), weight=3)


#Mainloop
root.mainloop()
