class Point():
    def __init__(self,x, y):
        #self. - means that these value will be stored inside Point itself
        # in properties that we are gonna call x and y
        self.x = x
        self.y = y

p = Point(2, 2)
print(p.x)
print(p.y)