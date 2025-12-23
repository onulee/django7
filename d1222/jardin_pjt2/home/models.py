from django.db import models

class ChartData(models.Model):
    cno = models.AutoField(primary_key=True)
    cyear = models.CharField(max_length=4)
    cdata = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.cno},{self.cyear},{self.cdata}'


class Payment(models.Model):
    # member = models.ForeignKey(Member, on_delete=models.CASCADE)
    member = models.CharField(max_length=100)
    tid = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    approved_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.member},{self.tid},{self.order_id}'