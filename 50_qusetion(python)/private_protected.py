class Demo:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"

    def display(self):
        print(self._protected)
        print(self.__private)

obj = Demo()
obj.display()