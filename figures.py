class Square:
    def __init__(self, x_sqr, y_sqr, side, color_sqr):
        self.x_sqr = x_sqr
        self.y_sqr = y_sqr
        self.side = side
        self.color_sqr = color_sqr

    def draw(self, canvas):
        canvas.data[self.x_sqr: self.x_sqr + self.side, self.y_sqr: self.y_sqr + self.side] = self.color_sqr


class Rectangle:
    def __init__(self, x_rec, y_rec, width_rec, height_rec, color_rec):
        self.x_rec = x_rec
        self.y_rec = y_rec
        self.width_rec = width_rec
        self.height_rec = height_rec
        self.color_rec = color_rec

    def draw(self, canvas):
        canvas.data[self.x_rec: self.x_rec + self.width_rec, self.y_rec: self.y_rec + self.height_rec] = self.color_rec

