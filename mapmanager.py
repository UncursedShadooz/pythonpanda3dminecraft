from direct.showbase.ShowBase import ShowBase

class Mapmanager():
    def __init__(self):
        self.model = 'block.egg' 
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1) #rgba

        # create the main map node:
        self.startNew()

        # create building blocks
        # self.addBlock((0,10, 0))
        self.generateGrid(size_x=20, size_y=20, size_z=3, spacing=1.0)


    def startNew(self):
        self.land = render.attachNewNode("Land") # the node which all the map blocks are attached to

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    # def generateGrid(self, size_x, size_y, spacing):
    #     for x in range(size_x):
    #         for y in range(size_y):
    #             position = (x * spacing, y * spacing, 0)
    #             self.addBlock(position)

    def generateGrid(self, size_x, size_y, size_z, spacing):
        for x in range(size_x):
            for y in range(size_y):
                pos_x = x * spacing
                pos_y = 20 + (y * spacing)
                pos_z = -2
                
                position = (pos_x, pos_y, pos_z)
                self.addBlock(position)

class VoxelWorld(ShowBase):
    def __init__(self):
        super().__init__()
        self.manager = Mapmanager()

game = VoxelWorld()
game.run()