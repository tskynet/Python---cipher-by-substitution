#!/usr/bin/env python
# coding: utf-8
import random
from fichier import *
from bdd import *
class Cipher:

    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","é","à","ç","è","ê","â","ë","ä"," ","?",";",".",":","!","\"","'","0","1","2","3","4","5","6","7","8","9"]
        self.alphabetTransition = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","é","à","ç","è","ê","â","ë","ä"," ","?",";",".",":","!","\"","'","0","1","2","3","4","5","6","7","8","9"]
        self.alphabetCipher = [""]*78
        self.cipherText=""
    def cipher(self, key, urlText):
        try:
            textCrypt = ""
            textClean = TextInput(urlText)
            text_ = textClean.readFile()
            self.generateAlphabet()
            text_temp  =[]
            for e in text_:
                cc = self.alphabet.index(e)
                text_temp.append(self.alphabetCipher[cc])

            textCrypt="".join(text_temp)

            
            self.cipherText = textCrypt
            print "your cipher text : "+self.cipherText
            bdd = Bdd()
            bdd.writeBdd(key, self.alphabetCipher)
            textClean.writeFile(self.cipherText)
            
        except NameError:
            print "Oops ! that was no valid url. Try again..."
    def generateAlphabet(self):
        i=0
        while i < 78:
            y = random.randint(0,len(self.alphabetTransition)-1)
            self.alphabetCipher[i] = self.alphabetTransition[y]
            del self.alphabetTransition[y]

            i = i +1

    def uncipherText(self, key, urlText):
        bdd = Bdd()
        bdd.getBdd(key)
        if (bdd.isExist == True):
            cipherAlphabet = bdd.alphabet
            textCipher = TextInput(urlText)
            text_ = textCipher.readFile()
            textDecryp =""
            text_temp = []
            for e in text_:
                cc = self.alphabetCipher.index(e)
                text_temp.append(self.alphabet[cc])
            textDecrypt = "".join(text_temp)
            print "Your text is : "+textDecrypt


        else:
            print "Sorry but, the following ressource is missing : textCipher"
cipher = Cipher()
cipher.generateAlphabet()
print cipher.alphabetCipher
