from Rect import Rectangle
from Trian import Triangle


class Child(Rectangle, Triangle):
    def __init__(self, base, height, l, b):
        Rectangle.__init__(self, l, b)
        Triangle.__init__(self, base, height)


child = Child(base=2, height=2, l=4, b=5)
result_train = child.area_triangle()
print("Are of triangle : ", result_train)

result_rect = child.area_rectangle()
print("Are of Rectangle : ",result_rect)