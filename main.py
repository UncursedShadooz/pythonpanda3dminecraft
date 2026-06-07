from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Minecraft(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(90)
        base.camera.setPos(0, -20, 3)

game = Minecraft()
game.run()