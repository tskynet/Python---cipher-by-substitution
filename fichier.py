
# monFichier = open("test.txt","r")
# contenuFichier = monFichier.read()
# print (contenuFichier)
# inputLocal = raw_input(">")
# monFichierLocal = open(inputLocal, "r")
# contenuFichierLocal = monFichierLocal.read()
# print (contenuFichierLocal)

class TextInput:

    def __init__(self, urlFile):
        self.urlFile =  urlFile
        self.thisFile = open(urlFile, "r")
    def printFile(self):
        print (self.thisFile.read())
        

    def closeFile(self):
        self.thisFile.close()

    def readFile(self):
        text = ""
        text = self.thisFile.read()
        
        return text
    def writeFile(self, cipherText):
        # penser à rajouter try catch & if pour verifier que l'url est bien set
        self.closeFile()
        self.thisFile = open(self.urlFile, "w")
        self.thisFile.write(cipherText)
        self.closeFile()
# test = TextInput("D:/dev in python/chiffrement substitution/test.txt")
