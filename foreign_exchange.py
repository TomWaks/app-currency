class ForeignExchange:
    def __init__(self, __short_name, __long_name):
        self.short_name = __short_name
        self.long_name = __long_name

        print("Created object ", self.short_name, "(" + self.long_name + ")")
        self.rate = []
        self.date = []

    def get_rate(self):
        print()
        print("Object ", self.short_name, "(" + self.long_name + ")")
        print(self.date)
        print(self.rate)
