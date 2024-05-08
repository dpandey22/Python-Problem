# Object Oriented Program

class Run:
    def __init__(self):
        self.__miles=4
        self.races=5
    def run(self):
        if self.__miles==4:
            return self.__miles
        self.races=8
        return self.races*self.__miles

turbo=Run()
turbo._Run__miles=2
print(turbo.run())
