# Install beautifulsoup
#pip install beautifulsoup4
# Install html5lib or lxml
# pip install html5lib or lxml
from bs4 import BeautifulSoup

with open('players.html','r') as html_file :
    html_content=html_file.read()
    print(html_content)

    parser='html5lib'
    soup =BeautifulSoup(html_content,parser)
    print(soup)
    # The title of th epage
    print('Title:',soup.title)
    print('Title text:',soup.title.text)
    # The first h3 element
    tag_object=soup.h3
    print(tag_object)
    # The concerned text
    print(tag_object.text)

    tag_child=tag_object.b
    print(tag_child)
    print(tag_child.parent)
    # Find its next sibling
    print(tag_child.attrs)

    print(tag_object.next_sibling)
