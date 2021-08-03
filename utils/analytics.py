import glob, os
from shutil import copyfile
import re
from os import path

rootDir = '../_build/dirhtml'

def concatDirs(dirs):
    if dirs == []:
        return ''
    else:
        return os.path.join(*dirs)
    

# Make sure that we are in the right directory.
if os.getcwd().split('/')[-1] == 'utils':
    os.chdir('../parts')
else:
    os.chdir('./parts')

for root, dirs, files in os.walk(rootDir):
    for file in files:
        # check if html file
        if(file.endswith('.html')):
            f = open(path.join(root, file))
            
            content = f.read()

            # Remove old tag here.
            newContent = re.sub(r'<script async="" src="https:\/\/www.googletagmanager.com/gtag/js\?id\=G\-2SCJHZ6L0L"><\/script>', 
                r'', content, flags = re.M)


            newContent = re.sub(r'''<script>[\s\S]*?window\.dataLayer[\s\S]*?\=[\s\S]*?window\.dataLayer[\s\S]*?\|\|[\s\S]*?\[\];[\s\S]*?function[\s\S]*?gtag\(\){ dataLayer.push\(arguments\);[\s\S]*?}[\s\S]*?gtag\('config',[\s\S]*?'G\-2SCJHZ6L0L'\);[\s\S]*?<\/script>''', 
                r'', newContent, flags = re.M)


            # Insert new tag
            addNewTag = re.sub(r'<\/head>', '<script async src="https://www.googletagmanager.com/gtag/js?id=G-2SCJHZ6L0L"></script><script>window.dataLayer=window.dataLayer || []; function gtag(){dataLayer.push(arguments);}gtag("js", new Date()); gtag("config", "G-2SCJHZ6L0L");</script></head>', newContent, flags = re.M)

            f.close()

            f_write = open(path.join(root, file), 'w')

            f_write.write(addNewTag)
            f_write.close()