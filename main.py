from lib.parser import Parser
from lib.tokenizer import *
from models import Message


class StartChat:
    # Asks user for input
    def __init__(self,):
        self.command = input("User> ")

    def start(self):
        tokens = Tokenizer().tokenize(self.command)
        Parser().parse(tokens)


while True:
    StartChat().start()

