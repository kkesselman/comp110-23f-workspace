"""Making points."""

from lessons.CQ07.point import Point 

my_point: Point = Point(1.0, 1.0)
print(my_point.x)
print(my_point.y)

my_point.scale(3)
print(my_point.x)