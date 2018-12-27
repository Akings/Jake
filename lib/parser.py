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
        print('Jake> ' + self.reps)

    def parse(self, snt):
        if Parser().match(['what', 'your', 'name'], snt):
            Parser().respond('i am Jake')
            
        elif Parser().alt(["hello", "hi"], snt):
            Parser().respond("hello there")
            
        else:
            Parser().respond('i dont understand')
            
