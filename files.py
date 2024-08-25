""" A collection and exploration of python functions and modules for manipulating files. """

# Built In
with open("test.txt", "a") as f:
    # a Append; r Read; w Write (truncate);
    # a+ Read/Write(end); r+ Read/Write(beg); w+ Read/Write (truncate)
    # 'with' creates a 'context' that automatically closes the file after leaving the indented children.
    content = f.read()

# Standard Library
import filecmp
import fileinput
import fnmatch
import glob
import linecache
from os import path, listdir
from pathlib import Path
import shutil
import stat
import tempfile

# Third Party


# Project or Personal


def py2txt(from_dir):
    for filename in listdir(from_dir):
        f = Path(from_dir, filename)
        f.rename(str(f).replace(".py", ".txt"))


def txt2py(from_dir):
    for filename in listdir(from_dir):
        f = Path(from_dir, filename)
        f.rename(str(f).replace(".txt", ".py"))
