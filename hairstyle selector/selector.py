# python random generator to select a hairstyle for me each morning


import random

import pandas as pd
from graphics import * 

def build_graphic(win):
    heading = Text(Point(50, 90), "Our style for today is")
    heading.setTextColor("purple")
    heading.setStyle("bold")
    heading.setSize(20)
    heading.draw(win)
    return

def generate_style(styles):
    accessory = styles.at[random.randint(0,9), "accessories"]
    shape = styles.at[random.randint(0,9), "shapes"]
    extra = styles.at[random.randint(0,9), "extras"]
    return(accessory, shape, extra)

    # print("Today let's do a " + styles.at[shape, "shapes"] + " style with "+styles.at[accessory, "accessories"]+" and "+styles.at[extra, "extras"])


def populate_graphic(accessory, shape, extra, win):
    accessorytext = Text(Point(50, 80), "a "+shape+" style")
    shapetext = Text(Point(50, 75), "with "+accessory+" accessories")
    extratext = Text(Point(50, 70), "and "+extra+" embellishment")

    accessorytext.draw(win)
    shapetext.draw(win)
    extratext.draw(win)

def main():
    # load in the file  hairstyle selector\styles.csv
    styles = pd.read_csv("hairstyle selector/styles.csv")
    # build the graphic
    #Create a white window for weekly calendar
    win = GraphWin('hairstyle', 550, 550)
    win.setBackground('light pink')
    win.setCoords(0,0,100,100)
    build_graphic(win)
    accessory, shape, extra = generate_style(styles)
    populate_graphic(accessory, shape, extra, win)

    p = win.getMouse()
    # Close the window
    win.close()





if __name__ == "__main__":
    main()

