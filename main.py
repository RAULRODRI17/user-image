from canvas import Canvas
from figures import Square, Rectangle

# Obtaining canvas width and height from the user 'int' is convert to integers the number of the user
canvas_width = int(input("Please enter a canvas width: ")) # this is the width of the total image
canvas_height = int(input("Please enter a canvas height: "))

colors = {'white': [255, 255, 255], 'black': [0, 0, 0]}
canvas_color = input("please select a color (white or black): ")

#Canvas is a pre established class in python that generates figures() requires
# (figures such: circle, square, rectangle, etc)
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

##data =
##data[:] = [255, 255, 0] # the ':' access all the data inside the matrix
#data = np.zeros((height, width 3), dtype=np.uint8)
#print(data)

# Make an array path

##data[0:1, 0:2] = [0, 200, 255]
## data[4:5, 3:5] = [255, 0, 100]
##data[0:1, 0:2] = [200, 200, 0]
##data[1:2, 1:3] = [100, 100, 0]
##data[2:3, 2:4] = [0, 0, 0]
##data[3:4, 1:3] = [0, 100, 100]
##data[4:5, 0:2] = [0, 255, 255]
## data[4:5, 3:5] = [255, 0, 100] # 4:5 is the row and the 3:5 column

#img = Image.fromarray(data, 'RGB')
#img.save('canvas.png')

while True:
    figure = input("What do you like to draw? (rectangle or square), Enter quit to quit: ")

    if figure.lower() == 'rectangle':
        x_rec_user = int(input("Enter x of the rectangle: "))  # this is going to begin in the coordinate
        y_rec_user = int(input("Enter y of the rectangle: "))
        width_rec_user = int(input("Enter width of the rectangle: "))  # these are the sides of the rectangle inside the total image
        height_rec_user = int(input("Enter height of the rectangle: "))
        color_red_user = int(input("How much red should the rectangle have (from 0 to 255)? "))  # this is to define the color of the rectangle
        color_green_user = int(input("How much green should the rectangle have (from 0 to 255)? "))
        color_blue_user = int(input("How much blue should the rectangle have (from 0 to 255)? "))

        rec = Rectangle(x_rec=x_rec_user, y_rec=y_rec_user, width_rec=width_rec_user, height_rec=height_rec_user,
                        color_rec=(color_red_user, color_green_user, color_blue_user))
        rec.draw(canvas)

    if figure.lower() == 'square':
        x_sqr_user = int(input("Enter x of the square: "))  # this is going to begin in the coordinate
        y_sqr_user = int(input("Enter y of the square: "))
        side_user = int(input("Enter the side of the square: "))
        color_sqr_red = int(input("How much red should the square have (from 0 to 255)? "))
        color_sqr_green = int(input("How much green should the square have (from 0 to 255)? "))
        color_sqr_blue = int(input("How much blue should the square have (from 0 to 255)? "))

        sqr = Square(x_sqr=x_sqr_user, y_sqr=y_sqr_user, side=y_sqr_user, color_sqr=(color_sqr_red, color_sqr_green,
                                                                                     color_sqr_blue))
        sqr.draw(canvas)

    if figure.lower() == 'quit':
        break

canvas.make('canvas.png')


