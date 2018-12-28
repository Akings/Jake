from datetime import datetime
def print_kw(**kwargs):

    for key, value in kwargs.items():
        print("key {} and value {}".format(key,value))


print_kw(id=2,date="today")
