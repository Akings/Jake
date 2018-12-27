from lib.parser import *
from lib.tokenizer import *

class startChat:

    def __init__(self,):
        self.command = input("User> ")

    def start(self):
        toks = Tokenizer().tokenize(self.command)
        Parser().parse(toks)


while True:
    startChat().start()