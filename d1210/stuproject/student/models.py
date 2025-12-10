from django.db import models

# 테이블을 생성하면 항상 id - AutoField 생성이 됨.
# 테이블명 student_student 생성 됨.
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    grade = models.IntegerField(default=1)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.sno},{self.name},{self.age},{self.grade},{self.gender}"
    
    
