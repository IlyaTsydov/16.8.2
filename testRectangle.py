from rectangle import Rectangle, Square, Circle

r1 = Rectangle(2, 3)
r2 = Rectangle(2, 4)

print(r1.get_area())
print(r2.get_area())

s1 = Square(3)
s2 = Square(7)

print(s1.get_area_square(),
      s2.get_area_square())

c1 = Circle(2)
c2 = Circle(3)

print(c1.get_area_circle())
print(c2.get_area_circle())


figures = [r1, r2, s1, s2, c1, c2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())