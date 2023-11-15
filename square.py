import math
class Square:
    def __init__(square, first_x, scnd_x, first_y, scnd_y, px, py):
        square.first_x = first_x
        square.scnd_x = scnd_x
        square.first_y = first_y
        square.scnd_y = scnd_y
        square.px = px
        square.py = py
    
    def calc_dist(self):
        return int(math.sqrt(pow(self.scnd_x - self.first_y, 2) + pow(self.scnd_y - self.first_y, 2)))
    
    def dist_x(self):
        return abs(self.scnd_x - self.first_x)
        
    def dist_y(self):
        return abs(self.scnd_y - self.first_y)
    def area(self):
        return self.dist_x() * self.dist_y();
    def perimeter(self):
        return 2 * (self.dist_x() + self.dist_y())
    def contains(self):
        if(self.px >= self.first_x and self.py >= self.first_y and self.px <= self.scnd_x and self.py <= self.scnd_y):
            return True
        else:
            return False
        
      
s1 = Square(0, 3, 0, 5, 0, 10)

print(s1.calc_dist())
print(s1.dist_x())
print(s1.dist_y())
print(s1.area())
print(s1.contains())
