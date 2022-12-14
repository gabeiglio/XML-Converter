import uuid
import xml.etree.ElementTree as et

# TODO: Create object wrapper for better manipulation and customization of css properties for now
class Document(object):
    def __init__(self, path):
        self.path = path
        self.file = open(path, "a")
        self.write("<!DOCTYPE html>\n<head></head>\n<body>\n")

    def write(self, input):
        self.file.write(input)

    def script(self):
        self.write("<script>\n")

        #looping through all ids and adding the respective js code
        #"document.getElementById(\"{}\").value".format(id)

        self.write("</script>")

    def addButtonExportXML(self):
        self.write("<button type=\"button\">Export to XML</button>")

    def close(self):
        self.addButtonExportXML()
        self.write("</body>\n</html>")
        self.file.close()

class Item(object):
    def __init__(self, item):
        self.item = item
        self.uuid = uuid.uuid4()

    def htmlTerminal(self, scope):
        result = printScope(scope) + "<div style=\"margin: 20px;\">\n" + printScope(scope + 1) + "<p>{}</p>\n".format(self.item.tag) + printScope(scope + 1) + "<input type=\"text\" id=\"{}\" style=\"height: 100px; width: 100%;\">\n".format(self.uuid) + printScope(scope) + "</div>\n"
        return result

    def htmlContainer(self, scope):
        result = printScope(scope) + "<div style=\"margin: {}px; padding: 20px; border-style: solid; border-color: gray; background-color: #E5E8E8; border-radius: 25px;\">\n".format(10 * scope) + printScope(scope) + "<h3>{}</h3>\n".format(self.item.tag)
        return result

def printScope(scope):
    result = ""
    for i in range(0, scope):
        result = result + " "
    return result

def traverse(root, scope, document):
    item = Item(root)
    document.write(item.htmlContainer(scope) if len(root) != 0 else item.htmlTerminal(scope))

    for item in root:
        traverse(item, scope + 1, document)

    if (len(root) != 0):
        document.write(printScope(scope) + "</div>\n")

def compileHTML(xml_file):
    # TODO: later change to function argument
    tree = et.parse(r"C:\Users\gigliozzi\Desktop\XML-Converter\tests\test1.xml")
    root = tree.getroot()

    # TODO: grab name of input file and create file output with same name
    document = Document("output.html")
    traverse(root, 1, document)
    document.close()

compileHTML("")
