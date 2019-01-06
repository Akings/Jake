from lib.db import *
from models import Message
from datetime import datetime

class Parser:
    def __init__(self):
        pass

    def match(self, arr, snts):
        count = 0
        for i in arr:
            if i in snts:
                count += 1
        if count == len(arr):
            return True
        else:
            return False

    def alt(self, arr, snts):
        count = 0
        for i in arr:
            if i in snts:
                count += 1
        if count >= 1:
            return True
        else:
            return False
        
    def respond(self, reps):
        self.reps = reps
        print ('Jake> ' + self.reps)

    def parse(self, snt):
        if self.match(['what', 'your', 'name'], snt):
            self.respond('i am Jake')
            
        elif self.alt(["hello", "hi","hey"], snt):
            self.respond("hello there")
            
        else:
            self.respond("still improving, i don't understand that for now")
            string = ""
            for i in snt:
                string += i + " "
            string = string.strip()
            # date = datetime.now().date()
            # time = datetime.now().time()
            new = Message()
            new.message = string
            new.save()
            #self.db.create_error(string)

