from item import Item

class Currency(Item):
    def __init__(self, name, value, weight, instant_value):
        super().__init__(name, value, weight)
        self.instant_value = instant_value
