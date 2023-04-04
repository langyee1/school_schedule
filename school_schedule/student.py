class Student:
    
    def __init__(self,name,grade,classes):
        self.name = name
        self.grade_level = grade
        self.classes = classes

    def add_class(self, class_name, **args): #at least it will have a class, but  w args ypu say youll have a bunch of other classes as well
        self.classes.append(class_name)
        for arg in args:#args is a tuple
            self.classes.append(arg)
        return self#for chaining       

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        print(f"{self.name} is a {self.grade_level}, and takes {', '.join(self.classes)}")
        
    