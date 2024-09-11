
class Person:
    
    city="Izmir"
    
    def __init__(self, birth_year, name, surname, gender):
        self.birth_year=birth_year
        self.name=name
        self.surname=surname
        self.gender=gender
        
    def body_properties(self,height_cm, weight_kg):
        self.height=height_cm
        self.weight=weight_kg
        
    
    def person_info(self):
        print("Person's Information:\n")
        print("Name and Surname:",self.name , self.surname)
        print("Birth year:", self.birth_year)
        print("Gender:", self.gender,"\n")
        
        
person1=Person(1997, "Selvet Elif","Demirel","woman")
person1.body_properties(167, 75)
person1.person_info()

person2=Person(1995, "Mr.Something", "Something","man")
person2.body_properties(191,90)
person2.person_info()