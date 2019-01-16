class Juese:
    def __init__(self, name, zy, smz, gjl):
        self.name = name
        self.zy = zy
        self.smz = smz
        self.gjl = gjl

    def gj(self, gjdx):
        gjdx.smz -= self.gjl
        print(gjdx.smz)


Garen = Juese('Garen', 'D', 200, 100)
Riven = Juese('Riven', 'N', 100, 200)

Garen.gj(Riven)

if hasattr(Garen, 'gj'):
    func = getattr(Garen, 'gj')
    func(Riven)