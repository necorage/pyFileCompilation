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
        return text.center( self.largeText - 2, " ")

    def header(self, text):
        cadena = self.pointLine("")
        cadena += self.pointLine(self.textLine(text))
        cadena += self.pointLine("")
        return cadena
    
    def readFile(self, filePath):
        f = open(filePath)
        data = f.read()
        f.close()
        return data+"\n"

    def folderFiles(self):
        fileData = ""
        for folder in pathlib.Path(self.rootDirectory).iterdir():   # search all directories in path 
            if folder.is_dir():
                subdir = folder.name
                for filePath in (pathlib.Path(subdir)).iterdir():       # search files in folders. Note that its a 'pathlib.WindowsPath' class
                    file = str(filePath)
                    if ".txt" in file:                              # search txt files in file path ()
                        fileName = file[(str(file).rfind('\\')+1):] # i take the fileName from path structure (folder/file.*)
                        fileData += self.header(fileName)
                        fileData += self.readFile(filePath)                        
        return (fileData)
    
    def saveInfo(self, allData):
        f = open(self.destination,'w')
        f.write(allData)
        f.close

import pathlib
import os
import platform

largeText = 80
destination = "demofile2.tcl"

rootDirectory = os.getcwd()
osSys = platform.system()

c1 = FileConverter(osSys, rootDirectory, destination, largeText)
c1.saveInfo(c1.folderFiles())
