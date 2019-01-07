from Jake.lib.parser import Parser
from Jake.lib.tokenizer import *
from Jake.lib.models import Message


class StartChat:
    # Asks user for input
    def __init__(self,):
        self.command = input("Waiting for your input> ")
        self.name = "Jake"

    def start(self):
        tokens = Tokenizer().tokenize(self.command)
        res = []
        mes = []
        cat = []
        checker = ""
        for index,i in enumerate(tokens):
            if len(tokens)<2:
                checker +=i+""
            else:
                if not index == len(tokens)-1:
                    checker += i + " "
                else:
                    checker += i + ""
        #print(checker)
        all = Message.objects.filter(message=checker)
        if len(all) > 0:
            for i in all:
                res.append(i.response)
                mes.append(i.message)
                cat.append(i.category)
        else:
            mes = tokens
        message = []
        for i in mes:
            m = i.split(" ")
            for i in m:
                message.append(i)
        #print(message)
        if len(cat)>0:
            res = []
            all = Message.objects.filter(category=cat[0])
            if len(all) > 0:
                for i in all:
                    res.append(i.response)
        #print(res)
        #print(cat)
        Parser().parse(res=res,snt=tokens)


while True:
    StartChat().start()

