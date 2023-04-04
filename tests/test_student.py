from school_schedule.student import Student

def test_instantiate_valid_student():
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
    
    result = quinn.name

    assert result == "Quinn"
    assert quinn.get_num_classes() == 6
