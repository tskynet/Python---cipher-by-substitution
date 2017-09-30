import ConfigParser
class Bdd:

    def __init__(self):
        self.cfg = ConfigParser.ConfigParser()
        self.isExist = False
        self.key = ""
        self.alphabet = [""]*78
        print "init bdd"

    def readBdd(self):
        self.cfg.read("param.cfg")

    def writeBdd(self, key, alphabet): #write a new line in bdd if the key doesnt exist
        self.readBdd()
        self.isExist = False
        self.checkBdd(key)
        if(self.isExist == True):
            print 'error, la cle existe deja!'
        else:
            self.cfg.set("Section1",key , alphabet)
            self.cfg.write(open('param.cfg','w'))
            print 'le else passe'

    def checkBdd(self, key): # for check if the key exist or not
        self.readBdd()
        for e in self.cfg.items('Section1'):
            if(key == e[0]):
                self.isExist = True
                self.key = e[0]
                self.alphabet = e[1]
                print 'ok bro'
            else:
                print 'not exist'

    def getBdd(self, key): #sert a recuperer l alphabet d une cle
        self.readBdd()
        self.checkBdd(key)
        if(self.isExist == True):
            print self.cfg.get('Section1', self.key)
                


#bdd = Bdd()
#bdd.readBdd()
#bdd.writeBdd("testparam1",'p')
#bdd.getBdd('cle1')

#bdd.checkBdd()
