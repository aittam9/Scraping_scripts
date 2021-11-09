#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BS


# asking for an url to save in a variable
URL = input('Write or paste an URL:')
page = requests.get(URL)

#creating a soup object
soup = BS(page.content, 'html5lib')
#text = soup.find('div', class_ = 'article-body')

#clean the html/js tags
text1 = '\n'.join([''.join(s.findAll(text=True))for s in soup.findAll('p')])

# asking to save the text in a file
question = input('Do you want to save the text in a file?')
if question == 'yes':
    file_name = input('Choose a name for the file:')
    with open(file_name, 'w') as f:
        f.write(text1)    #.replace('\n', ''))
elif question == 'no':
    scd_qst = input('Do you want to print the text in the shell?:')
    if scd_qst == 'yes':
        print('\n', text1)
else:
    print('Unvalid command')
