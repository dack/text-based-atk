import items

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name = "Gold", description = "dat CASH MONEY $$$", value = self.amt)
