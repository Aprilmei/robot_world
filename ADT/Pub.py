class pub():
    bankrupt=False
    def open(self):
        if not self.bankrupt:
            print("opened")
            
a=pub()
b=pub()
a.bankrupt=True
b.open()
            