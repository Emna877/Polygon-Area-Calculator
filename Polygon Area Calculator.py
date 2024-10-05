class Rectangle:
    def __init__(self,width,height):
        self.height = height
        self.width = width

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self,new):
        self.width=new

    def set_height(self,new):
        self.height=new
    
    def get_area(self):
        return (self.height*self.width)

    def get_perimeter(self):
        return (2*self.width+2*self.height)
    
    def get_diagonal(self):
        return ((self.width**2+self.height**2)**0.5)

    def get_picture(self):
        if self.height>50 or self.width>50:
            return 'Too big for picture.'
        else:
            picture='\n'.join(["*" * self.width for _ in range(self.height)])
            return picture + '\n'
    
    def get_amount_inside(self,shape):
        return(self.get_area()//shape.get_area())
        

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.side=side
    
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'

    def set_side(self,new):
        self.side=new
        self.width=new
        self.height=new

    def set_width(self,new):
        self.set_side(new)
    
    def set_height(self,new):
        self.set_side(new)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))