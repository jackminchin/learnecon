import os
os.system('python3 -m ipykernel install --user')
os.system('jupyter-book build . --all --builder dirhtml')
os.system('python3 ./utils/setIndex.py')


#os.system('jupyter-book build . --builder pdflatex')
