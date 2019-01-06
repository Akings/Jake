from lib.db import *
from lib.objects import *


class Message(DBA):
    id = models.IntegerField(PRIMARY_KEY=True)
    message = models.CharField(max_length=1000)

