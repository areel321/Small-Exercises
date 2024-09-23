# python random generator to select a hairstyle for me each morning


import random

import pandas as pd
from graphics import * 

def build_graphic(win):
    pass

def generate_style():
    accessory = random.randint(0,9)
    shape = random.randint(0,9)
    extra = random.randint(0,9)
    return(accessory, shape, extra)

    # print("Today let's do a " + styles.at[shape, "shapes"] + " style with "+styles.at[accessory, "accessories"]+" and "+styles.at[extra, "extras"])


def populate_graphic(accessory, shape, extra):
    pass

def main():
    # load in the file  
    styles = pd.read_csv("../styles.csv")
    # build the graphic
    #Create a white window for weekly calendar
    win = GraphWin('hairstyle', 550, 550)
    win.setBackground('light pink')
    win.setCoords(-100,-100,100,100)
    build_graphic(win)
    accessory, shape, extra = generate_style()
    populate_graphic(accessory, shape, extra)





if __name__ == "__main__":
    main()

