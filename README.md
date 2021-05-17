- confirm pip3 w/ `pip3 --version`
  - get it from `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`, `python3 get-pip.py`
- `python -m venv env`, confirm in file structure
- setting up a virtual env
  - `which python3` should yield a system install like /usr/local/bin/python3
  - `source env/bin/activate`
  - now `which python3` yields this specific folder

- `pip3 install alembic` will install into our env/lib like node_modules
  - also install python-dotenv

- `alembic init migrations`
  - check out 
