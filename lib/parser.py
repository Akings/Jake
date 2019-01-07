from Jake.lib.db import *
from Jake.lib.models import Message
from datetime import datetime
from random import choice

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

    def parse(self,res, snt):
        choices = {1:"greetings",2:"questions about me",
                   3:"questions about weather",4:"I dont know",5:"conversation",6:"actions"}
        thanks = ['Hey thanks',"I appreciate that","Thanks for improving me","I'm really grateful"]
        #print(mes)
        #print(res)
        #print(snt[0])

            
        #if self.match(res,snt):
         #   print(True)
         #   self.respond(choice(res))
        #elif self.alt()
        if len(res) > 0:
            self.respond(choice(res))
            
        else:
            self.respond("still improving, i don't understand that for now")
            user = input("Please teach me the answer: ")
            print("""My Categories:{}
            """.format(choices))
            cat = input("To what category does this answer belong?: ")
            string = ""
            for i in snt:
                string += i + " "
            string = string.strip()
            # date = datetime.now().date()
            # time = datetime.now().time()
            new = Message()
            new.message = string
            new.response = user
            new.category = choices[(int(cat))]
            new.save()
            print(choice(thanks))
            #self.db.create_error(string)

