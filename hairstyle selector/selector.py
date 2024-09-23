# python random generator to select a hairstyle for me each morning


import random

import pandas as pd
from graphics import * 

def build_graphic():
    pass

def generate_style():
    # load in the file  
    styles = pd.read_csv("./styles.csv")

    accessory = random.randint(0,9)
    shape = random.randint(0,9)
    extra = random.randint(0,9)
    return(accessory, shape, extra)

    # print("Today let's do a " + styles.at[shape, "shapes"] + " style with "+styles.at[accessory, "accessories"]+" and "+styles.at[extra, "extras"])


def populate_graphic(accessory, shape, extra):
    pass

def main():
    # load in the file  
    styles = pd.read_csv("./styles.csv")
    # build the graphic
    build_graphic()
    accessory, shape, extra = generate_style()
    populate_graphic(accessory, shape, extra)





if __name__ == "__main__":
    main()

