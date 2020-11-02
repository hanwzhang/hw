#kindle HTML -> Markdown; deletes space in Chinese
from bs4 import BeautifulSoup
import re

#Import and export position
name_old = input('Import - Enter file name:')
savepath = '/Users/hanwenzhang/Desktop/' + name_old[0:name_old.find('.')] + '.txt'
fh = open(name_old,'r')
fh2 = open(savepath,'w')
author_name = input('Author last name:')
note = BeautifulSoup(fh, 'html.parser')

if note.contents[0].find('，') == -1: c = False #detect Chinese using a Chinese comma
else: c = True
def cd(x): #delete space in Chinese texts
    if c == True: x = x.replace(' ','')
    return x

#Constructing note in txt
txtlines = ''
for x in note():
    try: att = x.attrs['class'][0]
    except: continue
    if att == 'sectionHeading': #chapter headings
        title = '❖' + x.contents[0].strip() + '❖'
        txtlines = txtlines + cd(title) + '\n' + '\n'
    elif att == 'noteHeading':
        if x.span != None: #highlight, generates in-text citation
            highlight = True
            loc = re.findall('Location [0-9]+', str(x))[0]
            in_text = '(' + author_name + ', loc. ' + re.findall('[0-9]+', loc)[0] + ')'
        else: highlight = False #note
    elif att == 'noteText':
        if highlight == True:
            text = x.contents[0].strip() + ' ' + in_text
            txtlines = txtlines + cd(text) + '\n' + '\n'
        else:
            text = '✪ ' + x.contents[0].strip()
             = txtlines + cd(text) + '\n' + '\n'
    else: continue

fh2.write(txtlines.rstrip())
print('done')
