# python random generator to select a movie from my watchlist


import random

import pandas as pd
from graphics import * 


def choose_option(win, title, options):
    heading = Text(Point(50, 90), title)
    heading.setStyle("bold")
    heading.setSize(14)
    heading.setTextColor("purple")
    heading.draw(win)

    buttons = []
    x1, x2 = 20, 80
    button_height = 8
    gap = 3
    y = 70

    for label, value in options:
        rect = Rectangle(Point(x1, y), Point(x2, y + button_height))
        rect.setFill("sky blue")
        rect.draw(win)

        text = Text(Point(50, y + button_height / 2), label)
        text.setSize(10)
        text.draw(win)

        buttons.append((rect, text, value))
        y -= (button_height + gap)

    while True:
        click = win.getMouse()
        for rect, text, value in buttons:
            p1 = rect.getP1()
            p2 = rect.getP2()
            if p1.getX() <= click.getX() <= p2.getX() and \
               p1.getY() <= click.getY() <= p2.getY():
                heading.undraw()
                for r, t, _ in buttons:
                    r.undraw()
                    t.undraw()
                return value

def make_selections(watchlist, win):
    runtime_options = [
    ("1 hr 30 min", 90),
    ("2 hr", 120),
    ("2 hr 30 min", 150),
    ("No preference", 0)
    ]

    runtime_spec = choose_option(
        win,
        "How long would you like the movie to be?",
        runtime_options
    )

    provider_options = [
        ("Netflix", "netflix"),
        ("Hulu", "hulu"),
        ("Prime", "prime"),
        ("No preference", "any")
    ]

    provider_spec = choose_option(
        win,
        "Do you have a provider preference?",
        provider_options
    )
    return runtime_spec, provider_spec


def generate_movie(watchlist, runtime_spec, provider_spec):

    if provider_spec != "any":
        # filter by provider
        watchlist = watchlist[watchlist['provider'] == provider_spec]
    if runtime_spec != 0:
        # filter by runtime
        watchlist = watchlist[watchlist['runtime'] <= (runtime_spec+10)]
    index_list = watchlist.index.tolist()
    #print(watchlist, index_list)

    if len(index_list) <= 0:
        title, runtime, provider, = 0,0,0
    else:
        title = watchlist.at[random.choice(index_list), 'title']
        runtime = watchlist.loc[watchlist['title']==title,'runtime'].iloc[0]
        provider = watchlist.loc[watchlist['title']==title, 'provider'].iloc[0]
    #print(title, runtime, provider)
    return title, runtime, provider


def populate_graphic(title, runtime, provider, win):
    if title == 0 and runtime == 0 and provider == 0:
        heading = Text(Point(50, 90), "no movie fits that criteria!")
        heading.setTextColor("purple")
        heading.setStyle("bold")
        heading.setSize(20)
        heading.draw(win)
    else: 
        heading = Text(Point(50, 90), "Our movie for today is")
        heading.setTextColor("purple")
        heading.setStyle("bold")
        heading.setSize(20)
        heading.draw(win)

        hours = round(runtime // 60)
        minutes = round(runtime % 60)
        titletext = Text(Point(50, 80), title)
        runtimetext = Text(Point(50, 75), str(hours)+" hours "+str(minutes)+" minutes")
        providertext = Text(Point(50, 70), provider)
        

        titletext.draw(win)
        runtimetext.draw(win)
        providertext.draw(win)
    

def main():
    # load in the file movie selector/watchlist.xlsx
    watchlist = pd.read_csv("watchlist.csv")
    # build the graphic
    #Create a window
    win = GraphWin('selection', 550, 550)
    win.setBackground('light pink')
    win.setCoords(0,0,100,100)

    runtime_spec, provider_spec = make_selections(watchlist, win)
    #print(runtime_spec, provider_spec)
    title, runtime, provider = generate_movie(watchlist, runtime_spec, provider_spec)
    populate_graphic(title, runtime, provider, win)
    
    
    # Close the window
    p = win.getMouse()
    if p:
        win.close()





if __name__ == "__main__":
    main()

