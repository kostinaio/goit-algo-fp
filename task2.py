

import turtle

WIDTH = 15
BRANCH_LENGTH = 120
ROTATION_ANGLE = 27

class TreeFractal(turtle.Turtle):
    def __init__(self, level):
        super(TreeFractal, self).__init__()
        self.level = level
        self.hideturtle()
        self.speed('fastest')
        self.left(90)
        self.width(WIDTH)
        self.penup()
        self.back(BRANCH_LENGTH * 1.5)
        self.pendown()
        self.forward(BRANCH_LENGTH)
        self.draw_tree(BRANCH_LENGTH, level)

    def draw_tree(self, branch_length, level):
        width = self.width()
        self.width(width * 3. / 4.)
        branch_length *= 3. / 4.
        self.left(ROTATION_ANGLE)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.right(2 * ROTATION_ANGLE)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.left(ROTATION_ANGLE)

        self.width(width)

if __name__ == '__main__':
    print("Вкажіть необхідний рівень рекурсії:")
    tree_level = int(input())
    window = turtle.Screen()
    window.bgcolor("white")
    tree = TreeFractal(tree_level)
    turtle.done()
