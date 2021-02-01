"""
File: my drawing
Name:Willie Li
----------------------
The file shows the graphic combined by different objects.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    The character called Kirby,who is my favorite role in
    the game. The background is filled with many colors
    because I wanna express that life is good.
    """

    w = GWindow(title='Kirby is cute')
    background = GRect(800, 800)
    background.filled = True
    background.fill_color = 'lightgreen'
    w.add(background)

    background1 = GRect(800, 100)
    background1.filled = True
    background1.fill_color = 'orchid'
    background1.color ='orchid'
    w.add(background1)

    background2 = GRect(800, 100)
    background2.filled = True
    background2.fill_color = 'yellow'
    background2.color = 'yellow'
    w.add(background2,0,100)

    background3 = GRect(800, 100)
    background3.filled = True
    background3.fill_color = 'lightblue'
    background3.color = 'lightblue'
    w.add(background3, 0, 200)

    background4 = GRect(800, 100)
    background4.filled = True
    background4.fill_color = 'lightsalmon'
    background4.color = 'lightsalmon'
    w.add(background4, 0, 300)

    hand1 = GOval(66, 66, x=129, y=150)
    hand1.filled = True
    hand1.fill_color = 'pink'
    hand1.color = 'sienna'
    w.add(hand1)
    hand3 = GOval(66, 66, x=271, y=150)
    hand3.filled = True
    hand3.fill_color = 'pink'
    hand3.color = 'sienna'
    w.add(hand3)
    body = GOval(200, 200, x=130, y=160)
    body.filled = True
    body.fill_color = 'pink'
    body.color = 'sienna'
    w.add(body)
    r_eye = GOval(30, 70, x=190, y=200)
    r_eye.filled = True
    r_eye.fill_color = 'sienna'
    r_eye.color = 'sienna'
    w.add(r_eye)
    r_eye1 = GOval(20, 60, x=195, y=200)
    r_eye1.filled = True
    r_eye1.fill_color = 'skyblue'
    r_eye1.color = 'skyblue'
    w.add(r_eye1)
    r_eye2 = GOval(25, 50, x=192, y=200)
    r_eye2.filled = True
    r_eye2.fill_color = 'sienna'
    r_eye2.color = 'sienna'
    w.add(r_eye2)
    r_eye3 = GOval(20, 35, x=195, y=203)
    r_eye3.filled = True
    r_eye3.fill_color = 'white'
    r_eye3.color = 'white'
    w.add(r_eye3)

    l_eye = GOval(30, 70, x=250, y=200)
    l_eye.filled = True
    l_eye.fill_color = 'sienna'
    l_eye.color = 'sienna'
    w.add(l_eye)
    l_eye1 = GOval(20, 60, x=255, y=200)
    l_eye1.filled = True
    l_eye1.fill_color = 'skyblue'
    l_eye1.color = 'skyblue'
    w.add(l_eye1)
    l_eye2 = GOval(25, 50, x=252, y=200)
    l_eye2.filled = True
    l_eye2.fill_color = 'sienna'
    l_eye2.color = 'sienna'
    w.add(l_eye2)
    l_eye3 = GOval(20, 35, x=255, y=203)
    l_eye3.filled = True
    l_eye3.fill_color = 'white'
    l_eye3.color = 'white'
    w.add(l_eye3)

    mouth = GArc(40, 80, 30, 120)
    w.add(mouth, 215, 280)
    mouth1 = GArc(30,80,0,100)
    w.add(mouth1,199,275)
    mouth2 = GArc(40, 30, 80, 140)
    w.add(mouth2, 247, 273)

    cheek = GOval(40, 20, x=150, y=260)
    cheek.filled = True
    cheek.fill_color = 'hotpink'
    cheek.color = 'hotpink'
    w.add(cheek)
    cheek1 = GOval(40, 20, x=280, y=260)
    cheek1.filled = True
    cheek1.fill_color = 'hotpink'
    cheek1.color = 'hotpink'
    w.add(cheek1)

    feet = GOval(70,80,x=140,y=285)
    feet.filled =True
    feet.fill_color= 'red'
    feet.color = 'sienna'
    w.add(feet)
    feet1 = GOval(70, 80, x=250, y=285)
    feet1.filled = True
    feet1.fill_color = 'red'
    feet1.color = 'sienna'
    w.add(feet1)

    s1 = GLabel('Kirby x stanCode')
    s1.font = 'New Time Roman -40 -italic'
    s1.color = 'ivory'
    w.add(s1,90, 100)

    s2 = GLabel('S C')
    s2.font = '-80'
    s2.color = 'white'
    w.add(s2, 10, 290)

    s2 = GLabel('1 0 1')
    s2.font = '-80'
    s2.color = 'white'
    w.add(s2, 320, 290)


if __name__ == '__main__':
    main()
