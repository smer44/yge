from yge.turnbased.yitem import yItem
class yFillItem(yItem):

    def __init__(self, *color):
        super().__init__(str(color),True)
        self.color = color

    def __display__(self,display):
        print(f"yFillItem.__display__ : {self.color}")
        display.fill(self.color)

    def __repr__(self):
        return f"<FillItem:{self.color}>"

    def __str__(self):
        return f"<FillItem:{self.color}>"