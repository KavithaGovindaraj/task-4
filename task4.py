class Circle:
    def __init__(self,lst) :
        self.lst = lst
        self.pi = 3.141
    # create area method
    def area (self) :
        area_lst = []
        a = 0
        for radius in self.lst :
            a = (self.pi)*(radius**2)
            area_lst.append(a)
        return area_lst
    # create perimeter method
    def perimeter (self) :
        perimeter_lst = []
        p = 0
        for radius in self.lst :
            p = 2*(self.pi)*radius
            perimeter_lst.append(p)
        return perimeter_lst
    
circle_1= Circle([10,501,22,37,100,999,87,351])
print(circle_1.area())           
print(circle_1.perimeter())



 