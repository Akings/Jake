from lib.parser import *
from lib.tokenizer import *
from lib.db import *


new = DBA()
new.create_table('ErrorMsgs')

class StartChat:
    # Asks user for input
    def __init__(self,):
        self.command = input("User> ")

    def start(self):
        tokens = Tokenizer().tokenize(self.command)
        Parser().parse(tokens)
        

while True:
    StartChat().start()
