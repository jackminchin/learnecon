import glob, os
from shutil import copyfile
import re

rootDir = '../_build/html'

def makeRedirectHtml(to):
    return '<meta http-equiv="Refresh" content="0; url={}" />'.format(to)


def makeRedirectIndexHtml():
    return '<meta http-equiv="Refresh" content="0; url=/intro/index.html" />'

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
            name = file.split('.')
            
    
            relPath = root.split('html')[1]
          

            os.makedirs(root + '/' + name[0], exist_ok=True)
            copyfile(root + '/' + file, root + '/' + name[0] + '/' + 'index.html')

            f_read = open(root + '/' + name[0] + '/' + 'index.html')
            
            content = f_read.read()
            c1= re.sub('\.\.\/\.\.\/', r'/', content, flags = re.M)
            c1 = re.sub('"_static', '"/_static', c1, flags=re.M)
            c1 = re.sub('href="(?!\/)', 'href="/', c1, flags=re.M)
            c1 = re.sub(r'(\w+(?=\.html))', r'\1/index', c1, flags=re.M)
            f_read.close()
            f_write = open(root + '/' + name[0] + '/' + 'index.html', 'w')

            f_write.write(c1)
            f_write.close()


            f = open(root + '/' + file, "w")

            if (name[0] == 'index'):
                f.write(makeRedirectIndexHtml())
            else:
                f.write(makeRedirectHtml(relPath + '/' + name[0] + '/' + 'index.html'))
            f.close()


