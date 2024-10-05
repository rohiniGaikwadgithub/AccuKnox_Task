
# implementing a Rectangle class 

class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
        
    def __iter__(self):
        yield 'length', self.length
        yield 'width', self.width
        
    
# create a rectangle object
rect = Rectangle(10, 20)    

# iterate over the rectangle object
for item in rect:
    print(item)
