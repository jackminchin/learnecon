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
