# python3
# this file enables "python3 -m huddle" to be run in terminal
# can equally just run this file to start program
# ref: https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6

# import app package (folder containing __init__.py file)
from huddle import dbtest
from huddle import dbtables
from huddle import ptsorting

# checking if the module (.py file) is being executed as the main module
if __name__ == '__main__':
    dbtest.run()
    dbtables.run()
    ptsorting.run()
