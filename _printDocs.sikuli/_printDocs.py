import pydoc
import os
from sikuli import *

# point to Sikuli folder on desktop
starting_folder = os.environ['USERPROFILE']+'\\desktop\\Sikuli\\Test_It_All'
folder_length = len(starting_folder) + 1

for x in os.walk(starting_folder):
    if x[0][-7:] == '.sikuli':
        stripped_folder = x[0][folder_length:]
        stripped_folder = stripped_folder[:-7]
        print(stripped_folder)
        pydoc.writedoc(stripped_folder)
