from xml.etree import ElementTree


tree = ElementTree.parse('example.xml')
root = tree.getroot()
'''print(root)
for genre in root:
    print(genre)
    for decade in genre:
        print(decade)

result = ElementTree.tostring(root).decode()
encoded_result = ElementTree.fromstring(result)
print(type(encoded_result))
'''

for movie in root.iter("movie"):
    print(movie.attrib['title'])
    for child in movie.findall("*"):
        print(child.text)
    #print(movie.attrib)
