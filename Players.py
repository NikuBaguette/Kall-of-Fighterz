class New_Players:
    count = 0
    def __init__(self,name="NEW_PLAYER",life=1000,height=100,width=60):
        self.name = name
        self.hp = life
        self.height = height
        self.width = width
        self.Stunned = False
    
    def GetStunned(self,time=1):
        self.Stunned=True
        #wait for time sec
        self.Stunned=False
        return None
        
    def IsStunned(self):
        return self.Stunned
