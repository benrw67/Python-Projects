from ui import *

cv = CvInterface()

with open('CV Project/cv.json', 'r+') as file:
    content = file.read()
    file.seek(0)
    content.replace('DOMAIN', cv.domain)
    content.replace('USER', cv.username)
    content.replace('PASSWORD', cv.password)
    content.replace('COMMSERVE', cv.cs_input)
    file.write(content)
