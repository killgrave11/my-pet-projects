import math

#ошибки
class InvalidCircleError(Exception):
    """Raised when a circle has invalid radius"""
    
class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""
    
    
    
#площадь круга
def calc_circle_area(radius):
    if radius <=0:
        raise InvalidCircleError("Radius is lesws or equal to 0.")
    s = 3.14*(radius**2)
    return s



class Triangle():
    def __init__(self, ab, ac, bc):
        self.ab=ab
        self.ac=ac
        self.bc=bc

    #площадь треугольника
    def calc_triangle_square(self, ab, ac, bc):
        if ab <= 0 or ac <= 0 or bc <= 0:
            raise InvalidTriangleError("One or more of the sides is less or equal to 0.")
        p = (ab+ac+bc)/2
        s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
        return s
    
    #прямоугольный ли треугольник
    def is_rect(self, ab, ac, bc):
        if (ab**2)+(ac**2)==bc**2:
            return True
        elif (ac**2)+(bc**2)==ab**2: 
            return True
        elif (bc**2)+(ab**2)==ac**2:
            return True
        else:
            return False



#Примеры:

try:
    circle = calc_circle_area(10)
except InvalidCircleError as ex:
    print(ex)
else:
    print(circle)


try:
    triangle = Triangle(ab=5, ac=4, bc=3)
except InvalidTriangleError as ex:
    print (ex)
else:
    print(triangle.calc_triangle_square(ab=5, ac=4, bc=3))
    print(triangle.is_rect(ab=5, ac=4, bc=3))