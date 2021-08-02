import os
os.system('python -m ipykernel install --user')
os.system('jupyter-book build . --all --builder dirhtml')
os.system('python ./utils/setIndex.py')


#os.system('jupyter-book build . --builder pdflatex')
