class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("你好 " + self.name + "!")

    def goodbye(self):
        print("再见 " + self.name + "!")

if __name__ == '__main__':
    man = Man("良子")
    man.hello()
    man.goodbye()
