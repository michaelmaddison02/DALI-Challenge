#Guess Who is a two-player board game where players each guess the identity of the other's chosen character.
#Players: You and the computer
#Objective: Guess who the computer has randomly selected. Each round, you are able to narrow down potential identities by guessing attributes

import json             #json file reader
from Tile import tile   #tile class
import tkinter
from tkinter import *
import random           #used to randomize lists
from PIL import ImageTk, Image   #used for resizing images

#open json file, return JSON object as list of Dictionaries
data = json.load(open('DALI_Data.json'))

#store the data into tile classes, get each image
Tile_List = []
for datum in data:
    Tile_List.append(tile(datum))

#shuffle the tiles, we will use the first 30
random.shuffle(Tile_List)

#load graphics start screen
def load_start_screen(width, height):
    tile_width = width / 8
    tile_height = height / 3

    #for each character
    for i in range(24):
        # Create a photoimage object of the image in the path
        img = Tile_List[i].get_image(120, 200 - 20)
        tkinter_img = ImageTk.PhotoImage(img)

        label1 = tkinter.Label(image=tkinter_img)
        label1.image = tkinter_img

        # Position image
        rect_x = 160 * (i % 8) + 10
        rect_y = 240 * int(i / 8) + 10

        image_x = rect_x + 10
        image_y = rect_y + 10

        canvas.create_rectangle(rect_x, rect_y, rect_x + 140, rect_y + 220, outline="#0C0A3E", fill="#0C0A3E")
        label1.place(x=image_x, y=image_y)

        text_x = tile_width / 2 + 160 * (i % 8)  # centered below image
        text_y = image_y + 210  # sit below image

        canvas.create_text(text_x, image_y + 200, text=Tile_List[i].name.upper(), fill="white", font=('Helvetica 12 bold'))

def button_command():
    #split text, get which category the guess is (year, major) and the guess
    text = entry.get().split(" ")
    d_key = text[0]
    d_element = ""

    for i in range(1, len(text)):
        if i != len(text)-1:
            d_element += text[i] + " "
        else:
            d_element += text[i]

    # if computer's tile has the attribute, hide all that do not have the attribute
    if Tile_List[r].contains_element(d_key, d_element):
        for i in range(24):
            if Tile_List[i].does_not_contains_element(d_key, d_element):
                rect_x = 160 * (i % 8) + 10
                rect_y = 240 * int(i / 8) + 10
                canvas.create_rectangle(rect_x, rect_y, rect_x + 140, rect_y + 220, outline="red", fill="red")
                canvas.pack()

    # if computer's tile does not have the attribute, hide all that have attribute
    elif Tile_List[r].does_not_contains_element(d_key, d_element):
        for i in range(24):
            if Tile_List[i].contains_element(d_key, d_element):
                rect_x = 160 * (i % 8) + 10
                rect_y = 240 * int(i / 8) + 10
                canvas.create_rectangle(rect_x, rect_y, rect_x + 140, rect_y + 220, outline="red", fill="red")
                canvas.pack()

    entry.delete(0, END)

    #when player makes guess, they either win or lose
    if d_key == "name":

        print(d_element.lower())
        #if you guess correctly, highlight computer's player in green
        if Tile_List[r].name.lower() == d_element.lower():
            rect_x = 160 * (r % 8) + 10
            rect_y = 240 * int(r / 8) + 10
            canvas.create_rectangle(rect_x, rect_y, rect_x + 140, rect_y + 220, outline="green", fill="green")
            canvas.pack()
            entry.insert(0, "you win!!!")
        else:
            #if you guess incorrectly, highlight everything in red
            for i in range(24):
                rect_x = 160 * (i % 8) + 10
                rect_y = 240 * int(i / 8) + 10
                canvas.create_rectangle(rect_x, rect_y, rect_x + 140, rect_y + 220, outline="red", fill="red")
                canvas.pack()
                entry.insert(0, "you lose!!!")
        entry.config(state=DISABLED)

#create window
window = Tk()
window.geometry("1280x770")
window.minsize(1280, 770)
window.maxsize(1280, 770)
window['background']='#81A094'
window.title("Guess Who?")

#create canvas to draw rectangles
canvas = Canvas(window, height=720, width=1280, bg="#81A094", highlightthickness=0)
canvas.pack()

#load start screen
load_start_screen(1280, 720)

#select random character
r = random.randint(0, 23)

#create textbox
entry = Entry(window, width=100)
entry.place(x=10, y=730)

#create "enter" button
button = Button(window, text="ENTER", command=button_command)
button.pack()
button.place(x=10, y=720)

entry.pack()

window.mainloop()