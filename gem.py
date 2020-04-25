class SupportGem:
    def __init__(self):
        self.multiplier = 1

class Empower(SupportGem):
    def __init__(self, level):
        self.level = level
        self.tags = ['Active']
        self.multiplier = 1.25
    

class Enlighten(SupportGem):
    def __init__(self, level):
        self.level = level
        self.tags = ['Active']
    
    @property
    def multiplier(self):
        return 1 - (self.level - 1) * 0.04