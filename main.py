from school_schedule.student import Student

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting").add_class("Calc 2").add_class("Calc 3").add_class("Calc 4")
quinn.get_num_classes()
quinn.summary()

# second instance
claire = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

#claire.add_class("Painting", ("Algebra 3", "Chemistry"))
claire.get_num_classes()
claire.summary()

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function