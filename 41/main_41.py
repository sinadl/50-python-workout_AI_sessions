class Scoop():
    def __init__(self,flavor):
        self.flavor = flavor
        
class Bowl():
    max_scoop = 3
    def __init__(self):
        self.scoops = []
        
    def add_scoops(self,*new_scps):
        for scp in new_scps:
            if len(self.scoops) < self.max_scoop:
                self.scoops.append(scp)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
    
class Bigbowl(Bowl):
    max_scoop = 5
    
    
    
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('cooki')
s5 = Scoop('strabbery')
b = Bigbowl()
b.add_scoops(s1, s5,s3,s1)
b.add_scoops(s3,s4,s2)
print(b)