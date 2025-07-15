class Ale:
    def __init__(self, name, abv):
        self.name = name
        self.abv = abv

def alcohol_content(self, volunme_in_oz):
    return self.abv * volunme_in_oz

def description(self):
    return f"(self.name): {self.abv * 100:.1f}% ABV"

class PaleAle(Ale):
    def __init__(self):
        super().__init__("Pale Ale", 0.055)


class IPA(Ale):
    def __init__(self):
        super().__init__("IPA", 0.065)


class Stout(Ale):
    def __init__(self):
        super().__init__("Stout", 0.07)


class Porter(Ale):
    def __init__(self):
        super().__init__("Porter", 0.06)

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 