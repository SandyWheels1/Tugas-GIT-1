class MoneyAnalyzer:
    def __init__(self):
        pass
    def praise(self):
        Money = int(input("How much you have?"))
        if Money >= 500:
            print ("damn you rich")
        elif Money >= 200:
            print ("okay")
        else:
            print ("poor")

checker = MoneyAnalyzer()
checker.praise()