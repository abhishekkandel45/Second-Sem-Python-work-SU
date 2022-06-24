# Example of creating pakage in python.

class Package:
    def __init__(self, name, version, author, description):
        self.name = name = ("I am a package")
        self.version = version= (2.0)
        self.author = author =("Abhishek")
        self.description = description = ("Assignment V")

    def __str__(self):
        return "Package: {}, Version: {}, Author: {}, Description: {}".format(self.name, self.version, self.author, self.description) # return the string representation of the object

#PRINTING THE PACKAGE
print(Package)
