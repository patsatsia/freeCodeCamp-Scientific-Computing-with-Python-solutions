class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height})")

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        string = (("*"*self.width) + "\n") * self.height

        return string


    def get_amount_inside(self, shape):
        current_area = self.height * self.width
        passed_in_area = shape.height * shape.width
        number_of_times = int(current_area/passed_in_area)
        return number_of_times

class Square(Rectangle):
    
    def __init__(self, single_side_length):
        self.height = single_side_length
        self.width = single_side_length

    def __str__(self):
        return f"Square(side={self.height})"

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_height(self, single_side_length):
        self.height = single_side_length
        self.width = single_side_length

    def set_width(self, single_side_length):
        self.height = single_side_length
        self.width = single_side_length