from Jake.lib.db import *
from Jake.lib.models import Message
from datetime import datetime
from random import choice

class Parser:
    def __init__(self):
        self.name = "Jake"

    def change_name(self,new_name):
        self.name = new_name
        return "I like my new name, {}".format(self.name)

    def match(self, arr, snts):
        count = 0
        for i in arr:
            if i in snts:
                count += 1
        #if count == len(arr):
        if (count/len(arr)*1.0) >= 0.5:
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
        
    def respond(self,reps):
        self.reps = reps
        print ('{}> '.format(self.name) + self.reps)

    def parse(self,res, snt):
        choices = {1:"greetings",2:"questions about my name",3:"questions about coding",4:"I dont know",5:"conversation",
                   6:"actions",7:"general questions about me",8:"questions about what i can do"}
        action_cat = {1:"calls",2:"change my name",3:"weather"}
        thanks = ['Hey thanks',"I appreciate that","Thanks for improving me","I'm really grateful"]
        #print(mes)
        #print(res)
        #print(snt[0])

            
        #if self.match(res,snt):
         #   print(True)
         #   self.respond(choice(res))
        #elif self.alt()
        if len(res) > 0:
            #for key,value in self.actions().items():
                #print(snt)
             #   if self.match(value[2],snt):
             #       param = []
             #       for i in value[1]:
             #           user = input(i+": ")
             #           param.append(user)
             #       func = value[0]
             #       print(func)
             #       self.respond(func(self,param[:]))
             #   else:
                self.respond(reps=choice(res))

                #print(value[2])
                #if snt[0] in value[2]:
                #    print(key)

        else:
            self.respond(reps="still improving, i don't understand that for now")
            user = input("Please teach me the answer: ")
            print("""My Categories:\n{}
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
            if choices[(int(cat))] == "actions":
                print("Please help me, which action category do i classify this?\naction categories: \n{}".format(action_cat))
                act_cat = input("Classify the action: ")

                new.category = action_cat[(int(act_cat))]
            else:
                new.category = choices[(int(cat))]
            new.save()
            print(choice(thanks))
            #self.db.create_error(string)
            #print(self.actions())


    def actions(self):
        actions = {}
        all = Parser.__dict__
        for name,value in all.items():
            if not name.startswith("__"):
                if "name" in name:
                    actions[name]=[value,['new_name'],['change','name','new','name']]
            #if keyword in name:
            #    value(self,"Theo")
        return actions




