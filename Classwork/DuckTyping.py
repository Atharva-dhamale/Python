
#Duck Typing : It is a concept where the type of an object is determined by its behaviour , not by its class

class InkjetPrinter:
    def printdocument(self,document):
        print("Inkjet printer printing :",document)

class LazerPrinter:
    def printdocument(self,document):
        print("Lazer printer printing :",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"PDFWriter saving {document} as PDF:")


def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LazerPrinter())
    StartPrinting(PDFWriter())

main()