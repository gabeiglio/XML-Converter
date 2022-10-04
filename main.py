import xml.etree.ElementTree as et

# xml -> [restrictions per field]* -> html form -> xml

margin = 10

def printScope(scope):
    result = ""
    for i in range(0, scope):
        result = result + " "
    return result

def write(file, input):
    file.write(input)

def traverse(root, scope, file):
    if (len(root) != 0):
        write(file, printScope(scope) + "<div style=\"margin: {}px; padding: 20px; border-style: solid; border-color: gray; background-color: #E5E8E8; border-radius: 25px;\">\n".format(margin * scope))
        write(file, printScope(scope) + "<h3>{}</h3>\n".format(root.tag))
    else:
        write(file, printScope(scope) + "<div style=\"margin: 20px;\">\n")
        write(file, printScope(scope + 1) + "<p>{}</p>\n".format(root.tag))
        write(file, printScope(scope + 1) + "<input type=\"text\" id=\"lname\" name=\"lname\" style=\"height: 100px; width: 100%;\">\n")
        write(file, printScope(scope) + "</div>\n")
    for item in root:
        traverse(item, scope + 1, file)
    if (len(root) != 0):
        write(file, printScope(scope) + "</div>\n")

def compileHTML(xml_file):
    #later change to function argument
    tree = et.parse("/Users/gabeiglio/Developer/XML-Converter/tests/test1.xml")
    root = tree.getroot()

    output = open("output.html", "a")
    traverse(root, 1, output)
    output.close()

compileHTML("")
