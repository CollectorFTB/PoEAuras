class SupportGem:
    def __init__(self):
        self.multiplier = 1
    
    def apply_to(self, active):
        pass

class Empower(SupportGem):
    def __init__(self, level, quality=0):
        self.name = 'Empower'
        self.level = level
        self.quality = quality
        self.tags = ['Support']
        self.support_list = ['Active']
        self.multiplier = 1.25
    
    def apply_to(self, active):
        active.level += self.level-1

class Enlighten(SupportGem):
    def __init__(self, level, quality=0):
        self.name = 'Enlighten'
        self.level = level
        self.quality = quality
        self.tags = ['Support']
        self.support_list = ['Active']
    
    @property
    def multiplier(self):
        return 1 - (self.level - 1) * 0.04