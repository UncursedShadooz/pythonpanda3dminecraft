from direct.showbase.ShowBase import ShowBase

class Minecraft(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
game = Minecraft()
game.run()