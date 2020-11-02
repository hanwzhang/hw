from bs4 import BeautifulSoup
#HTML -> txt; deletes extra space in Chinese
import re

#Import and export position
name_old = input('Import - Enter file name:')
savepath = '/Users/hanwenzhang/Desktop/' + name_old[0:name_old.find('.')] + '.txt' #export path
fh = open(name_old,'r')
fh2 = open(savepath,'w')
author_name = input('Author last name:')

#html parsing -> titles, note/highlight determinant, texts
note = BeautifulSoup(fh, 'html.parser')

#Chinese detection
if note.contents[0].find('，') == -1: #detect Chinese using a Chinese comma
    c = False
else: c = True
def cd(x): #delete space in Chinese texts
    if c == True:
        x = x.replace(' ','')
    return x

#Constructing note in Markdown in string 'mdlines'
mdlines = ''
for x in note():
    try: att = x.attrs['class'][0]
    except: continue
    if att == 'sectionHeading':
        title = '⭕️' + x.contents[0].strip() + '⭕️'
        mdlines = mdlines + cd(title) + '\n' + '\n'
    elif att == 'noteHeading':
        loc = re.findall('Location [0-9]+', str(x).strip())[0]
        in_text = '(' + author_name + ', loc. ' + re.findall('[0-9]+', loc)[0] + ')'
        continue
    elif att == 'noteText':
        text = x.contents[0].strip() + ' ' + in_text
        mdlines = mdlines + cd(text) + '\n' + '\n'
    else: continue

fh2.write(mdlines.rstrip())
print('done')
