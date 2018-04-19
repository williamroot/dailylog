import turtle

def draw_square(square):
    for i in range(1,5):
        square.forward(100)
        square.right(90)

def draw_circle(circle):
    for i in range(1,5):
        circle.circle(100)
        circle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('black')
    art = turtle.Turtle()
    art.shape('square')
    art.speed(12)
    for i in range(1,73):
        draw_square(art)
        art.color('red')
        art.right(5)
    for i in range(1,73):
        draw_circle(art)
        art.color('white')
        art.right(-5)
    window.exitonclick()

if __name__ == '__main__':
    draw_art()
    
