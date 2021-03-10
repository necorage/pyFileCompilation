class FileConverter:
    def __init__(self, osSys, rootDirectory, destination, largeText):
        self.osSys = osSys
        self.rootDirectory = rootDirectory
        self.destination = destination
        self.largeText = largeText

    def osPlatform(self):
        if self.osSys == "Windows":
            return "\\"
        else:
            return "/"

    def pointLine(self, text):
        return text.center(self.largeText, "#") + '\n'

    def textLine(self, text):
        return "text".center( self.largeText - 2, " ")


    def header(self, text):
        cadena = self.pointLine("")
        cadena += self.pointLine(self.textLine('text'))
        cadena += self.pointLine("")
        return cadena
        

import pathlib
import os


largeText = 80

destination = "demofile2.tcl"
rootDirectory = os.getcwd()

import platform
osSys = platform.system()

c1 = FileConverter(osSys, rootDirectory, destination, largeText)

print (c1.header(' texto cadena 1'))