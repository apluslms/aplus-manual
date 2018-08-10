'''
Created on 9 Aug 2018

@author: atilante
'''

def get_direction(n):
    # Puolitetaan lukua n kunnes se on pariton.
    while not n % 2:
        n /= 2
    # Valitaan suunta luvun n jakojäännöksen mukaan.
    return "right" if n % 4 == 1 else "left"


def turtles(t):
    # Määritetään askeleen pituus
    step = 5
    # Määritellään nopeus maksimiksi
    t.speed(0)
    # Piirretään tuhat askelta
    for i in range(1, 1001):
        # Siirrytään eteenpäin
        t.forward(step)
        # Valitaan suunta
        turn = get_direction(i)
        # Käännytään 90 astetta valittuun suuntaan
        if turn == 'left':
            t.left(90)
        else:
            t.right(90)

if __name__ == "__main__":

    # The code template for students

    import turtle
    lightningFast = turtle.Turtle()
    turtles(lightningFast)
    window = turtle.Screen()
    window.exitonclick()


    # Alternative code example for exercise grader
    #import simpleturtle
    #lightningFast = simpleturtle.Turtle()
    #turtles(lightningFast)
    #lightningFast.get_image().write_to_file('dragon_curve.png')
