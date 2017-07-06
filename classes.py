##students = []
#class Student:
## Class attribute olarak school_name tanimladik
#    school_name = "TOPHANE TEKNIK"
 #   def add_student(self, name,student_id=332):
  #      student = {"name":name,"student_id":student_id}
   #     students.append(student)

#student = Student()
#student.add_student("Mark")
#student.add_student("Ismail",135)
#print(students)


##CONSTRUCTOR METHODU __INIT__ kullanilir  student_add seklinde fonksiyonu cagirmana gerek yok.
sdes=[]

class Student:
    school_name= "TOPHANE MESLEK"
    def __init__(self, name,sde_id=332):
        self.name = name
        self.sde_id = sde_id
        sdes.append(self)
    def __str__(self):
        return "SDE " + self.name

    def get_school_name(self):
        return self.school_name
    def get_name_capitalize(self):
        return self.name.capitalize()

#abuzer = SDE("FUAT")
#print(sdes)

#print(abuzer)

#print(Student.school_name)
#yukaridaki print islemi, class instancei olusturmuyor. classin icerisindeki attributeu direkt olarak cagiriyor)

##Instance Attributelari , tum instance icerisinde gecerli olan tanimlardir, Class Attributeleri , Class in tamaminda genel olarak gecerli olan attributelerdir. Class attributelari methodlarin ustunde ancak Classin icerisinde tanimlamalisin.

class HighSchoolStudent(Student):
    school_name = "HURRIYET EML"
    def get_school_name(self):
        return "This is a High School Student"
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

james = HighSchoolStudent("james")
print(james.get_school_name())
print(james.get_name_capitalize())
