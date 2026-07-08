#rectangle class creation
class rectangle:
    #member variable 
    length = 0 
    breadth = 0

    #method to initialize data
    def initialize(self , l , b):
        self.length = l
        self.breadth = b

    # method to display the data 
    def display(self):
        print("--------------Rectangle---------------")
        print("Length is: ",self.length)
        print("Breadth is: ",self.breadth)
        print("---------------------------------------")
#------------------------------------------

#object creation
rect = rectangle()
rect.initialize(20,50)
rect.display()