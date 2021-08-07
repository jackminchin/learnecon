# Learn Econ Online Book

## Development 

### Clone the repo

`gh repo clone jackminchin/learnecon`

### Create a Virtual Environment

Firstly, create a virtual env in the learnecon working directory:

`python3 -m venv .venv`

next, activate by:

`source .venv/bin/activate`

### Install dependencies

Once you have cloned the repo and created the environment, install the required dependencies using pip.

`pip install -r requirements.txt`

### Start writing

You will then be able to run the book in development by using:

`python dev.py`

this will build and host a version of the book at `https://localhost:8001` and rebuild the book when you press save in the markdown page files. 

### Create a pull request 

Create a pull request.

## Authoring Content

Our aim is to have as many people as possible contribute high quality content to the book. Anyone can make a pull request to the repo, adding their content and helping the community. Once you have finished, you can make a pull request that will be reviewed by one of the managers. 

### Choosing Topics

You can work on (nearly) any economics topics you wish. Before you start, please seek approval by creating an issue on the repo, a repository manager will then confirm your topic. You can also contribute to existing sections.

### Adding Citations

In order to add a citation, first either find or create a bibtex style entry and append it to the `zreferences.bib` file in the project root. This can then be cited in the text with: {cite:p
}\`citationcode\`.

At the bottom of the page, if it doesn't already exist, add a bibliography by:
```
# References
<!-- ## The Neoclassical Growth Model -->
```{bibliography} ../../zreferences.bib
:filter: docname in docnames
```


### Get Credit

coming soon.

