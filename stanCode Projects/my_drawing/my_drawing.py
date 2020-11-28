"""
File: my_drawing
Name: Charlie Liu
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


# globe variable
window = GWindow(width=600, height=800, title='We are coming in.')


def main():
    """
    the idea is use the slogan in dora-av-men and the poster in the newest movie of doraemon to generate my picture.
    """
    sun()
    doraemon()
    nobita()
    wall()
    dinosaur()
    slogan()


def dinosaur():
    dinosaur_img = GOval(250, 400, x=25, y=540)
    dinosaur_img.filled = True
    dinosaur_img.fill_color = 'green'
    dinosaur_img.color = 'green'
    window.add(dinosaur_img)
    dinosaur_head_img = GOval(230, 300, x=100, y=600)
    dinosaur_head_img.filled = True
    dinosaur_head_img.fill_color = 'green'
    dinosaur_head_img.color = 'green'
    window.add(dinosaur_head_img)
    dinosaur_eye_img = GOval(30, 50, x=200, y=585)
    dinosaur_eye_img.filled = True
    dinosaur_eye_img.fill_color = 'lightgreen'
    dinosaur_eye_img.color = 'lightgreen'
    window.add(dinosaur_eye_img)
    dinosaur_eye1_img = GOval(15, 15, x=212, y=590)
    dinosaur_eye1_img.filled = True
    dinosaur_eye1_img.fill_color = 'black'
    dinosaur_eye1_img.color = 'black'
    window.add(dinosaur_eye1_img)
    dinosaur_eye1_img = GOval(5, 5, x=222, y=590)
    dinosaur_eye1_img.filled = True
    dinosaur_eye1_img.fill_color = 'white'
    dinosaur_eye1_img.color = 'black'
    window.add(dinosaur_eye1_img)


def slogan():
    label = GLabel('討', x=450, y=680)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('厭', x=450, y=730)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('死', x=500, y=700)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('相', x=500, y=750)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('嚇', x=550, y=430)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('到', x=550, y=480)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('人', x=550, y=530)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('家', x=550, y=580)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('了', x=550, y=630)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('‧', x=550, y=680)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('‧', x=550, y=730)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('‧', x=550, y=780)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('我', x=100, y=100)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('們', x=100, y=150)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('進', x=100, y=200)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('來', x=100, y=250)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('囉', x=100, y=300)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('‧', x=100, y=350)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('‧', x=100, y=400)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)
    label = GLabel('‧', x=100, y=450)
    label.font = 'courier-20'
    label.color = 'white'
    window.add(label)


def wall():
    wall_left = picture_wall()
    window.add(wall_left)
    wall_right = picture_wall1()
    window.add(wall_right)
    wall_right = picture_wall2()
    window.add(wall_right)


def picture_wall2():
    wall1 = GPolygon()
    wall1.add_vertex((300, 0))
    wall1.add_vertex((350, 75))
    wall1.add_vertex((440, 100))
    wall1.add_vertex((410, 180))
    wall1.add_vertex((440, 220))
    wall1.add_vertex((460, 280))
    wall1.add_vertex((470, 340))
    wall1.add_vertex((463, 400))
    wall1.add_vertex((473, 430))
    wall1.add_vertex((453, 470))
    wall1.add_vertex((432, 520))
    wall1.add_vertex((420, 550))
    wall1.add_vertex((310, 635))
    wall1.add_vertex((335, 635))
    wall1.add_vertex((443, 550))
    wall1.add_vertex((455, 520))
    wall1.add_vertex((473, 470))
    wall1.add_vertex((495, 430))
    wall1.add_vertex((482, 400))
    wall1.add_vertex((492, 340))
    wall1.add_vertex((480, 280))
    wall1.add_vertex((464, 220))
    wall1.add_vertex((435, 180))
    wall1.add_vertex((450, 100))
    wall1.add_vertex((375, 75))
    wall1.add_vertex((300, 0))
    wall1.filled = True
    wall1.fill_color = 'gray'
    wall1.color = 'gray'
    return wall1


def picture_wall1():
    wall1 = GPolygon()
    wall1.add_vertex((600, 0))
    wall1.add_vertex((300, 0))
    wall1.add_vertex((350, 75))
    wall1.add_vertex((440, 100))
    wall1.add_vertex((410, 180))
    wall1.add_vertex((440, 220))
    wall1.add_vertex((460, 280))
    wall1.add_vertex((470, 340))
    wall1.add_vertex((463, 400))
    wall1.add_vertex((473, 430))
    wall1.add_vertex((453, 470))
    wall1.add_vertex((432, 520))
    wall1.add_vertex((420, 550))
    wall1.add_vertex((310, 635))
    wall1.add_vertex((300, 900))
    wall1.add_vertex((600, 900))
    wall1.filled = True
    wall1.fill_color = 'darkgrey'
    wall1.color = 'darkgrey'
    return wall1


def picture_wall():
    wall1 = GPolygon()
    wall1.add_vertex((0, 0))
    wall1.add_vertex((300, 0))
    wall1.add_vertex((250, 75))
    wall1.add_vertex((180, 100))
    wall1.add_vertex((160, 180))
    wall1.add_vertex((170, 220))
    wall1.add_vertex((140, 280))
    wall1.add_vertex((230, 340))
    wall1.add_vertex((220, 400))
    wall1.add_vertex((200, 440))
    wall1.add_vertex((200, 500))
    wall1.add_vertex((220, 550))
    wall1.add_vertex((310, 635))
    wall1.add_vertex((300, 900))
    wall1.add_vertex((0, 900))
    wall1.filled = True
    wall1.fill_color = 'darkgrey'
    wall1.color = 'grey'
    return wall1


def sun():
    sun_feel = sun_color()
    window.add(sun_feel)


def sun_color():
    sun = GRect(600, 900, x=0, y=0)
    sun.filled = True
    sun.fill_color = 'lightyellow'
    sun.color = 'lightyellow'
    return sun


def nobita():
    body = nobita_body()
    window.add(body)
    face = nobita_face()
    window.add(face)
    hair = nobita_hair()
    window.add(hair)
    hair1 = nobita_hair1()
    window.add(hair1)
    eye1 = nobita_eye1()
    window.add(eye1)
    eye2 = nobita_eye2()
    window.add(eye2)
    eye3 = nobita_eye3()
    window.add(eye3)
    eye4 = nobita_eye4()
    window.add(eye4)
    eye5 = nobita_eye5()
    window.add(eye5)
    eye6 = nobita_eye6()
    window.add(eye6)
    glass = nobita_glass()
    window.add(glass)
    nose = nobita_nose()
    window.add(nose)
    mouth = nobita_mouth()
    window.add(mouth)
    hand = nobita_hand()
    window.add(hand)
    hand_cloth = nobita_handcloth()
    window.add(hand_cloth)


def nobita_hand():
    hand = GPolygon()
    hand.add_vertex((200, 475))
    hand.add_vertex((310, 555))
    hand.add_vertex((310, 635))
    hand.add_vertex((200, 555))
    hand.filled = True
    hand.fill_color = 'antiquewhite'
    hand.color = 'antiquewhite'
    return hand


def nobita_handcloth():
    hand_cloth = GPolygon()
    hand_cloth.add_vertex((310, 555))
    hand_cloth.add_vertex((385, 505))
    hand_cloth.add_vertex((385, 585))
    hand_cloth.add_vertex((310, 635))
    hand_cloth.filled = True
    hand_cloth.fill_color = 'yellow'
    hand_cloth.color = 'yellow'
    return hand_cloth


def nobita_body():
    body = GOval(200, 700, x=315, y=480)
    body.filled = True
    body.fill_color = 'yellow'
    body.color = 'yellow'
    return body


def nobita_mouth():
    mouth = GOval(50, 10, x=385, y=465)
    mouth.filled = True
    mouth.fill_color = 'red'
    mouth.color = 'black'
    return mouth


def nobita_nose():
    arc = GArc(15, 15, 45, 270, x=395, y=415)
    arc.filled = False
    arc.fill_color = 'antiquewhite'
    arc.color = 'black'
    return arc


def nobita_glass():
    glass = GLine(480, 390, 498, 390)
    return glass


def nobita_eye5():
    eye_5 = GOval(5, 5, x=392, y=385)
    eye_5.filled = True
    eye_5.fill_color = 'ivory'
    eye_5.color = 'black'
    return eye_5


def nobita_eye6():
    eye_6 = GOval(5, 5, x=412, y=385)
    eye_6.filled = True
    eye_6.fill_color = 'ivory'
    eye_6.color = 'black'
    return eye_6


def nobita_eye4():
    eye_4 = GOval(10, 20, x=390, y=385)
    eye_4.filled = True
    eye_4.fill_color = 'black'
    eye_4.color = 'black'
    return eye_4


def nobita_eye3():
    eye_3 = GOval(10, 20, x=410, y=385)
    eye_3.filled = True
    eye_3.fill_color = 'black'
    eye_3.color = 'black'
    return eye_3


def nobita_eye2():
    eye_2 = GOval(75, 80, x=405, y=350)
    eye_2.filled = True
    eye_2.fill_color = 'whitesmoke'
    eye_2.color = 'black'
    return eye_2


def nobita_eye1():
    eye_1 = GOval(75, 80, x=330, y=350)
    eye_1.filled = True
    eye_1.fill_color = 'whitesmoke'
    eye_1.color = 'black'
    return eye_1


def nobita_hair1():
    arc = GArc(150, 180, 0, 180, x=345, y=310)
    arc.filled = True
    arc.fill_color = 'antiquewhite'
    arc.color = 'antiquewhite'
    return arc


def nobita_face():
    face = GOval(180, 210, x=323, y=300)
    face.filled = True
    face.fill_color = 'antiquewhite'
    face.color = 'black'
    return face


def nobita_hair():
    arc = GArc(165, 200, 0 ,180, x=325, y=290)
    arc.filled = True
    arc.fill_color = 'black'
    return arc


def doraemon():
    hand = doraemon_hand()
    window.add(hand)
    body = doraemon_body()
    window.add(body)
    bodywhite = doraemon_bodywhite()
    window.add(bodywhite)
    ring = doraemon_ring()
    window.add(ring)
    blue_head = doraemon_blue_head()
    window.add(blue_head)
    white_head = doraemon_white_head()
    window.add(white_head)
    nose = doraemon_nose()
    window.add(nose)
    eye1 = doraemon_eye1()
    window.add(eye1)
    eye2 = doraemon_eye2()
    window.add(eye2)
    eye3 = doraemon_eye3()
    window.add(eye3)
    eye4 = doraemon_eye4()
    window.add(eye4)
    eye5 = doraemon_eye5()
    window.add(eye5)
    eye6 = doraemon_eye6()
    window.add(eye6)
    mouth1 = doraemon_mouth1()
    window.add(mouth1)
    smile = doraemon_smile()
    window.add(smile)
    beard1 = doraemon_beard1()
    window.add(beard1)
    beard2 = doraemon_beard2()
    window.add(beard2)
    beard3 = doraemon_beard3()
    window.add(beard3)
    beard4 = doraemon_beard4()
    window.add(beard4)
    beard5 = doraemon_beard5()
    window.add(beard5)
    beard6 = doraemon_beard6()
    window.add(beard6)
    finger = doraemon_finger()
    window.add(finger)
    bag = doraemon_bag()
    window.add(bag)
    bell = doraemon_bell()
    window.add(bell)


def doraemon_bell():
    bell = GOval(30, 30, x=245, y=425)
    bell.filled = True
    bell.fill_color = 'gold'
    bell.color = 'gold'
    return bell


def doraemon_bodywhite():
    arc = GArc(160, 750, 180, 180, x=175, y=200)
    arc.filled = True
    arc.fill_color = 'ivory'
    arc.color = 'ivory'
    return arc


def doraemon_bag():
    arc = GArc(100, 200, 180, 180, x=210, y=425)
    arc.filled = True
    arc.fill_color = 'ivory'
    arc.color = 'black'
    return arc


def doraemon_finger():
    finger = GOval(50, 50, x=375, y=390)
    finger.filled = True
    finger.fill_color = 'ivory'
    finger.color = 'black'
    return finger


def doraemon_hand():
    hand = GRect(180, 30, x=225, y=400)
    hand.filled = True
    hand.fill_color = 'blue'
    return hand


def doraemon_ring():
    arc = GArc(200, 180, 180 ,180, x=150, y=340)
    arc.filled = True
    arc.fill_color = 'red'
    return arc


def doraemon_body():
    body = GOval(200, 700, x=150, y=180)
    body.filled = True
    body.fill_color = 'blue'
    body.color = 'black'
    return body


def doraemon_beard6():
    beard = GLine(300, 330, 365, 355)
    return beard


def doraemon_beard5():
    beard = GLine(220, 330, 160, 355)
    return beard


def doraemon_beard4():
    beard = GLine(300, 300, 365, 300)
    return beard


def doraemon_beard3():
    beard = GLine(160, 300, 220, 300)
    return beard


def doraemon_beard2():
    beard = GLine(160, 255, 220, 275)
    return beard


def doraemon_beard1():
    beard = GLine(300, 275, 365, 255)
    return beard


def doraemon_smile():
    arc = GArc(180, 100, 180 ,180, x=160, y=325)
    return arc


def doraemon_mouth1():
    mouth1 = GLine(260, 275, 260, 365)
    return mouth1


def doraemon_eye6():
    eye_6 = GOval(5, 5, x=240, y=190)
    eye_6.filled = True
    eye_6.fill_color = 'ivory'
    eye_6.color = 'black'
    return eye_6


def doraemon_eye5():
    eye_5 = GOval(5, 5, x=275, y=190)
    eye_5.filled = True
    eye_5.fill_color = 'ivory'
    eye_5.color = 'black'
    return eye_5


def doraemon_eye4():
    eye_4 = GOval(15, 30, x=270, y=190)
    eye_4.filled = True
    eye_4.fill_color = 'black'
    eye_4.color = 'black'
    return eye_4


def doraemon_eye3():
    eye_3 = GOval(15, 30, x=235, y=190)
    eye_3.filled = True
    eye_3.fill_color = 'black'
    eye_3.color = 'black'
    return eye_3


def doraemon_eye2():
    eye_2 = GOval(50, 75, x=260, y=150)
    eye_2.filled = True
    eye_2.fill_color = 'ivory'
    eye_2.color = 'black'
    return eye_2


def doraemon_eye1():
    eye_1 = GOval(50, 75, x=210, y=150)
    eye_1.filled = True
    eye_1.fill_color = 'ivory'
    eye_1.color = 'black'
    return eye_1


def doraemon_nose():
    nose = GOval(30, 30, x=245, y=225)
    nose.filled = True
    nose.fill_color = 'red'
    nose.color = 'red'
    return nose


def doraemon_blue_head():
    head1 = GOval(300, 300, x=100, y=125)
    head1.filled = True
    head1.fill_color = 'blue'
    head1.color = 'blue'
    return head1


def doraemon_white_head():
    head2 = GOval(275, 250, x=115, y=175)
    head2.filled = True
    head2.fill_color = 'ivory'
    head2.color = 'black'
    return head2


if __name__ == '__main__':
    main()
