#!/usr/bin/python
import random
class Cipher:
    
    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.alphabetTransition = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.alphabetCipher = [""]*26
        self.cipherText=""
    def cipher(self, text_):
        textCrypt = ""
        text_ = text_.lower()
        
        self.generateAlphabet()
        text_temp  =[]
        for e in text_:
            cc = self.alphabet.index(e)
            text_temp.append(self.alphabetCipher[cc])

        textCrypt="".join(text_temp)
        self.cipherText = textCrypt
        print self.cipherText

    def generateAlphabet(self):
        i=0
        while i < 26:
            y = random.randint(0,len(self.alphabetTransition)-1)
            self.alphabetCipher[i] = self.alphabetTransition[y]
            del self.alphabetTransition[y]
            
            i = i +1

    def uncipherText(self):
        
        if self.cipherText != "":
            textDecryp =""
            text_temp = []
            for e in self.cipherText:
                cc = self.alphabetCipher.index(e)
                text_temp.append(self.alphabet[cc])
            textDecrypt = "".join(text_temp)
            print textDecrypt
            

        else:
            print "Sorry but, the following ressource is missing : textCipher"








