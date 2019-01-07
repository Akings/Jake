from Jake.lib.db import *
from Jake.lib.objects import *


class Message(DBA):
    id = models.IntegerField(PRIMARY_KEY=True)
    message = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    category = models.CharField(max_length=200)



#obj = Message()
#obj.create_all()

