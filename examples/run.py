from glob import glob
import os

curdir = os.path.dirname(os.path.abspath(__file__))
examples = glob(os.path.join(curdir, '*/*.py'))

for example in examples:
    print(example)
    with open(example) as in_file:
        exec(in_file.read())
