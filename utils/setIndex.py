import os

# Make sure that we are in the right directory.
if os.getcwd().split('/')[-1] == 'utils':
    os.chdir('../_build/dirhtml')
else:
    os.chdir('./_build/dirhtml')


def makeRedirectIndexHtml():
    return '<meta http-equiv="Refresh" content="0; url=/intro/index.html" />'


f = open('index.html', "w")
f.write(makeRedirectIndexHtml())
f.close()